import cv2
import os

dataPath = "/home/pi/Desktop/Rostros/Reconocimiento Facial/Datos" #Ruta en donde vamos a guardar las listas de los datos
imagePaths = os.listdir(dataPath)
print('imagePaths=',imagePaths)

#face_recognizer = cv2.face.EigenFaceRecognizer_create()
#face_recognizer = cv2.face.FisherFaceRecognizer_create()
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Leyendo el modelo
#face_recognizer.read('modeloEigenFace.xml')
#face_recognizer.read('modeloFisherFace.xml')
face_recognizer.read('modeloLBPHFace.xml')

cap = cv2.VideoCapture(0)#Entrarda de Video en timepo real
#cap = cv2.VideoCapture('Imagenes y videos de Prueba/salvador.mp4')#videos de prueba
#cap = cv2.VideoCapture('Imagenes y videos de Prueba/marisol.mp4')
#cap = cv2.VideoCapture('Imagenes y videos de Prueba/marisol2.mp4')
#cap = cv2.VideoCapture('Imagenes y videos de Prueba/yuuki2.mp4')


faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:
    ret,frame = cap.read()
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()
    
    faces = faceClassif.detectMultiScale(gray,1.3,5)
    
    for (x,y,w,h) in faces:
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)
        
        cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)

        # FigenFaces
#   if result[1] < 1000:
    #   cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
     #  cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
  # else:
         #   cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
          #  cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        
        #FisherFaces
  #  if result[1] < 100:
   #     cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
    #    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
    #else:
    #    cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
       # cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        
        
        # LBPHFace
    if result[1] < 70:
        cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
    else:
        cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
           
    cv2.imshow('frame',frame)
    k = cv2.waitKey(1)
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
