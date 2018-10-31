import face_recognition
import os
import numpy as np


class FaceRecog:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        dirname = 'faceRecog/knowns'
        files = os.listdir(dirname)
        for filename in files:
            name, ext = os.path.splitext(filename)
            if ext == '.jpg':
                self.known_face_names.append(name)
                pathname = os.path.join(dirname, filename)
                img = face_recognition.load_image_file(pathname)
                face_encoding = face_recognition.face_encodings(img)[0]
                self.known_face_encodings.append(face_encoding)

        self.face_locations = []
        self.face_encodings = []
        self.face_names = []

    def getNames(self, _frame):
        frame = _frame
        rgb_frame = frame[:, :, ::-1]

        #self.face_locations에는 얼굴들의 위치가 담겨 있다. 즉, 두 명이 존재하면 두 명의 얼굴 위치가 있다.
        #self.face_encodings에는 얼굴들의 특징점이 추출된 배열이 있다.
        self.face_locations = face_recognition.face_locations(rgb_frame)
        self.face_encodings = face_recognition.face_encodings(rgb_frame, self.face_locations)
        self.face_names = []

        for face_encoding in self.face_encodings:
            '''
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            self.face_names.append(name)
            '''
            distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            min_value = min(distances)

            name = "Unknown"
            #실험적 수치가 필요
            if min_value < 0.48:
                index = np.argmin(distances)
                name = self.known_face_names[index]
            self.face_names.append(name)
        return self.face_names
        '''
        # Display the results
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            print(name)
        return frame
        '''
