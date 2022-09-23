from typing import List, Set, Dict, Optional

# MYPY ----------------------------------------
# http://www.mypy-lang.org/

x: int = 2


def fail(y: str):
    print(y)


fail(x)  # Argument 1 to "fail" has incompatible type "int"; expected "str"

# missing attr
class Missing:
    def __init__(self, name: str) -> None:
        self.name = name


m = Missing()  # Missing positional argument "name" in call to "Missing"
print(m.missing)  # "Missing" has no attribute "missing"

notafunction()  # Name "notafunction" is not defined


# PYLINT ----------------------------------------
# https://pylint.pycqa.org/en/latest/index.html

def noreturn():
    print("not returning a value")
x = noreturn() # Assingning result of a function call, where the function has no return [assignment-from-no-return]



if __name__ == "__main__":
    print("this should not have run.")
