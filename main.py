import subprocess
import cv2
import os
from tkinter import *
from classify_webcam import detect_sign
from classify_webcam import prediction_output


def train_model():
    subprocess.call("./train.sh",shell=True)
    print("Model Trained")


def create_sign_images(sign_name):
    if os.path.isdir("./dataset/"+sign_name) == False:
        os.mkdir("./dataset/"+sign_name)
    c = 0
    cap = cv2.VideoCapture(0)
    res, score = '', 0.0
    counter = 0
    mem = ''
    consecutive = 0
    sequence = ''
    i = 0
    while True:
        ret, img = cap.read()
        img = cv2.flip(img, 1)
        i = i+1
        if ret:
            x1, y1, x2, y2 = 300, 100, 500, 300
            img_cropped = img[y1:y2, x1:x2]
            image_data = cv2.imencode('.jpg', img_cropped)[1].tostring()
            a = cv2.waitKey(1)  # waits to see if `esc` is pressed
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.imshow("img", img)
            if i > 50 and i < 150:
                if i%10==0:
                    print("Image Captured:",i)
                cv2.imwrite("./dataset/" + sign_name + "/" + str(i) + ".jpg", img_cropped)
            elif i >= 150:
                cv2.destroyAllWindows()
                return


def init_gui(main_window_object):
    main_window_object.title('India Sign Language')
    # main_window_object.geometry("500x500")
    main_window_object.resizable(0, 0)

    label = Label(main_window_object, text="Text label:")
    label.grid(row=0, column=0)
    # label.pack()

    enter_label = Entry(main_window_object, bd=5)
    enter_label.grid(row=0, column=1)
    # enter_label.pack()

    add_sign_button = Button(main_window_object, text="Add Sign", command=lambda: create_sign_images(enter_label.get()))
    add_sign_button.grid(row=1, column=0)
    # add_sign_button.pack()
    train_button = Button(main_window_object, text="Train(after dataset creation)", command=train_model)
    train_button.grid(row=1, column=1)

    detect_button = Button(main_window_object, text="Detect", command=detect_sign)
    detect_button.grid(row=2, column=0)

    exit_button = Button(main_window_object, text="Exit", command=lambda: exit())
    exit_button.grid(row=2, column=1)



def main():
    main_window_object = Tk()
    init_gui(main_window_object)
    main_window_object.mainloop()


if __name__ == "__main__":
    main()
