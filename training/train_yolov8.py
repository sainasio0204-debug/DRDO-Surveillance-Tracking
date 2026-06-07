from ultralytics import YOLO

model = YOLO("yolov8l.pt")
model.train(
    data="dataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    name="yolov8l_custom",
    device=0 
)






