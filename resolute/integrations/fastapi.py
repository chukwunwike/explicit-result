from typing import Any, TypeVar, Optional, Union
from fastapi import HTTPException
from .._result import Result
from .._option import Option, Nothing

T = TypeVar("T")

def unwrap_or_http(
    result: Union[Result[T, Any], Option[T]],
    status_code: int = 404,
    detail: Optional[str] = None
) -> T:
    """
    Unwrap a Result or Option, or raise a FastAPI HTTPException.
    
    If it's an Err or Nothing, raises HTTPException with the given status_code.
    The 'detail' defaults to the error value for Results, or 'Not found' for Options.
    """
    if isinstance(result, Result):
        if result.is_ok():
            return result.unwrap()
        raise HTTPException(
            status_code=status_code,
            detail=detail or str(result.unwrap_err())
        )
    
    # Handle Option
    if result.is_some():
        return result.unwrap()
    
    raise HTTPException(
        status_code=status_code,
        detail=detail or "Not found"
    )
