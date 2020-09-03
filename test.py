from get_argument import getArgument
import cv2
import numpy as np

#lấy được đối tượng arg từ hàm getArgument()
arg = getArgument()

# đọc được ảnh từ đường dẫn
img = cv2.imread(arg.image_path)

# Chuyển đổi sang ảnh gray
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.resize(img, (32,32), interpolation = cv2.INTER_LINEAR)

print(img)
cv2.imshow('Image',img)
# Chuyển sang ảnh nhị phân nhờ 2 ngưỡng threshold này - nếu trong khoảng thì chuyển về 255 , ngoài khoảng thì chuyển về 0
#đúng kiểu ảnh nhị phân
_, img = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
print("============================================")
print(img)
cv2.imshow('Image 2 ',img)

cv2.waitKey(0)
cv2.destroyAllWindows()