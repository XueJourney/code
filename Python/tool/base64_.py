import base64

def image_to_base64(image_path):
    """
    将图像转换为base64字符串。

    参数:
    image_path (str): 图像文件的路径。

    返回:
    str: 图像的base64编码字符串。
    """
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

# Example usage:
encoded_image = image_to_base64("D:/work/加密/wzh/wzh_计算/20221204-145242/Image1.png")
# print(encoded_image)
# open("./res.txt", "w").write(encoded_image)

