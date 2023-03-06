# setup_wordlist.py

import pathlib
import sys
from string import ascii_letters

in_path = pathlib.Path(sys.argv[1])
out_path = pathlib.Path(sys.argv[2])

"""
*in_path* supplies create_wordlist() with a plaintext file
*out_path* is the output filename for a wordlist that setup will populate with 5 letter words

## Example

>>> in_path = pathlib.Path('test_input.txt')
>>> out_path = pathlib.Path('test_output.txt')
>>> create_wordlist(in_path,out_path)

These are the 5 length words pulled from test_input.txt
beats
break
cases
first
great
never
often
there
"""

def create_wordlist(in_file, outfile):

    words = sorted(
        {
            word.lower()
            for word in in_path.read_text(encoding="utf-8").split()
            if all(letter in ascii_letters for letter in word) and len(word) == 5
        },
        key = lambda word: (len(word), word),
    )
    print(f"These are the 5 length words pulled from {in_path}")
    print("\n".join(words))

    out_path.write_text("\n".join(words))

if __name__ == '__main__':
    create_wordlist(in_path, out_path)
