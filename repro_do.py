from resolute import do, Ok, Err, Result

@do()
def branching_test(x: int) -> Result[int, str]:
    if x > 0:
        val = yield Ok(x)
        return val * 2
    else:
        val = yield Ok(100)
        return val + 1

@do()
def early_err_test(x: int) -> Result[int, str]:
    if x == 0:
        yield Err("zero")
    return x * 2

def main():
    print(f"branching_test(5): {branching_test(5)}")
    print(f"branching_test(-1): {branching_test(-1)}")
    print(f"early_err_test(0): {early_err_test(0)}")
    print(f"early_err_test(5): {early_err_test(5)}")

if __name__ == "__main__":
    main()
