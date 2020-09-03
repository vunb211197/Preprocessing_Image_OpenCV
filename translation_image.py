import cv2
from get_argument import getArgument
import numpy as np 

#lấy được đối tượng arg từ hàm getArgument()
arg = getArgument()

# đọc được ảnh từ đường dẫn
img = cv2.imread(arg.image_path)
rows, cols = img.shape[:2]
cv2.imshow('Orginal Image',img)
# thử các trường hợp dịch chuyển ảnh
tx, ty = (200, 200)
M1 = np.array([[1, 0, tx], [0, 1, ty]], dtype=np.float32)
tran1 = cv2.warpAffine(img, M1, (cols, rows))
cv2.imshow('Tran1',tran1)

# Dịch chuyển hình ảnh xuống góc dưới bên trái
M2 = np.array([[1, 0, -tx], [0, 1, ty]], dtype=np.float32)
tran2 = cv2.warpAffine(img, M2, (cols, rows))
cv2.imshow('Tran2',tran2)

# Dịch chuyển hình ảnh xuống góc dưới bên trái
M3 = np.array([[1, 0, tx], [0, 1, -ty]], dtype=np.float32)
tran3 = cv2.warpAffine(img, M3, (cols, rows))
cv2.imshow('Tran3',tran3)

# Dịch chuyển hình ảnh xuống góc dưới bên trái
M4 = np.array([[1, 0, -tx], [0, 1, -ty]], dtype=np.float32)
tran4 = cv2.warpAffine(img, M4, (cols, rows))
cv2.imshow('Tran4',tran4)

cv2.waitKey(0)
cv2.destroyAllWindows()