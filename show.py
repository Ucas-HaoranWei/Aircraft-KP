import os
import cv2

path_img = './images'
path_ann = './annotations'

filenames =  os.listdir(path_ann)

for filename in filenames:
    images = cv2.imread(os.path.join(path_img, filename.split('.')[0] + '.jpg'))
    with open(os.path.join(path_ann, filename), 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            points = lines[i].split(',')
            for j in range(0, len(points)):
                # print(points)
                cv2.circle(images, (int(float(points[0])), int(float(points[1]))), 5, (0, 255,0), 3)
                cv2.circle(images, (int(float(points[2])), int(float(points[3]))), 5, (0, 255,0), 3)
                cv2.circle(images, (int(float(points[4])), int(float(points[5]))), 5, (0, 255, 0), 3)
                cv2.circle(images, (int(float(points[6])), int(float(points[7]))), 5, (0, 255, 0), 3)
                cv2.circle(images, (int(float(points[8])), int(float(points[9]))), 5, (0, 255, 0), 3)
    cv2.imshow('show', images)
    cv2.imwrite('./show.jpg', images)
    cv2.waitKey(0)