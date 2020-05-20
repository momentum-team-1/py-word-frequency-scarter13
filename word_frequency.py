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
    #print(no_stop_words)
        #find the longest word to use for indention purposes
    word_length = 0
    for word in no_stop_words:
        if len(word) > word_length:
            #print (word, len(word))
            word_length = len(word)
    #print (word_length)
        #count remaining word usage
    word_counts = {}
    for word in no_stop_words:
        if word in word_counts:
            word_counts[word] +=1
        else: word_counts[word] = 1
    #print (word_counts)
        #sort words by frequency
    ordered_by_freq = (sorted(word_counts.items(), key=lambda seq: seq[1], reverse=True))
    #print (ordered_by_freq)
        #print words, freq, graph, indent, and add a space past the pipe for values less than 10
    for key, value in ordered_by_freq:
        indent = (word_length + 1 - len(key))
        space = " "
        star = "*"
        if value >= 10:
            print (indent * space, key, " | ", value, value * star)
        else:
            print (indent * space, key, " |  ", value, value * star)
    

   
    

    

    



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
