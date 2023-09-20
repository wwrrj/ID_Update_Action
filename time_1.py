import os
import datetime

# 获取当前北京时间
beijing_time = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
time_str = beijing_time.strftime("%Y%m%d_%H-%M")

# 源文件路径
source_dir = r"./IDList/"
marble_source_path = os.path.join(source_dir, "marble.txt")
munch_source_path = os.path.join(source_dir, "munch.txt")
ventar_source_patch = os.path.join(source_dir, "ventar.txt")


# 新文件名
marble_new_name = f"marble-Note12Tubro_{time_str}_IDList.txt"
munch_new_name = f"munch-K40s_{time_str}_IDList.txt"
ventar_new_name = f"ventar-Mi11_{time_str}_IDList.txt"

# 目标文件路径
marble_target_path = os.path.join(source_dir, marble_new_name)
munch_target_path = os.path.join(source_dir, munch_new_name)
ventar_target_path = os.path.join(source_dir, ventar_new_name)

# 重命名文件
os.rename(marble_source_path, marble_target_path)
os.rename(munch_source_path, munch_target_path)
os.rename(ventar_source_patch, ventar_target_path)
