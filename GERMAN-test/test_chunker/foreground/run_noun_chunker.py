import sys, german_noun_chunker

def main():
    list = sys.argv[1]
    input_file = open(list, encoding='utf-8')
    for line in input_file:
        german_noun_chunker.run_chunker(line)

if __name__ == '__main__':
    main()
