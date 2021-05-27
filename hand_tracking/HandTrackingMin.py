import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
    # openCV에서 활용할 나의 카메라 지정

mpHands = mp.solutions.hands
    # mediapipe의 솔루션인 hands를 불러온다.
hands = mpHands.Hands()
    # hands라는 이름으로 인스턴스 생성.
mpDraw = mp.solutions.drawing_utils
    # 화면에 시각화하기 위한 도구 불러오기.

pTime = 0
cTime = 0
    # FPS를 표기 할 때 활용할 시간 변수 초기화

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # openCV에서는 RGB가 아닌 BGR 순서로 색상을 표시한다. 왜죠..?
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # id는 랜드마크의 인덱스, lm은 이미지(영상)의 좌상단을 기준으로 상대위치(0~1)이다.
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                # 위치를 픽셀 단위로 알기위해 영상의 폭, 높이와 곱해준다. 
                # 생략한다면 위치가 소수점으로 나와서 보기도 안좋다.
                print(id, cx, cy)
                if id in [0, 4, 8,12,16,20]:
                    # 나는 기준으로 손목(0)과 각 손가락의 끝을 잡았다.
                    cv2.circle(img, (cx,cy), 15, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    # 영상의 FPS를 표기하기 위한 작업. 난 이것도 신기했다. 
    # 이전에 pygame에서는 그냥 함수로 불러내기만 했지 어떻게 만드는지는 몰랐는데 이렇게 또 배우네.

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 255), 3)
    # 위에서 계산한 FPS를 영상 좌상단 (10, 70) 지점에 표기.

    cv2.imshow('Image', img)
    cv2.waitKey(1)
    # 그냥 단순히 키입력을 기다리는 코드인 줄 알았는데 꽤나 중요한 친구더라.
    # 없으면 커널에서 충돌이 난다는건지..? 정확한 개념을 아직은 모르겠다. 

    