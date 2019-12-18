from textblob_de import TextBlobDE as TextBlob
import itertools, sys

def grouper(n, it):
    # grouper(3, 'ABCDEFG') --> ABC DEF G
    it = iter(it)
    return iter(lambda: list(itertools.islice(it, n)), [])

def is_empty(line):
    return len(line.strip())==0

def run_chunker(list_name):
    # list_name = sys.argv[1]
    # read in foreground.list file line by line as input for the file names to put into noun chunker
    # with open(foreground_list) as foreground_file:
    #     # read each line of the foreground.list file and then split the .txt tag out
    #     line = foreground_file.readline()
    file_name_without_tag = list_name.rsplit('.', 1)[0]
    # for every line that is read, use noun chunker on it and output .tchunk file
    with open(file_name_without_tag+".txt", "r", encoding='utf-8') as input_file, open(file_name_without_tag+".tchunk", "w", encoding='utf-8') as output_file:
        for line in input_file:
            if is_empty(line):
                continue
            line = TextBlob(line).parse().split('/')
            tags = list(grouper(3, line))
            for t in tags:
                word = t[0].split()
                if len(t) > 1:
                    if len(word) > 1:
                        word = word[1]
                    else:
                        word = word[0]
                    pos = t[1]
                    chunk = t[2]
                    output_file.write(f"{word}\t{word}\t{pos}\t{chunk}\n")
            output_file.write("\n")

if __name__ == "__main__":
    run_chunker()
