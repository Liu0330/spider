from PIL import Image

image = Image.open('a.jpg')

'''选择图片'''
width, height = image.size

#  高和宽进行比较，较大的为新图片的长度
# new_length = height if height > width else width
new_length = max(height,width)

# 创建一张正方形空图片，底色为白色,
new_image = Image.new(image.mode, (new_length, new_length), color='white')

# 将要处理的图片粘贴到新创建的图片上，居中
if height > width:  # 如果高度大于宽，则填充图片的宽度
    new_image.paste(image, (int((new_length - width) / 2)), 0)
else:
    new_image.paste(image, (0, int((new_length - height) / 2)))

# 朋友圈一排三张图片因此宽度切割成3份
new_length = int(new_length / 3)
# 用来保存每一个切图
box_list = []
for i in range(0, 3):
    for j in range(0, 3):
        # 确定每个图片的位置
        box = (j * new_length, i * new_length, (j + 1) * new_length, (i + 1) * new_length)  # (left, top, right, bottom)
        box_list.append(box)
# 通过crop函数对图片进行切割
image_list = [new_image.crop(box) for box in box_list]

for (index, image) in enumerate(image_list):
    image.save(str(index) + '.png', 'PNG')
print("九宫格图片生成完毕！")