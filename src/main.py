import cv2
from pyzbar.pyzbar import decode

# 读取图像
image = cv2.imread('test.png')

# 解码二维码
decoded_objects = decode(image)

# 输出解码结果
for obj in decoded_objects:
    print(f'Decoded Data: {obj.data.decode("utf-8")}')
    print(f'Type: {obj.type}')