from blockchain import Blockchain
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

def main():
    chain1=Blockchain()
    chain2=Blockchain()
    
    candidate1=input('Enter first candidate name')
    candidate2=input('Enter second candidate name')
    cand1_votes=0
    cand2_votes=0
    voters_id=["SUNNY","ANTARIKA","DEBASMITA","BISWAJIT"]
    no_of_voters=len(voters_id)
    print('no of voters:',no_of_voters)
    voted=[]
    
    
    
    
    while True:
        if voters_id!=[]:
            name=camera_capture()
        if voters_id==[]:
            print('voting is over')
            if cand1_votes>cand2_votes:
                print(f"{candidate1} won the election with {cand1_votes}")
                print(f"AND THE VOTES FOR {candidate1} ARE:")
                chain1.print_blockchain()
            elif cand2_votes>cand1_votes:
                print(f"{candidate2} won the election with {cand2_votes}")
                print(f"AND THE VOTES FOR {candidate2} ARE:")
                chain2.print_blockchain()
            elif cand1_votes==cand2_votes:
                print('tied!!')
                chain1.print_blockchain()
                chain2.print_blockchain()
            break
        else:
            voter=input('Enter your Id:')
            
            if voter in voted:
                print('you already voted')
            else:
                if voter in voters_id and voter==name:
                    print(f"1.{candidate1}\n2.{candidate2}")
                    choice=int(input('Enter your choice'))
                    if choice==1:
                        chain1.add_block(voter)
                        cand1_votes+=1
                        print(f"you voted {candidate1}")
                    elif choice==2:
                        chain2.add_block(voter)
                        cand2_votes+=1
                        print(f"you voted {candidate2}")
                    voters_id.remove(voter)
                    voted.append(voter)
                else:
                    print('you are not allowed to vote')

def faceEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList                   

def camera_capture():
    path = 'c:/Users/sunny/Desktop/Exploring-the-Bitcoin-Cryptocurrency-Market-master/Exploring-the-Bitcoin-Cryptocurrency-Market-master/images'
    images = []
    
    personNames = []
    myList = os.listdir(path)
    #print(myList)
    for cu_img in myList: 
        current_Img = cv2.imread(f'{path}/{cu_img}')
        images.append(current_Img)
        personNames.append(os.path.splitext(cu_img)[0])
    #print(personNames)
    encodeListKnown = faceEncodings(images)
    #print(encodeListKnown)
    print('All Encodings Complete!!!')
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)
            
        facesCurrentFrame = face_recognition.face_locations(faces)
        encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)
        for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                
            matchIndex = np.argmin(faceDis)
                
            if matches[matchIndex]:
                name = personNames[matchIndex].upper()
                    
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) == 13:
            break
    return name    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
	main()