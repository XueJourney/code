"""幻影图像"""
from PIL import Image
# 定义main函数,函数函数接收两张图片,并将彩色图片转换为黑白(L)
def main(img1, img2):
    img1_ = Image.open(img1).convert("L")
    img2_ = Image.open(img2).convert("L")
    # 将img_图片调整为img_的尺寸
    img1_ = img1_.resize(img2_.size)
    img1_.show()
    img2_.show()

# 调用main函数
if "__main__" == __name__:
    main("Python/study/26-幻影图像（上）-工程包//1.jpg", "Python/study/26-幻影图像（上）-工程包/img/2.jpg")