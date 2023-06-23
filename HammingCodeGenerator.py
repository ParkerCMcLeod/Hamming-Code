def get_binary_input():
    binary_string = ""
    while True:
        input_string = input(
            "\nEnter a sequence of binary data to be encoded (0s and 1s): "
        )

        valid = True
        for c in input_string:
            if c != "0" and c != "1":
                print("\nInvalid input.\n")
                valid = False
                break
            else:
                binary_string = input_string
                break

        if valid:
            break

    return binary_string


binary_string = get_binary_input()

print(f"\nBinary sequence entered: {binary_string}\n")
