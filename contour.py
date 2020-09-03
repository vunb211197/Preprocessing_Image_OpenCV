from get_argument import getArgument
import cv2
import numpy as np

#lấy được đối tượng arg từ hàm getArgument()
arg = getArgument()

# đọc được ảnh từ đường dẫn
img = cv2.imread(arg.image_path)

imgOrigin = img.copy()
img1 = img.copy()
img2 = img.copy()


cv2.imshow('Orginal Image',img)

# Lọc ảnh nhị phân bằng thuật toán canny
imgCanny = cv2.Canny(img, 100, 200)
cv2.imshow('Binary_Canny Image',imgCanny)



contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

print(cv2.contourArea(contours[12]))

# contours trả về 1 list các contour .Mỗi contour là một mảng các tọa độ [x,y] của các điểm biên trong đối tượng

#vẽ các contour đó trên ảnh gốc

# Vẽ toàn bộ contours trên hình ảnh gốc
c1=cv2.drawContours(img1, contours, -1, (0, 255, 0), 3)
cv2.imshow('C1',c1)
# Vẽ chỉ contour thứ 12 trên hình ảnh gốc
c2=cv2.drawContours(img2, contours, 12, (0, 255, 0), 3)
cv2.imshow('C2',c2)


#vẽ bounding box là một đường biên đóng bao quanh vật thể ,có thể có nhiều hình dạng nhau 
#một bouding box có thể được xác định thông qua một contour


cv2.waitKey(0)
cv2.destroyAllWindows()