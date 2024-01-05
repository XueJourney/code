import os
import json

def read_and_classify_log_files(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.log')]
    consistent = []
    inconsistent = []

    for file in files:
        filepath = os.path.join(directory, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    # 解析日志行
                    parts = line.strip().split('] ')
                    data = parts[1]
                    # 提取Response部分
                    response = json.loads(data.split('Response: ')[1])

                    # 根据description分类
                    if response['result']['description'] == '一致':
                        consistent.append(response)
                    else:
                        inconsistent.append(response)
                except Exception as e:
                    print(f"Error processing line: {line}. Error: {e}")
    
    return consistent, inconsistent

# 使用示例
directory = './log/idcard'
consistent, inconsistent = read_and_classify_log_files(directory)

# 输出分类后的结果
print("一致的结果:")
print_list_name = []
for res in consistent:
    # print(res)
    if(not(res["result"]["name"] in print_list_name)):
        print(res["result"]["name"],":",res["result"]["idcard"])
        print_list_name.append(res["result"]["name"])

print("\n不一致的结果:")
print_list_name = []
for res in inconsistent:
    # print(res)
    if(not(res["result"]["name"] in print_list_name)):
        print(res["result"]["name"],":",res["result"]["idcard"])
        print_list_name.append(res["result"]["name"])