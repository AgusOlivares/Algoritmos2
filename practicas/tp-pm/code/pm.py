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


