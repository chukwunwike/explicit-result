import asyncio
from resolute import safe, Ok, Err, Result
from resolute._async_helpers import map_async, and_then_async, or_else_async

def test_safe():
    try:
        @safe(Exception) # pass Exception as func
        def bad(): pass
        print("@safe(Exception) worked?")
    except Exception as e:
        print(f"@safe(Exception) failed with: {type(e).__name__}: {e}")

async def test_async_helpers():
    res = Ok(1)
    
    # Is map_async taking function first or result first?
    # In resolute._async_helpers, it is def map_async(result: Result[T, E], f: Callable[[T], Awaitable[U]])
    # It works, but maybe the names or argument orders are considered inconsistent?
    pass

if __name__ == '__main__':
    test_safe()
    asyncio.run(test_async_helpers())
