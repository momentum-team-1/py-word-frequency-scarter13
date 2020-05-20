STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

import string
punctuation = string.punctuation

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    opened_file = open(file)
    text = opened_file.read()
    #print(text)
        #replace hyphens
    no_hyphen = text.replace("-"," ")
        #remove punctuation
    no_punctuation = ""
    for char in no_hyphen:
        if char not in punctuation:
            no_punctuation = no_punctuation + char
        #make everything lowercase
    lower_case_text = no_punctuation.lower()
    #print(lower_case_text)
        #split into words
    all_words = lower_case_text.split()
    #print(all_words)
        #remove stop words
    no_stop_words = []
    for each_word in all_words:
        if each_word not in STOP_WORDS:
            no_stop_words.append(each_word)
    print(no_stop_words)
    

    



    #remove the stop words
    #count the frequency of the remaing words (see ex 6 for sort function)
    #output as a cord list, count and graph of *** (ex 7 for justify)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
