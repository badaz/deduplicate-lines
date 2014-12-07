# -*- coding: utf-8 -*-

import argparse

def main():
    """Deduplicates lines in a file. Takes input file path and outputfile
    file path as arguments. Creates a deleted.txt file containing
    deleted lines. Outputs the total count of deleted lines in file.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="input file")
    parser.add_argument("output_file", type=str, help="output file")

    args = parser.parse_args()

    # count = deduplicate_lines_in_file(file_paths[0], file_paths[1])
    count = deduplicate_lines_in_file(args.input_file, args.output_file)
    # print 'Input file is', file_paths[0]
    # print 'Output file is', file_paths[1]
    print 'Input file is', args.input_file
    print 'Output file is', args.output_file
    print 'Number of lines removed :', count
    print 'Duplicate lines copied to deleted.txt'


def deduplicate_lines_in_file(file_path, new_file_path):
    """Deduplicates lines in a file. file_path points to the origin file,
    new_file_path points to the new file with only unique lines. function
    also creates a deleted.xml file containing all deleted lines and returns
    the count of deleted lines.
    """
    with open(file_path, 'r') as read_file:
        with open(new_file_path, 'w') as written_file:
            with open('deleted.txt', 'w') as deleted_file:
                text, count, deleted = deduplicate_lines(read_file.read())
                written_file.write(text)
                deleted_file.write(deleted)
                return count


def deduplicate_lines(str):
    """Iterates over every line. if the line is not in seen list, 
    adds it to the list, else adds it to deleted list and increment
    count by 1.
    """
    count = 0
    str_list = str.split('\n')
    seen = []
    del_str_list = []

    for line in str_list:
        if line in seen:
            count += 1
            del_str_list.append(line)
        else:
            seen.append(line)

    nl = '\n'
    seen_str = nl.join(seen)
    deleted_str = nl.join(del_str_list)
    return seen_str, count, deleted_str

if __name__ == "__main__":
    main()
