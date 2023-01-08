
import re
from unicodedata import normalize
from typing import List

regex_pattern = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.:]+')

def slugify(text: str, delim='_') -> str:
    """
    https://stackoverflow.com/questions/9042515/normalizing-unicode-text-to-filenames-etc-in-python
    """
    splitted_text: List[str] = regex_pattern.split(str(text))

    #Compatibility decomposition. Example 𝓱𝓲 -> hi
    result = [
        normalize('NFKD',word).encode('ascii', 'ignore').decode('utf-8') \
        for word in splitted_text if word
    ]
    return delim.join(result)


def create_mp3_filename(text: str) -> str:
    return f'{slugify(text)}.mp3'
