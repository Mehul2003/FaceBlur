import cv2
import random

face_cascade = cv2.CascadeClassifier('../opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../opencv-master/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
smile_cascade = cv2.CascadeClassifier('../opencv-master/data/haarcascades/haarcascade_smile.xml')


def blur(image, x_val, y_val, width, height):
    blur_factor = 20
    r_min = int(y_val/blur_factor)
    c_min = int(x_val/blur_factor)
    r_max = int((y_val+height)/blur_factor)
    c_max = int((x_val+width)/blur_factor)
    for row in range(r_min, r_max):
        for col in range(c_min, c_max):
            r_avg,b_avg,g_avg = scramble(image, row*blur_factor, col*blur_factor, blur_factor, blur_factor)
            for y in range(row*blur_factor, (row+1)*blur_factor):
                for x in range(col*blur_factor, (col+1)*blur_factor):
                    image[y][x] = (r_avg,b_avg,g_avg)
    return image

def average(image, row, col, h, w):
    r_tot = 0
    b_tot = 0
    g_tot = 0
    total = w*h
    for i in range(row, row+h):
        for j in range(col,col+w):
            r,g,b = image[i][j]
            r_tot += r
            g_tot += g
            b_tot += b
    return (int(r_tot/total),int(g_tot/total),int(b_tot/total))

def scramble(image, row, col, h, w):
    rand_row = random.randint(row, row+h)
    rand_col = random.randint(col, col+w)
    return image[rand_row][rand_col]

def detect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        image = blur(frame, x, y, w, h)


    return image

# cap = cv2.VideoCapture(0)
while(True):
    # ret, frame = cap.read()
    # frame = cv2.flip(frame, 1)
    frame = cv2.imread('assets/1.png', cv2.IMREAD_COLOR);

    frame = detect(frame)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
