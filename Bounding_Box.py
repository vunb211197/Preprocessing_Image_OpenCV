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

# Chuyển đổi sang ảnh gray
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Chuyển sang ảnh nhị phân
_, img = cv2.threshold(img, 250, 255, cv2.THRESH_BINARY)
#chuyển đen thành trắng , trắng thành đen
img=cv2.bitwise_not(img)

# # Lọc ảnh nhị phân bằng thuật toán canny
# img = cv2.Canny(img, 100, 200)

cv2.imshow('Binary_Image',img)

# Tìm kiếm contours trên ảnh nhị phân
contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print('vux',len(contours))
# Tìm ra diện tích của toàn bộ các contours
area_cnt = [cv2.contourArea(cnt) for cnt in contours]

# Vẽ bounding box cho tất cả các contour
for cnt in contours:
    print(len(cnt))
    #các đinh tọa độ x,y là điểm góc bắt đầu của hình chữ nhật, w,h là chiều dài chiều rộng hình chữ nhật
    x,y,w,h = cv2.boundingRect(cnt)
    #vẽ hình chữ nhật
    img = cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Bounding box',img)
    #tim hình chữ nhật có diện tích nhỏ nhất bao quanh contour
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    img = cv2.drawContours(img2,[box],0,(100,100,100),2)
    cv2.imshow('Bouding Min Box',img)

cv2.waitKey(0)
cv2.destroyAllWindows()