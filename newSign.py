import cv2

c = 0

cap = cv2.VideoCapture(0)

res, score = '', 0.0
counter = 0
mem = ''
consecutive = 0
sequence = ''
i=0
while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    i=i+1 
    if ret:
        
        x1, y1, x2, y2 = 300, 100, 500, 300
        img_cropped = img[y1:y2, x1:x2]
        image_data = cv2.imencode('.jpg', img_cropped)[1].tostring()
        a = cv2.waitKey(1) # waits to see if `esc` is pressed
        cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 2)
        cv2.imshow("img", img)
        if i>50 and i<150:
            print("captured")
            cv2.imwrite("./a/"+str(i)+".jpg",img_cropped)
        elif i>=150:
            exit()
