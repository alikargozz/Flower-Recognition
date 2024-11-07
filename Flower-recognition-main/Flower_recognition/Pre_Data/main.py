import os
import torch
from ultralytics import YOLO

def train_model():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Using device: {device}")

    # YOLOv8 nano modelini başlat
    model = YOLO('yolov8n.pt')

    # Modeli eğit
    model.train(data='data.yaml', epochs=100, optimizer='Adam', patience=10, lr0=0.0001, imgsz=640, device=device, amp=False)


if __name__ == '__main__':
    train_model()
