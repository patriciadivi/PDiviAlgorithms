def is_palindrome_iterative(word):
    if word == '':
        return False

    palindrome = False
    pos = 0
    meio = len(word) // 2
    while pos <= meio:
        palindrome = word[pos] == word[-pos-1]
        pos += 1
    return palindrome
