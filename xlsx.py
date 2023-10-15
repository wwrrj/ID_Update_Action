import openpyxl
import os

# 查找文件
directory_path = 'D:/temp'
txt_files = [filename for filename in os.listdir(directory_path) if filename.endswith('.xlsx') and ('12T' in filename or 'K40s' in filename or 'MI 11' in filename or 'Y70' in filename or '855' in filename)]

# 遍历符合条件的xlsx文件
for file_name in txt_files:
    file_path = os.path.join(directory_path, file_name)

    # 打开Excel文件
    workbook = openpyxl.load_workbook(file_path)

    # 选择要读取的工作表
    sheet = workbook.active  # 使用默认的工作表

    # 定义一个列表来存储主板ID数据
    mainboard_ids = []

    # 遍历Excel中的每一行，从第7列开始（跳过前6列）
    for row in sheet.iter_rows(min_row=2, values_only=True):
        cell_value = str(row[9])  # 假设ID在第7列
        # 检查ID不为空并不是设备序列号
        if cell_value and not cell_value.startswith("设备序列号"):
            mainboard_ids.append(cell_value)

    # 关闭Excel文件
    workbook.close()

    # 确定输出文件名
    if '12T' in file_name:
        output_file_name = 'marble.txt'
    elif 'K40s' in file_name:
        output_file_name = 'munch.txt'
    elif 'MI 11' in file_name:
        output_file_name = 'ventar.txt'
    elif '855' in file_name:
        output_file_name = 'sm8150.txt' 
    elif 'Y70' in file_name:
        output_file_name = 'halo.txt'
    else:
        # 如果文件名不包含关键词，默认使用generic.txt
        output_file_name = 'generic.txt'

    # 将主板ID写入对应的txt文件，设置编码为UTF-8
    output_dir = './IDList'
    os.makedirs(output_dir, exist_ok=True)  # 创建输出目录，如果不存在
    output_file_path = os.path.join(output_dir, output_file_name)
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for id_value in mainboard_ids:
            file.write(id_value + '\n')
