def is_palindrome_recursive(word, low_index, high_index):
    palindrome = False
    pos = 0
    while pos < len(word):
        if word == "":
            return False
        elif high_index <= low_index:
            return True
        else:
            palindrome = (
                word[low_index] == word[high_index]
                and is_palindrome_recursive(
                    word, low_index + 1, high_index - 1
                )
            )
        pos += 1
    return palindrome


#  Segundo Jeito de fazer
    # if word == "":
    #     return False
    # elif high_index <= low_index:
    #     return True
    # elif word[low_index] == word[high_index]:
    #     initial_index = low_index + 1
    #     final_index = high_index - 1
    #     return is_palindrome_recursive(word, initial_index, final_index)
    # return False
