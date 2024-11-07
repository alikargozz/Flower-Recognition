import cv2
import os
from albumentations import (
    HorizontalFlip, VerticalFlip, Rotate, RandomBrightnessContrast,
    GaussianBlur, GaussNoise, Compose
)
import numpy as np

# Görüntü klasör yolu ve çıktılar için yeni klasör yolu
input_folder = 'images'
output_folder = 'augmented_images'
os.makedirs(output_folder, exist_ok=True)

# Augmentasyon işlemleri
transform = Compose([
    HorizontalFlip(p=0.5),
    VerticalFlip(p=0.5),
    Rotate(limit=30, p=0.5),
    RandomBrightnessContrast(p=0.5),
    GaussianBlur(p=0.3),
    GaussNoise(p=0.3)
])

# Görüntüleri işle ve kaydet
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        image = cv2.imread(os.path.join(input_folder, filename))
        for i in range(5):  # Aynı görüntü için 5 augmentasyon oluştur
            augmented = transform(image=image)['image']
            new_filename = f"{os.path.splitext(filename)[0]}_aug_{i}.jpg"
            cv2.imwrite(os.path.join(output_folder, new_filename), augmented)

print("Augmentasyon işlemi tamamlandı.")
