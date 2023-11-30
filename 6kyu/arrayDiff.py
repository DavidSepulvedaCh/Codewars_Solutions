"""  

    DESCRIPTION:
        Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

        It should remove all values from list a, which are present in list b keeping their order.

        array_diff([1,2],[1]) == [2]

"""


def array_diff(a, b):
    result = []
    for element in a:
        if element not in b:
            result.append(element)
    return result
