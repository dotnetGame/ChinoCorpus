import json
import re
import sys
import getopt
'''
{
    'source': '00-00',
    'start': '0:00:00.00',
    'end': '0:00:00.00',
    'name': 'unk',
    'text': ''
}
'''
def read_data(filename):
    ret = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        begin_record = False
        for each_line in lines:
            re_line = re.compile(r'Dialogue: (?P<marked>[01]),(?P<start>[0-9]:[0-9]{2}:[0-9]{2}.[0-9]{2}),(?P<end>[0-9]:[0-9]{2}:[0-9]{2}.[0-9]{2}),(?P<style>[0-9a-zA-Z*]+),(?P<name>[0-9a-zA-Z*]+),(?P<marginl>[0-9]{1,4}),(?P<marginr>[0-9]{1,4}),(?P<marginv>[0-9]{1,4}),(?P<effect>.*?),(?P<text>.+)')
            match = re_line.match(each_line.strip())
            if match:
                if begin_record:
                    ret.append({
                        'source': '01-01',
                        'start': match.group('start'),
                        'end': match.group('end'),
                        'name': 'unk',
                        'text': match.group('text')
                    })
                if match.group('text') == '----------TXT----------':
                    begin_record = True
    return ret

def write_data(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for each_line in lines:
            f.write(json.dumps(each_line, ensure_ascii=False) + '\n')



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

    lines = read_data(input_path)
    write_data(output_path, lines)

if __name__ == "__main__":
    main(sys.argv)