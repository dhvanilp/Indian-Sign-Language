import tensorflow as tf
import sys
import os
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import copy
import cv2
# Disable tensorflow compilation warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

prediction_output=[]

def predict(image_data, label_lines,softmax_tensor,sess):
    predictions = sess.run(softmax_tensor,
                           {'DecodeJpeg/contents:0': image_data})

    # Sort to show labels of first prediction in order of confidence
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

    max_score = 0.0
    res = ''
    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        if score > max_score:
            max_score = score
            res = human_string
    return res, max_score

def detect_sign():
    label_lines = [line.rstrip() for line
                   in tf.gfile.GFile("logs/trained_labels.txt")]
    with tf.gfile.FastGFile("logs/trained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        c = 0

        cap = cv2.VideoCapture(0)

        res, score = '', 0.0
        counter = 0
        mem = ''
        consecutive = 0
        sequence = ''

        while True:
            ret, img = cap.read()
            img = cv2.flip(img, 1)
            # img = cv2.flip(img, 0)
            if ret:
                x1, y1, x2, y2 = 300, 100, 500, 300
                img_cropped = img[y1:y2, x1:x2]
                image_data = cv2.imencode('.jpg', img_cropped)[1].tostring()
                a = cv2.waitKey(1)  # waits to see if `esc` is pressed

                # if counter == 8:
                res, score = predict(image_data,label_lines,softmax_tensor,sess)

                print("This is the result: ", res.upper(), float(score))
                # cv2.putText(img, '%s' % (res.upper()), (100,400), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 4)
                # cv2.putText(img, '(score = %.5f)' % (float(score)), (100,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
                mem = res
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.imshow("img", img)
                # img_sequence = np.zeros((200,1200,3), np.uint8)
                # cv2.putText(img_sequence, '%s' % (sequence.upper()), (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
                # cv2.imshow('sequence', img_sequence)

                if a == 27:  # when `esc` is pressed
                    break

    # Following line should... <-- This should work fine now
    cv2.destroyAllWindows()
    cv2.VideoCapture(0).release()

detect_sign()