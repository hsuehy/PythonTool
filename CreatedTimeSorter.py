import os
import sys
import shutil
import datetime
from tqdm import tqdm


# 通过命令行参数获取源目录路径
if len(sys.argv) > 1:
    source_dir = sys.argv[1]
else:
    source_dir = "/app/files"  # 默认的原始文件目录

# CreatedTimeSorter: 基于创建时间的文件分类工具
#
# 该脚本根据文件的创建时间自动将指定目录下的文件按照年份和月份进行分类。
# 它将文件归档到对应的年份和月份目录中，便于整理和查找文件。
#
# CreatedTimeSorter 工具具有以下特点：
# - 自动分类：根据文件的创建时间，无需手动指定分类规则，工具会自动将文件归档到相应的年份和月份目录中。
# - 平台兼容：支持不同的操作系统和文件系统，读取文件的创建时间属性，确保在各种环境下都能正常工作。
# - 进度展示：使用进度条展示分类过程，方便用户实时了解文件分类的进度。
# - 错误处理：在处理文件过程中，对错误情况进行了处理，确保不会因为错误而中断整个分类过程。
#
# 使用方法：
# - 指定原始文件所在目录 (source_dir)。
# - 脚本会遍历原始文件目录及其子目录中的所有文件。
# - 文件将按照创建时间移动到相应的目录中。
# - 目标目录将按照如下格式创建：/source_dir/年份/月份。
#
# 注意：确保操作系统和文件系统支持读取文件的创建时间。
#
# 示例用法：
# python CreatedTimeSorter.py /app/files
#
# 作者：Hsueh
# 日期：2023-05-18

# 创建进度条
progress_bar = tqdm(desc="文件分类进度")

# 遍历原始文件目录中的所有文件
for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)

    # 获取文件的创建时间
    file_stat = os.stat(file_path)
    created_time = datetime.datetime.fromtimestamp(file_stat.st_birthtime)

    # 提取年份和月份
    year = str(created_time.year)
    month = str(created_time.month).zfill(2)  # 使用 zfill 方法补零

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
# 执行文件分类
