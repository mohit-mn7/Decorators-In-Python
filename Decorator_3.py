def is_called():
    print("Hello from Called Function!")
    def is_returned():
        print("Hello from Returned Function!")
    return is_returned


new = is_called()

new()
