import sys, german_noun_chunker, german_chunker_file_io

def main():
    list = sys.argv[1]
    german_chunker_file_io.update_list(list)
    input_file = open(list, encoding='utf-8')
    for line in input_file:
        german_noun_chunker.run_chunker(line)

if __name__ == '__main__':
    main()
