from get_argument import getArgument
import cv2

#lấy được đối tượng arg từ hàm getArgument()
arg = getArgument()

# đọc được ảnh từ đường dẫn
img = cv2.imread(arg.image_path)
rows, cols = img.shape[:2]
cv2.imshow('Orginal Image',img)


# Xoay ảnh kích thước 45 độ tại tâm của ảnh, độ phóng đại ảnh không đổi.
M5 = cv2.getRotationMatrix2D(center = (cols/2,rows/2), angle=-45, scale=1)
tran5 = cv2.warpAffine(img, M5, (cols,rows))
cv2.imshow('Tran5',tran5)
# Xoay ảnh kích thước 45 độ tại tâm của ảnh và độ phóng đại giảm 1/2
M6 = cv2.getRotationMatrix2D(center = (cols/2,rows/2), angle=-45, scale=0.5)
tran6 = cv2.warpAffine(img, M6, (cols,rows))
cv2.imshow('Tran6',tran6)
# Xoay ảnh kích thước -45 độ tại tâm của ảnh
M7 = cv2.getRotationMatrix2D(center = (cols/2,rows/2), angle=45, scale=1)
tran7 = cv2.warpAffine(img, M7, (cols,rows))
cv2.imshow('Tran6',tran7)
# Xoay ảnh kích thước 20 độ tại góc trên bên trái
M8 = cv2.getRotationMatrix2D(center = (0, 0), angle=-20, scale=1)
tran8 = cv2.warpAffine(img, M8, (cols,rows))
cv2.imshow('Tran8',tran8)
# Xoay ảnh kích thước 20 độ tại góc dưới bên phải
M9 = cv2.getRotationMatrix2D(center = (cols,rows), angle=-20, scale=1)
tran9 = cv2.warpAffine(img, M9, (cols,rows))
cv2.imshow('Tran9',tran9)

cv2.waitKey(0)
cv2.destroyAllWindows()