from typing import Tuple
from file_utils import read_file 
from text_utils import get_all_palindromes, get_palingrams, get_palingrams_v2


res: Tuple[str, int, int] = read_file('../text.txt')
print(f"""
file_name: {res[0]} 
# of words: {res[1]}
# of sentences: {res[2]}
""")

file = open('../text.txt')
palindromes: dict = get_all_palindromes(file.read())
print(palindromes)
file.close()

file = open('../palingrams_sus.txt')
txt: str = file.read()
print(get_palingrams(txt))
print() 
print(get_palingrams_v2(txt))
file.close()
