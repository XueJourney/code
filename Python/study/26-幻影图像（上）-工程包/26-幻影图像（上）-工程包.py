"""幻影图像"""
from PIL import Image
# 定义main函数,函数函数接收两张图片,并将彩色图片转换为黑白(L)
def main(img1, img2):
    img1_ = Image.open(img1).convert("L")
    img2_ = Image.open(img2).convert("L")
    # 将img_图片调整为img_的尺寸
    img1_ = img1_.resize(img2_.size)
    # img1_.show()
    # img2_.show()
    # 使用point()方法,优化两张图片
    img1_ = img1_.point(changeL)
    img2_ = img2_.point(changeD)
    # 调用first函数,实现照片合成
    first(img1_, img2_).save("./img/result.jpg")

# 定义函数changeL,将像素值变为原先的1.1倍
def changeL(img):
    return img * 1.1

# 定义函数changeD,将像素值变为原先的1.1倍
def changeD(img):
    return img * 1.1

# 定义函数first,实现照片合成,传入两个参数--imga和imgb,分别代表两张照片
def first(imga, imgb):
    img1 = imga.load()
    img2 = imgb.load()
    # 获取图片的宽和高
    width, height = imga.size
    # 创建一个新图片
    for i in range(width):
        for j in range(height):
            a = img1[i, j]
            b = img2[i, j]
            # 公式进行合成每个像素点
            color = 255-a+b
            if color > 200:
                img1[i,j] = 160 - a + b
            else:
                img1[i,j] = color
    return imga

# 调用main函数
if "__main__" == __name__:
    main("./img/1.png", "./img/2.png")