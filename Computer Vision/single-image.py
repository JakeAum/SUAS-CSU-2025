from ultralytics import YOLO
import cv2

# Load a pretrained YOLO model (recommended for training)
model = YOLO("yolov8n.pt")

# Path to your image
image_path = r"Computer Vision\test_images\katrina.jpg"

# Read the image
image = cv2.imread(image_path)

# Run inference
results = model(image)[0]  # [0] because predict returns a list of Results objects

# Process detections
print("\nDetections:")
print("-" * 50)

for box in results.boxes:
    # Get class id, confidence and bounding box coordinates
    class_id = results.names[box.cls.item()]
    confidence = round(box.conf.item(), 2)
    coords = [round(x) for x in box.xyxy.tolist()[0]]  # Convert to integer coordinates
    
    print(f"Object: {class_id}")
    print(f"Confidence: {confidence * 100}%")
    print(f"Bounding Box: {coords}")
    print("-" * 50)

# Display the image with detections
annotated_frame = results.plot()
cv2.imshow("YOLOv8 Detection", annotated_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()