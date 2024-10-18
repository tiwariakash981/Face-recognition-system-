import face_recognition 
import cv2
import numpy as np
import csv 
import os
from datetime import datetime 

video_capture = cv2.VideoCapture()

akash_img = face_recognition.load_image_file("C:\AKASH\Projects\Face Recognition\akash.png")
akash_encoding = face_recognition.face_encoding(akash_img)

ajay_img = face_recognition.load_image_file("C:\AKASH\Projects\Face Recognition\ajay.png")
ajay_encoding = face_recognition.face_encoding(ajay_img)

known_faces_names = [ajay_img,akash_img]
known_faces_encoding = [akash_encoding,ajay_encoding]

students = known_faces_names.copy()

face_locations =[]
face_encodings = []
face_names = []
 
s = True

while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]

    if s:
        face_locations = face_recgnition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names = []

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
            name = ''
            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
            mini = np.argmin(face_distance)

            if matches[mini]:
                name = known_faces_names[mini]

            face_names.append(name)
            if name in known_faces_names:
                students.remove(name)
                print(students)
                current_time = now.strftime('%H-%M-%S')
                lnwriter.writerow([name,current_time])
    cv2.imshow('attendance_system',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroAllWindows()
f.close()




