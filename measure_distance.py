import imgsim
import cv2
import sys
import glob
import re

# get value from command line arg
video_id = sys.argv[1]

vtr = imgsim.Vectorizer()
# slide of title and book
blue = cv2.imread("./input/blue.png")
blue_vac = vtr.vectorize(blue)
# talk questioner
pink = cv2.imread("./input/pink.png")
pink_vac = vtr.vectorize(pink)

# output*.png all files
files = glob.glob(f'{video_id}/output*.png')
# Get a number from a file name and get the largest number
file_numbers = [int(re.search(r'(\d\d\d\d)', file).group()) for file in files]
max_number = max(file_numbers)

results = []
for x in range(max_number):
  another_img = cv2.imread(f"./{video_id}/output%04d.png" %(x + 1))
  another_vac = vtr.vectorize(another_img)
  blue_res = imgsim.distance(blue_vac, another_vac)
  if blue_res < 17:
    print(x, "sec =", round(blue_res, 2))
    results.append(x)
    continue
  pink_res = imgsim.distance(pink_vac, another_vac)
  if pink_res < 16:
    print(x, "sec =", round(pink_res, 2))
    results.append(x)
    continue

# In the case of continuous value of 1.
# [1, 2, 3, 5, 6, 7, 8, 10] -> [1, 5, 10]
temp = [results[0]]
previous = results[0]
for num in results[1:]:
  if previous != num - 1:
    temp.append(num)
  previous = num
results = temp

# sec to min and sec
results = [(x // 60, x % 60) for x in results]

# resultsの分秒を表示
for min, sec in results:
  print(f"{min}分 {sec}秒")
