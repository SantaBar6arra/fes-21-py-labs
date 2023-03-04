import sys
sys.path.append('../src')
from file_utils import count_sentences, count_words


# todo: more files for test cases
def count_words_test() -> None:
    file = open('../text.txt', 'r')
    txt: str = file.read()
    file.close() 
    
    assert count_words(txt) == 69
    
def count_sentences_test() -> None:
    file = open('../text.txt', 'r')
    txt: str = file.read()
    file.close() 
    
    assert count_sentences(txt) == 4
    