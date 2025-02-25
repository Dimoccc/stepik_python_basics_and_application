import os
import re
arr = []
for corrent_dir, dirs, files in os.walk('main'):
    # print(corrent_dir, dirs, files)
    for a in files:
        if a[-3:] == '.py':
            arr.append(corrent_dir)
            # print('dirs',corrent_dir, arr)

arr = list(set(arr))
arr.sort()
with open("2.4-2-out.txt", "w") as out_file:
    out = '\n'.join(arr)
    out_file.write(out)


# import os
# import re

# # p - текущий каталог
# # d - список каталогов
# # f - список файлов
# arr = []
# for (p, d, f) in os.walk("main"):
#     for cur_file in f:
#         if re.search(r"\.py", cur_file) != None:
#             arr.append(p)

# arr = list(set(arr))
# arr.sort()
# with open("2.4-main.txt", "w") as file_out:
#     for dir_line in arr:
#         file_out.write(dir_line + "\n")

# import os

# for cur_dir, subdirs, files in os.walk("main"):
#     for file in files:
#         if file.endswith(".py"):
#             print(cur_dir)
#             break