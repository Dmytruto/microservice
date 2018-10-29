import os
import face_recognition
import pickle
faces = os.listdir('./faces')
known_face_encodings = []
known_face_names = []

for face in faces:
    name  = face.split(".")[0]
    print(name)
    print(face)
    load_face = face_recognition.load_image_file('./faces/' + face)
    face_point = face_recognition.face_encodings(load_face)[0]
    known_face_encodings.append(face_point)
    known_face_names.append(name)
    
named_point = zip(known_face_names,known_face_encodings)
f = open('store.pckl', 'wb')
pickle.dump(named_point, f)
f.close()