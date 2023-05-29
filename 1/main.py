import re

def read_file(file_path: str) -> tuple[str, int, int]:
    with open(file_path, 'r') as file:
        text = file.read()

    s = re.split(r'[.!?]+', text)
    s = [s.strip() for s in s if s.strip()]

    words = re.findall(r'\b\w+\b', text)

    return text, len(s), len(words)


def check_palindrome(word: str) -> bool:
    word = ''.join(c for c in word if c.isalpha()).lower()
    return word == word[::-1]

def get_all_palindromes(content: str) -> dict:
    try:
        with open(content) as file:
            cont = file.read()
        my_dict = {}
        words = cont.split()
        for word in words:
            if check_palindrome(word) == True:
                my_dict[len(my_dict)] = word
    finally:
        return my_dict

def get_palingrams(content: str) -> dict:
    try:
        with open(content) as f:
            cont = f.read()
        my_dict = {}
        sentences = cont.split(".")
        for sentence in sentences:
            if check_palindrome(''.join(sentence.split(' '))) == True:
                if ''.join(sentence.split(' ')) != '':
                    my_dict[len(my_dict)] = sentence
    finally:
        return my_dict

print(read_file('flop.txt'), get_palingrams("flop.txt"), get_all_palindromes('flop.txt'))
