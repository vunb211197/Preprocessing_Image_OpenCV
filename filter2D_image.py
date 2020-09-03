from get_argument import getArgument
import cv2
import numpy as np

#lấy được đối tượng arg từ hàm getArgument()
arg = getArgument()

# đọc được ảnh từ đường dẫn
img = cv2.imread(arg.image_path)
cv2.imshow('Orginal Image',img)


kernel = np.ones((5,5),np.float32)/25
imgSmooth = cv2.filter2D(img,-1,kernel)
cv2.imshow('Smooth Image',imgSmooth)

cv2.waitKey(0)
cv2.destroyAllWindows()