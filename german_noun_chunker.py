from textblob_de import TextBlobDE as TextBlob
import itertools

def grouper(n, it):
    # grouper(3, 'ABCDEFG') --> ABC DEF G
    it = iter(it)
    return iter(lambda: list(itertools.islice(it, n)), [])

def is_empty(line):
    return len(line.strip())==0

def main():
    with open("german_text.txt", "r") as input_file, open("german_output.tchunk", "w") as output_file:
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
    main()
