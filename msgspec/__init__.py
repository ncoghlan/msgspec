from ._core import (
    DecodeError,
    EncodeError,
    Field as _Field,
    Meta,
    MsgspecError,
    Raw,
    Struct,
    UnsetType,
    UNSET,
    NODEFAULT,
    ValidationError,
    defstruct,
    convert,
    to_builtins,
)


def field(*, default=NODEFAULT, default_factory=NODEFAULT, name=None):
    return _Field(default=default, default_factory=default_factory, name=name)


field.__doc__ = _Field.__doc__


from . import msgpack
from . import json
from . import yaml
from . import toml
from . import inspect
from . import structs

# Override version info for a Python 3.13 compatible pre-release
# that can be built from a GitHub source tarball
#
# This is an interim workaround while waiting for the next upstream release:
#
# * https://github.com/jcrist/msgspec/issues/764
# * https://github.com/jcrist/msgspec/issues/777
#
# Hardcoding the version allows this to be built from a GitHub commit
# tarball rather than having to trust a third party build process

__version__ = "0.18.7.dev0+ncoghlan-py313-prerelease"
