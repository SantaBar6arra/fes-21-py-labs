from typing import Tuple 
from function import *

CountWordsTest()
IsPalinfrome_Test()
GetPalingrams_Test()
GetPalingrams_V2_Test()
print('everything passed')

MyFile: Tuple[str, int] = ReadFile('C:/Users/Ivan/OneDrive/Рабочий стол/Folders/Lab for Uni/course2sem2/lab1py/text.txt')
print(f"""
Назва файлу: {MyFile[0]}
Кількість слів: {MyFile[1]}""")

file = open('C:/Users/Ivan/OneDrive/Рабочий стол/Folders/Lab for Uni/course2sem2/lab1py/text.txt')
palindromes: dict = GetAllPalindromes(file.read())
print(palindromes)
print("*********************************************")
file.close()

file = open('C:/Users/Ivan/OneDrive/Рабочий стол/Folders/Lab for Uni/course2sem2/lab1py/palingrams_sus.txt')
txt: str = file.read()
print(GetPalingrams(txt))
print("*********************************************") 
print(GetPalingrams_Better(txt))
file.close()
