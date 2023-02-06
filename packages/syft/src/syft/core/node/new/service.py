# stdlib
import inspect
from inspect import Parameter
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Type

# relative
from ....core.node.common.node_table.syft_object import SyftObject
from ...common.serde.serializable import serializable
from ...common.uid import UID
from .signature import Signature


class AbstractNode:
    id: UID


class AbstractService:
    node: AbstractNode
    node_uid: UID


@serializable(recursive_serde=True)
class ServiceConfig(SyftObject):
    public_path: str
    private_path: str
    public_name: str
    method_name: str
    doc_string: Optional[str]
    signature: Signature
    permissions: List


class ServiceConfigRegistry:
    __service_config_registry__: Dict[str, ServiceConfig] = {}
    __public_to_private_path_map__: Dict[str, str] = {}

    @classmethod
    def register(cls, config: ServiceConfig) -> None:
        if not cls.path_exists(config.public_path):
            cls.__service_config_registry__[config.public_path] = config
            cls.__public_to_private_path_map__[config.public_path] = config.private_path

    @classmethod
    def private_path_for(cls, public_path: str) -> str:
        return cls.__public_to_private_path_map__[public_path]

    @classmethod
    def get_registered_configs(cls) -> Dict[str, ServiceConfig]:
        return cls.__service_config_registry__

    @classmethod
    def path_exists(cls, path: str):
        return path in cls.__service_config_registry__


def deconstruct_param(param: inspect.Parameter) -> Dict[str, Any]:
    # Gets the init signature form pydantic object
    param_type = param.annotation
    if not hasattr(param_type, "__signature__"):
        raise Exception(
            f"Type {param_type} needs __signature__. Or code changed to support backup init"
        )
    signature = param_type.__signature__
    sub_mapping = {}
    for k, v in signature.parameters.items():
        sub_mapping[k] = v
    return sub_mapping


def expand_signature(signature: Signature, autosplat: List[str]) -> Signature:
    new_mapping = {}
    for k, v in signature.parameters.items():
        if k in autosplat:
            sub_mapping = deconstruct_param(v)
            for s, t in sub_mapping.items():
                new_t_kwargs = {
                    "annotation": t.annotation,
                    "name": t.name,
                    "default": t.default,
                    "kind": Parameter.POSITIONAL_OR_KEYWORD,
                }
                new_t = Parameter(**new_t_kwargs)
                new_mapping[s] = new_t
        else:
            new_mapping[k] = v

    return Signature(
        **{
            "parameters": list(new_mapping.values()),
            "return_annotation": signature.return_annotation,
        }
    )


def service_method(
    name: Optional[str] = None,
    path: Optional[str] = None,
    autosplat: Optional[List[str]] = None,
):
    def wrapper(func):
        func_name = func.__name__
        class_name = func.__qualname__.split(".")[-2]
        _path = class_name + "." + func_name
        signature = inspect.signature(func)
        if autosplat is not None and len(autosplat) > 0:
            signature = expand_signature(signature=signature, autosplat=autosplat)

        config = ServiceConfig(
            public_path=_path if path is None else path,
            private_path=_path,
            public_name=("public_" + func_name) if name is None else name,
            method_name=func_name,
            doc_string=func.__doc__,
            signature=signature,
            permissions=["Guest"],
        )
        ServiceConfigRegistry.register(config)

        def _decorator(self, *args, **kwargs):
            return func(self, *args, **kwargs)

        return _decorator

    return wrapper


class SyftServiceRegistry:
    __service_registry__: Dict[str, Callable] = {}

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        if hasattr(cls, "__canonical_name__") and hasattr(cls, "__version__"):
            mapping_string = f"{cls.__canonical_name__}_{cls.__version__}"
            cls.__object_version_registry__[mapping_string] = cls

    @classmethod
    def versioned_class(cls, name: str, version: int) -> Optional[Type["SyftObject"]]:
        mapping_string = f"{name}_{version}"
        if mapping_string not in cls.__object_version_registry__:
            return None
        return cls.__object_version_registry__[mapping_string]

    @classmethod
    def add_transform(
        cls,
        klass_from: str,
        version_from: int,
        klass_to: str,
        version_to: int,
        method: Callable,
    ) -> None:
        mapping_string = f"{klass_from}_{version_from}_x_{klass_to}_{version_to}"
        cls.__object_transform_registry__[mapping_string] = method

    @classmethod
    def get_transform(
        cls, type_from: Type["SyftObject"], type_to: Type["SyftObject"]
    ) -> Callable:
        klass_from = type_from.__canonical_name__
        version_from = type_from.__version__
        klass_to = type_to.__canonical_name__
        version_to = type_to.__version__
        mapping_string = f"{klass_from}_{version_from}_x_{klass_to}_{version_to}"
        return cls.__object_transform_registry__[mapping_string]
