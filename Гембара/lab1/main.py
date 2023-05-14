def read_file(file_path: str) -> tuple[str, int, int]:
    try:
        with open(file_path) as f:
            cont = f.read()
            words_count = len(cont.split())
            sentence_count = len(cont.split('.'))
    finally:
        return (cont, words_count, sentence_count)


def check_palindrome(word: str) -> bool:
    for i in range(0, int(len(word) / 2)):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True


def get_all_palindromes(content: str) -> dict:
    try:
        with open(content) as f:
            my_dict = {}
            cont = f.read()
            words = cont.split()
            for word in words:
                if check_palindrome(word) == True:
                    my_dict[len(my_dict)] = word
    finally:
        return my_dict

def get_palingrams(content: str) -> dict:
    try:
        with open(content) as f:
            my_dict = {}
            cont = f.read()
            sentences = cont.split(".")
            for sentence in sentences:
                if check_palindrome(''.join(sentence.split(' '))) == True:
                    if ''.join(sentence.split(' ')) != '':
                        my_dict[len(my_dict)] = sentence
    finally:
        return my_dict

print(read_file('ny.txt'), get_palingrams("ny.txt"), get_all_palindromes('ny.txt'))
