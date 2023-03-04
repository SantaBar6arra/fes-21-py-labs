from typing import Tuple
import re


def read_file(file_path: str) -> Tuple[str, int, int]:
    """ 
    reads file in the path specified. 

    returns: Tuple[<file name>, <count of words>, <count of sentences>]
    """
    file = open(file_path, 'r')

    txt: str = file.read()

    res: Tuple[str, int, int] = (file_path, count_words(txt), count_sentences(txt))

    file.close()

    return res


def count_words(in_txt: str) -> int:
    """
    counts the count of words in the string specified

    returns: integer value of how much words there are
    """
    return len(re.findall(r'\b\w+\b', in_txt))


def count_sentences(in_txt: str) -> int:
    """
    counts the count of sentences in the string specified

    returns: integer value of how much sentences there are
    """
    return len(re.findall(r'([A-Z][^\.!?]*[\.!?])', in_txt))
