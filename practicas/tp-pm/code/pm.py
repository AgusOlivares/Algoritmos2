 # c: Character
def existChar(String, c):
    for i in String:
        if i == c:
            return True
    return False
    
def isPalindrome(String):

    string_sinEspacios = String.replace(" ", "")

    mid_char = len(string_sinEspacios) // 2

    for i in range(len(string_sinEspacios[:mid_char])):
        if string_sinEspacios[i] != string_sinEspacios[len(string_sinEspacios) - i - 1]:
            return False
    return True
    
def mostRepeatedChar(String, c):

    dict = {}
    
    for i in String:
        dict[i] =+ 1

    return max(dict, key = dict.get)


def reduceLen(String):

    reduced_list = []
    for char in String:

            if char == (reduced_list and reduced_list[-1]):
                reduced_list.pop()
            else:
                reduced_list.append(char)
    return reduced_list

def isContained(String, SubString):

    long_SubString = len(SubString)

    comprobation_array = [False] * long_SubString
    i = 0

    for char in String:
        if char == SubString[i]:
            comprobation_array[i] = True
            i += 1
        if i == long_SubString:
            break
    if comprobation_array.count(True) == long_SubString:
        return True
    else:
        return False


