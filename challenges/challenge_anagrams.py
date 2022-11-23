def element_partition(list, initPos, endPos):
    pivot = list[endPos]
    index = initPos - 1
    for j in range(initPos, endPos):
        if list[j] <= pivot:
            index += 1
            list[index], list[j] = list[j], list[index]
    list[index + 1], list[endPos] = list[endPos], list[index + 1]
    return index + 1


def order_elements(array, initPos, endPos):
    if initPos < endPos:
        pivot = element_partition(array, initPos, endPos)
        order_elements(array, initPos, pivot - 1)
        order_elements(array, pivot + 1, endPos)
    return array


def is_anagram(first_string, second_string):
    firstString = list(first_string.lower())
    secondString = list(second_string.lower())
    resultFirstString = order_elements(firstString, 0, len(firstString) - 1)
    resultSecondString = order_elements(secondString, 0, len(secondString) - 1)
    if resultFirstString == "" or resultSecondString == "":
        validateResult = False
    validateResult = resultFirstString == resultSecondString
    return (
        "".join(resultFirstString),
        "".join(resultSecondString),
        validateResult,
    )
