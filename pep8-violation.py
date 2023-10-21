# https://peps.python.org/pep-0008/

# Wrong:

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
                          var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
