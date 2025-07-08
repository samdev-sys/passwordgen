import cv2


imgcapture= cv2.VideoCapture(0)
result= True


while(result):
    ret, frame= imgcapture.read()
    cv2.imwrite("prueba.jpg", frame)
    result= False
    print("imagen guardada...")

imgcapture.release()