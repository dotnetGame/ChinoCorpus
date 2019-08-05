import json

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


# press 's' for skip
def mark_characters(lines, character_table):
    print('press "s" for skip')
    for i, each_char in enumerate(character_table):
        print(f'press {i}: {each_char}')
    
    for each_line in lines:
        name = each_line['name']
        line = each_line['line']
        print(f'character: {name}, line: {line}')

        val = input('please input character: ')
        if val == 's':
            continue

        if val.isdigit():
            each_line['name'] = character_table[int(val)]



def main():
    character_table = ['unk', 'chino', 'kokoa', 'rize', 'teitsupi', 'takahiro', 'chiya', 'sharo']
    lines = read_data('data/zh-CHT/full_data.json')
    mark_characters(lines, character_table)
    write_data('data/zh-CHT/full_data_new.json', lines)

if __name__ == "__main__":
    main()