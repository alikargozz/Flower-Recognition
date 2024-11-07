import os

# Görüntülerin bulunduğu klasör yolu
image_folder = 'images'

# Her görüntüye karşılık boş bir .txt dosyası oluştur
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg'):
        txt_filename = os.path.splitext(filename)[0] + '.txt'
        txt_path = os.path.join(image_folder, txt_filename)
        
        # Eğer dosya zaten yoksa oluştur
        if not os.path.exists(txt_path):
            with open(txt_path, 'w') as f:
                pass  # Boş dosya oluştur

print("Tüm görüntüler için .txt dosyaları oluşturuldu.")
