"""
explicit-result: Result & Option Types for Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A production-grade, zero-dependency library providing Result and Option types
for explicit error handling and functional programming in Python.

Key Features:
- Monadic Result[T, E] and Option[T] types.
- Type-safe error propagation with @do and @do_option decorators.
- Transparent exception wrapping with @safe and @safe_async.
- Configurable error visibility and full Pydantic v2 support.

Usage:
    >>> from explicit_result import Ok, Err, Result
    >>> def parse_int(s: str) -> Result[int, str]:
    ...     try:
    ...         return Ok(int(s))
    ...     except ValueError:
    ...         return Err(f"Not a number: {s}")
"""

# Core types
from ._result import Result, Ok, Err
from ._option import Option, Some, Nothing, _NothingType

# Decorators
from ._decorators import safe, safe_async

# Combinators
from ._combinators import (
    collect,
    collect_all,
    partition,
    flatten_result,
    flatten_option,
    sequence,
    transpose,
    transpose_result,
)

# Exceptions
from ._exceptions import UnwrapError, SafeDecoratorError

# Context propagation
from ._context import ContextError

# Async helpers
from ._async_helpers import (
    from_awaitable,
    map_async,
    and_then_async,
    from_optional_async,
    map_option_async,
    and_then_option_async,
)

# Do-notation
from ._do import do, do_option

__all__ = [
    # Result
    "Result",
    "Ok",
    "Err",
    # Option
    "Option",
    "Some",
    "Nothing",
    # Decorators
    "safe",
    "safe_async",
    # Combinators
    "collect",
    "collect_all",
    "partition",
    "flatten_result",
    "flatten_option",
    "sequence",
    "transpose",
    "transpose_result",
    # Exceptions
    "UnwrapError",
    "SafeDecoratorError",
    # Context propagation
    "ContextError",
    # Async helpers
    "from_awaitable",
    "map_async",
    "and_then_async",
    "from_optional_async",
    "map_option_async",
    "and_then_option_async",
    # Do-notation
    "do",
    "do_option",
]

__version__ = "0.3.1"
__author__ = "explicit_result contributors"
__license__ = "MIT"

