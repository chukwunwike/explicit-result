from resolute import safe, Result

@safe
def negate(x: int) -> int:
    return -x

@safe()
def negate_with_parens(x: int) -> int:
    return -x

print("Calling negate(5)...")
try:
    res = negate(5)
    print("negate(5) result:", res)
except Exception as e:
    print("negate(5) failed:", e)

print("\nCalling negate_with_parens(5)...")
try:
    res = negate_with_parens(5)
    print("negate_with_parens(5) result:", res)
except Exception as e:
    print("negate_with_parens(5) failed:", e)
