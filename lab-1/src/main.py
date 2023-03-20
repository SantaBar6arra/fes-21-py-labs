from typing import Tuple
from functions import readFile, getAllPalindromes, getPalingramsSimplified, getPalingramsExtended


result: Tuple[str, int, int] = readFile('C:/Programming/Projects/LNU labs/My labs/Python/fes-21-py-labs/lab-1/text.txt')
print(f"""
File name: {result[0]} 
Cuantity of words: {result[1]}
Cuantity of sentences: {result[2]}
""")

textFile = open('C:/Programming/Projects/LNU labs/My labs/Python/fes-21-py-labs/lab-1/text.txt')
palindromes: dict = getAllPalindromes(textFile.read())
print("---------------------") 
print(palindromes)
textFile.close()

textFile = open('C:/Programming/Projects/LNU labs/My labs/Python/fes-21-py-labs/lab-1/palingrams_sus.txt')
text: str = textFile.read()
print("---------------------") 
print(getPalingramsSimplified(text))
print("---------------------") 
print(getPalingramsExtended(text))
print("---------------------") 

textFile.close()