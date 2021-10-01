def char_to_int(character: str) -> int:
    return ord(character) - ord('a')

def int_to_char(ascii: int) -> str:
    return chr(ascii + ord('a'))

def displace(cypher: str, displacement: int) -> str:
    if(cypher == ' '):
        return ' '
    elif(cypher == '"'):
        return '"'
    else:
        return int_to_char((char_to_int(cypher)+displacement) % 26)

def cipher(word: str,displacement: int) -> str:
    return ''.join([displace(x, displacement) for x in word])

def decrypt(word: str, ascii: int) -> str:
    return ''.join([displace(x, -ascii) for x in word])