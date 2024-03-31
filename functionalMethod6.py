def outer():
    def inner():
        print("Im functional inner")

    # Function outer() returns function inner()
    return inner

function = outer()
function

function()

outer()()