#火车站，进站验票一样
import cv2
import os
import numpy as np
def take_face():
    cap = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
    isCreate = True
    num = 1
    while True:
        if num == 6:
            num =1
            isCreate = True
        f, frame = cap.read()
        faces = face_detector.detectMultiScale(frame,scaleFactor = 1.3,minNeighbors = 5)
        if isCreate and (num == 1):
            file = input('name(N,quit):')
            os.makedirs('./face/%s' % (file), exist_ok=True)
            isCreate = False
        for x, y, w, h in faces[:1]:
            target = frame[y + 2:y + h - 1, x + 2:x + w - 1]
            cv2.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=[0, 0, 255], thickness=2)
        cv2.imshow('face', frame)
        key = cv2.waitKey(42)
        if ord('w') == key:
            # 保存图片
            cv2.imshow('face', target)
            cv2.waitKey(42)
            cv2.imwrite('./face/%s/%d.jpg' % (file,num),
                        cv2.resize(target,(64,64),interpolation=cv2.INTER_LINEAR))
            num +=1
            print('图片保存成功！')
        elif ord('q') == key:
            break
    cap.release()
    cv2.destroyAllWindows()
# Alt + Enter,帮助我们创建方法
def load_faces():
    labels = os.listdir('./face')
    # 列表生成式获取人脸数据
    # X = np.asarray([cv2.cvtColor(cv2.imread('./faces/%s/1.jpg'%(i),code = cv2.COLOR_BGR2GRAY))
    #                 for i in labels])
    X = []
    y = []
    for i,l in enumerate(labels):
        for j in range(1,6):
            face = cv2.imread('./face/%s/%d.jpg'%(l,j))
            face = cv2.cvtColor(face,code=cv2.COLOR_BGR2GRAY)
            X.append(face)
            y.append(i)
    X = np.asarray(X)
    y = np.asarray(y)
    return X,y,labels
def recognize_static_face():
    X, y, labels = load_faces()
    face_recognizer = cv2.face.LBPHFaceRecognizer_create(radius = 1,neighbors = 3,threshold = 30)
    face_recognizer.train(X[::5],y[::5])
    print(X.shape)
    for face in X:
        cv2.imshow('face',face)
        x,y = face.shape
        result = face_recognizer.predict(face)
        print('这个是： ',labels[result[0]])
        print('可信度(值越小越可信)：',result)
        cv2.waitKey(2000)
    cv2.destroyAllWindows()


def recognize_dynamic_face():
    X,y,labels = load_faces()
    # Eigen特征，数学运算（卷积抽取特征）---> 128个特征值
    # 对比，欧式距离，越大，越远越不相似，越小越近，越相似
    # face_recognizer = cv2.face.EigenFaceRecognizer_create()
    # face_recognizer = cv2.face.FisherFaceRecognizer_create()
    face_recognizer = cv2.face.LBPHFaceRecognizer_create(radius = 3,neighbors = 8,threshold = 200)
    face_recognizer.train(X,y)
    cap = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
    while True:
        f,frame = cap.read()
        gray = cv2.cvtColor(frame,code=cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray)
        try:
            for x,y,w,h in faces:
                cv2.rectangle(frame,pt1 = (x,y),pt2 = (x+w,y+h),color=[0,0,255],thickness=2)
                gray = gray[y:y+h,x:x+w]
                gray = cv2.resize(gray,(64,64),interpolation=cv2.INTER_LINEAR)
                result = face_recognizer.predict(gray)
                if result[0] == -1:

                    cv2.putText(frame, '', (x, y - 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, [0,0,255], 2)
                else:
                    cv2.putText(frame, labels[result[0]], (x, y - 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, [0,0,255], 2)
                    print('可信度(越小越可信)：',result[1])
        except:
            pass
        cv2.imshow('face',frame)
        if ord('q') == cv2.waitKey(42):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # take_face()#人脸采集
    # recognize_static_face()#人脸静态识别
    recognize_dynamic_face()# 人脸动态识别