import face_recognition

image = face_recognition.load_image_file('team1.jpg')
face_locations = face_recognition.face_locations(image)

#Array of cordinates of face locations
#print(face_locations)

print(f'there are {len(face_locations)} people in this image')