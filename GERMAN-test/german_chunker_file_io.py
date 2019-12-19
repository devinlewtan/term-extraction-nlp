import sys

## takes as input a .list file and outputs a new modified list
## where all of the old .txt files are renamed to .tchunk files

def update_list(old_list):
    # split the old file name from its tag and make it the new file name with format XXX_new.list
    # listname_old = sys.argv[1]
    listname_old = old_list
    listname_old_tag = listname_old.rsplit('.',1)[0]
    listname_new = listname_old.rsplit('.',1)[0] + "_new.list"

    with open(listname_old, encoding='utf-8') as input_file, open(listname_new,"w", encoding='utf-8') as output_file:
        for line in input_file:
            file_name_without_tag = line.rsplit('.', 1)[0]
            filename_new = listname_old_tag + "/" + file_name_without_tag+".tchunk\n"
            output_file.write(filename_new)
if __name__ == "__main__":
    update_list()
