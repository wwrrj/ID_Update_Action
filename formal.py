with open('./IDList/marble.txt', 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()

not_starting_with_0x0 = [line for line in lines if not line.startswith('0x0')]

with open('./IDList/marble.txt', 'w', encoding='utf-8') as output_file:
    output_file.writelines([line for line in lines if line.startswith('0x0')])

with open('./IDList/Stupid_People_ID.txt', 'w', encoding='utf-8') as output_file:
    output_file.writelines(not_starting_with_0x0)
