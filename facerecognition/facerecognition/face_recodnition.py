import face_recognition
import cv2
import pickle

f = open('store.pckl', 'rb')
namedEncoding = pickle.load(f)
f.close()
known_face_names, known_face_encodings = zip(*namedEncoding)
cap = cv2.VideoCapture(0)
if not cap.isOpened():

    raise IOError("Cannot open webcam")
while True:

    ret, frame = cap.read()
    face_names = []
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, known_face_locations= face_locations)

    for face_encode in face_encodings:

        matches = face_recognition.compare_faces(known_face_encodings, face_encode)
        name = "Unknown"
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        face_names.append(name)

    for face_location, name in zip(face_locations, face_names):

            top, right, bottom, left = face_location
            name_color = (0, 0, 255) if (name == "Unknown")  else (0, 255, 0)
            cv2.rectangle(frame, (left, top), (right, bottom), name_color, 2)
            cv2.putText(frame, name, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), lineType=cv2.LINE_AA)

    cv2.imshow('Face Cropper', frame)
    if cv2.waitKey(1) == 13:  # 13 is the Enter Key
        break