import functools
from resolute import do, Ok, Result

@do()
def pipeline() -> Result[int, str]:
    """Test documentation."""
    x = yield Ok(1)
    return x

print("pipeline name:", pipeline.__name__)
print("pipeline doc:", pipeline.__doc__)
print("pipeline module:", pipeline.__module__)
print("pipeline qualname:", getattr(pipeline, "__qualname__", "MISSING"))
print("pipeline annotations:", getattr(pipeline, "__annotations__", "MISSING"))
print("pipeline wrapped:", getattr(pipeline, "__wrapped__", "MISSING"))

if pipeline.__name__ == "pipeline" and pipeline.__doc__ == "Test documentation.":
    print("\nBasic metadata preserved.")
else:
    print("\nBasic metadata LOST.")

if getattr(pipeline, "__qualname__", "") == "pipeline":
     print("Qualname preserved.")
else:
     print("Qualname LOST or mismatched:", getattr(pipeline, "__qualname__", "MISSING"))

if hasattr(pipeline, "__wrapped__"):
    print("Wrapped attribute present.")
else:
    print("Wrapped attribute MISSING.")
