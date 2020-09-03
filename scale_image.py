from get_argument import getArgument
import cv2

#lấy được đối tượng arg từ hàm getArgument()
arg = getArgument()

# đọc được ảnh từ đường dẫn
img = cv2.imread(arg.image_path)
cv2.imshow('Orginal Image',img)

# Scale image bằng cách gấp đôi width and height
h, w = img.shape[:2]
imgScale = cv2.resize(img, (int(w*2), int(h*2)), interpolation = cv2.INTER_LINEAR)
cv2.imshow('Scale Image',imgScale)
cv2.waitKey(0)
cv2.destroyAllWindows()
