import json

import sys
import getopt

def read_data(filename):
    ret = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for each_line in lines:
            ret.append(json.loads(each_line))

    return ret

def write_data(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for each_line in lines:
            f.write(json.dumps(each_line, ensure_ascii=False) + '\n')


# press 'enter' to skip
def mark_characters(lines, character_table):
    print('press enter to skip')
    for i, each_char in enumerate(character_table):
        print(f'press {i}: {each_char}')
    
    for each_line in lines:
        name = each_line['name']
        line = each_line['text']
        print(f'character: {name}, text: {line}')

        val = input('please input character: ')

        if val.isdigit():
            each_line['name'] = character_table[int(val)]



def main(argv):
    input_path = ""
    output_path = ""
    try:
        opts, args = getopt.getopt(argv[1:], "hi:o:", ["help", "input=", "output="])

        # 处理 返回值options是以元组为元素的列表。
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print('mark.py -i <input_path> -o <output_path>')
                print('or: mark.py --input=<input_path> --output=<output_path>')
                sys.exit()
            elif opt in ("-i", "--input"):
                input_path = arg
            elif opt in ("-o", "--output"):
                output_path = arg
    except getopt.GetoptError:
        print('Error: mark.py -i <input_path> -o <output_path>')
        print('   or: mark.py --input=<input_path> --output=<output_path>')
        sys.exit(2)

    character_table = ['unk', 'chino', 'kokoa', 'rize', 'teitsupi', 'takahiro', 'chiya', 'sharo']
    lines = read_data(input_path)
    mark_characters(lines, character_table)
    write_data(output_path, lines)

if __name__ == "__main__":
    main(sys.argv)