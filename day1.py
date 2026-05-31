import cv2
import matplotlib.pyplot as plt
image=cv2.imread("image.jpg")
print(image.shape)
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.imshow(image)
plt.show()