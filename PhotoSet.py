import os
import shutil
import re
import sys
from tqdm import tqdm

def PhotoSet(source_dir):
    """
    TimeSorter: 文件按时间分类工具

    该脚本根据文件名中的日期信息，将指定目录下的文件按照年份和月份进行分类。
    它会创建对应的年份和月份目录，并将文件移动到相应的目录中，以便更好地组织和查找文件。

    参数:
        source_dir (str): 原始文件所在目录路径

    使用示例:
        python timesorter.py /app/files

    """

    # 定义匹配日期的正则表达式
    date_pattern = r"(\d{4})(\d{2})\d{2}"

    # 创建进度条
    progress_bar = tqdm(desc="文件分类进度")

    # 遍历原始文件目录中的所有文件
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        # 提取文件名中的年份和月份
        match = re.search(date_pattern, filename)
        if match:
            year = match.group(1)
            month = match.group(2)

            # 创建目标目录（如果不存在）
            target_dir = os.path.join(source_dir, year, month)
            os.makedirs(target_dir, exist_ok=True)

            # 移动文件到目标目录
            shutil.move(file_path, target_dir)

        # 更新进度条
        progress_bar.update(1)

    # 关闭进度条
    progress_bar.close()

    print("文件分类完成！")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        source_dir = sys.argv[1]
    else:
        source_dir = "/app/files"  # 默认的原始文件目录

    PhotoSet(source_dir)
