from ultralytics import YOLO
import cvzone
import cv2
import math


# cap = cv2.VideoCapture("fire.mp4")
# model = YOLO("fire_model.pt")

# # Reading the classes
# classnames = ["fire"]

# while True:
#     frame = cv2.imread(image_path)

image_path = "./fire (1347).png"
img = cv2.imread(image_path)
# cap = cv2.VideoCapture()
model = YOLO("fire_model.pt")

# Reading the classes
classnames = ["fire"]

while True:
    # ret, frame = cap.read(img)
    # print(frame)
    # print(img)
    frame = cv2.resize(img, (640, 480))
    result = model(frame, stream=True)

    # Getting bbox,confidence and class names information to work with
    for info in result:
        boxes = info.boxes
        for box in boxes:
            confidence = box.conf[0]
            confidence = math.ceil(confidence * 100)
            Class = int(box.cls[0])
            if confidence > 50:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
                cvzone.putTextRect(
                    frame,
                    f"{classnames[Class]} {confidence}%",
                    [x1 + 8, y1 + 100],
                    scale=1.5,
                    thickness=2,
                )

    cv2.imshow("frame", frame)
    cv2.waitKey(900)
