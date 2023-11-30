"""  
    DESCRIPTION:
        Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

        Examples:

        * 'abc' =>  ['ab', 'c_']
        * 'abcdef' => ['ab', 'cd', 'ef']

"""


def solution(s):
    x = []
    for i in range(0, len(s), 2):
        par = s[i:i+2]
        x.append(par)

    if len(s) % 2 != 0:
        x[-1] += '_'

    return x
