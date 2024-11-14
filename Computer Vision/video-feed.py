from ultralytics import YOLO
import cv2
import time

# Load the YOLOv8 model - using the pre-trained nano model
model = YOLO('yolov8n.pt')  # nano model is smallest and fastest


# Initialize camera
cap = cv2.VideoCapture(0)
if cap is None:
    print("Error: Could not access any camera")
    exit()

# Set a reasonable FPS target
fps = 30
delay = 1/fps

try:
    while True:
        start_time = time.time()
        
        # Capture frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
            
        # Run YOLOv8 inference on the frame
        results = model(frame, conf=0.5)  # confidence threshold 0.5
        
        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        
        # Display the annotated frame
        cv2.imshow('YOLOv8 Detection', annotated_frame)
        
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
        # Control FPS
        elapsed = time.time() - start_time
        if elapsed < delay:
            time.sleep(delay - elapsed)
            
finally:
    cap.release()
    cv2.destroyAllWindows()