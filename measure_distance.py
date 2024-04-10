import imgsim
import cv2

vtr = imgsim.Vectorizer()
# slide of title and book
blue = cv2.imread("./input/blue.png")
blue_vac = vtr.vectorize(blue)
# talk questioner
pink = cv2.imread("./input/pink.png")
pink_vac = vtr.vectorize(pink)

for x in range(1475):
  another_img = cv2.imread("./HyVM0zMvVFc/output%04d.png" %(x + 1))
  another_vac = vtr.vectorize(another_img)
  blue_res = imgsim.distance(blue_vac, another_vac)
  if blue_res < 17:
    print(x + 1, "sec =", round(blue_res, 2))
    continue
  pink_res = imgsim.distance(pink_vac, another_vac)
  if pink_res < 16:
    print(x + 1, "sec =", round(pink_res, 2))
    continue
