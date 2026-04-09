from resolute import Ok, Err
import os

def fail():
    return 1 / 0

def run_test(label, verbose_val):
    os.environ["RESOLUTE_VERBOSE_ERROR"] = str(verbose_val)
    # Note: we need to re-import or rely on property sensing
    try:
        fail()
    except Exception as e:
        res = Err(e)
        print(f"--- {label} (Env: {verbose_val}) ---")
        print(res)
        print()

print("VERIFYING CONFIGURABLE VERBOSITY\n")
run_test("VERBOSE MODE", "1")
run_test("CONCISE MODE", "0")
