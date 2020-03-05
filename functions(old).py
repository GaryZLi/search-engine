def parse(text):
    tokens = []
    length = len(text)
    char = 0

    while char < length:
        if text[char] == '<':      
            while char < length and text[char] != '>':
                char += 1
        else:
            while char < length and text[char] == ' ':
               char += 1
        
            start = char

            #                          0 - 9                                              A-Z                                                a-z
            while char < length and ( (ord(text[char]) > 47 and ord(text[char]) < 58) or (ord(text[char]) > 64 and ord(text[char]) < 91) or (ord(text[char]) > 96 and ord(text[char]) < 123) ):
                char += 1
            
            temp = text[start:char]
            if len(temp) > 0:
                tokens.append(temp)

            if char < length and text[char] != '<':
                char += 1

    return tokens


# with open('name.json', 'r') as file:
#     text = json.loads(file.read())['content']

#     print(parse(text))

# <a>fadsfkjldskljfds</a>fsdhjklsdf