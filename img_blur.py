from get_argument import getArgument
import cv2
import numpy as np

#lấy được đối tượng arg từ hàm getArgument()
arg = getArgument()

# đọc được ảnh từ đường dẫn
img = cv2.imread(arg.image_path)
cv2.imshow('Orginal Image',img)

blur_img = cv2.blur(img,(5,5))
cv2.imshow('Blur Image',blur_img)

blur_img_2=cv2.boxFilter(img,-1,(5,5))
cv2.imshow('Blue Image 2 ',blur_img_2)



#bộ lọc gaussian 
#hiệu quả trong việc xóa nhiễu hình ảnh
gaussian_img = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('Gaussain_image',gaussian_img)




#bộ lọc median ( như bộ lọc trung bình nhưng đây là tính median chứ ko phải mean)
median_img = cv2.medianBlur(img,5)
cv2.imshow('Median_image',median_img)
#bộ lọc bilateral: Được khởi tạo thông qua hàm cv2.bilateralFilter(). 
# Các bộ lọc trình bày trước đó cho thấy có xu hướng làm mờ cạnh. Tuy nhiên bộ lọc này lại chỉ remove nhiễu mà vẫn bảo tồn được các cạnh

bilateral_img = cv2.bilateralFilter(img,2,0,0)
cv2.imshow('Bilateral_image',bilateral_img)

cv2.waitKey(0)
cv2.destroyAllWindows()