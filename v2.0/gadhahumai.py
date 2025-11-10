import torch
import numpy as np
import cv2
from time import time
from ultralytics import YOLO
import Alert
import Tampered

class MugDetection:

    pic = -2

    def __init__(self, capture_index, model_name):
        self.capture_index = capture_index
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("Using Device:", self.device)
        self.model = self.load_model(model_name)

    def get_video_capture(self):
        """Initialize webcam/video feed"""
        cap = cv2.VideoCapture(self.capture_index)
        if not cap.isOpened():
            raise RuntimeError("[ERROR] Could not open camera.")
        return cap

    def load_model(self, model_name):
        """Load YOLOv8 model"""
        if model_name:
            model = YOLO(model_name)
        else:
            model = YOLO("yolov8n.pt")  # fallback pretrained model
        model.to(self.device)
        print(f"[INFO] Model '{model_name}' loaded successfully on {self.device}.")
        return model

    def score_frame(self, frame):
        """Run inference on a frame using YOLOv8"""
        results = self.model(frame, stream=False, device=self.device,verbose=False)
        # Return detections (labels, coordinates, confidence scores)
        detections = results[0]
        labels = detections.boxes.cls.cpu().numpy() if detections.boxes is not None else []
        cords = detections.boxes.xyxy.cpu().numpy() if detections.boxes is not None else []
        scores = detections.boxes.conf.cpu().numpy() if detections.boxes is not None else []
        return labels, cords, scores

    def class_to_label(self, x):
        """Convert numeric label to class name"""
        return self.model.names[int(x)]

    def plot_boxes(self, results, frame):
        labels, cords, scores = results
        n = len(labels)

        for i in range(n):
            if scores[i] >= 0.6:  # draw boxes with confidence ≥ 0.6
                x1, y1, x2, y2 = map(int, cords[i])
                bgr = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                label = self.class_to_label(labels[i])
                text = f"{label}: {scores[i]:.2f}"
                cv2.putText(frame, text, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)

                # Save frame + trigger alert (only once)
                if MugDetection.pic == 1:
                    cv2.imwrite("frame_1.jpg", frame)
                    # Alert.Ambulance()
                    # Alert.Police()
                    Alert.FireTruck()
                MugDetection.pic += 1

        return frame

    def run(self):
        """Run the detection loop"""
        cap = self.get_video_capture()
        print("[INFO] Starting detection... Press ESC to exit.")

        while True:
            ret, frame = cap.read()
            if not ret:
                print("[ERROR] Frame not received from camera.")
                break

            frame = cv2.resize(frame, (416, 416))

            # Tampering detection logic
            Red, Green, Blue = np.sum(frame[:, :, 2]), np.sum(frame[:, :, 1]), np.sum(frame[:, :, 0])
            if (Red + Green + Blue) / 3 < 7799766:
                print("Tampered")

            # Run detection
            start_time = time()
            results = self.score_frame(frame)
            frame = self.plot_boxes(results, frame)
            end_time = time()

            fps = 1 / np.round(end_time - start_time, 2)
            cv2.putText(frame, f'FPS: {int(fps)}', (20, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

            cv2.imshow('YOLOv8 Detection', frame)

            # Exit on ESC
            if cv2.waitKey(5) & 0xFF == 27:
                cv2.destroyAllWindows()
                break

        cap.release()
        print("[INFO] Detection stopped.")
