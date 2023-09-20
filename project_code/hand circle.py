import mediapipe as mp
import cv2

handModel=mp.solutions.hands
handModelDrawing=mp.solutions.drawing_utils
webcam=cv2.VideoCapture(0)

with handModel.Hands(min_detection_confidence=0.6,min_tracking_confidence=0.6) as hands:
    while True:
        control,frame=webcam.read()
        rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        result=hands.process(rgb)
        imageH, imageW, _ = frame.shape
        cv2.rectangle(frame, (250, 150), (500, 250), (0, 255, 0), 3)

        if result.multi_hand_landmarks:
            for handLandmark in result.multi_hand_landmarks:
                indexFinger_point = handLandmark.landmark[8 ]
                x = int(indexFinger_point.x*imageW)
                y = int(indexFinger_point.y*imageH)
                cv2.circle(frame, (x, y), 4, (0, 255, 0), 6)
                if 250<x<500 and 150<y<250:
                    cv2.rectangle(frame, (250, 150), (500, 250), (0, 255, 0), -1)
                    cv2.putText(frame, "Button Was Pressed!", (50, 50), cv2.FONT_ITALIC, 2, (255, 0, 0), 2)

        cv2.imshow("Button Pressed Test",frame)
        #if cv2.waitKey(10)==27:
         #   break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break