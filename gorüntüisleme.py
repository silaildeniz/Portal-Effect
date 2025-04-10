import cv2  # OpenCV kütüphanesini içe aktar
import numpy as np  # NumPy kütüphanesini içe aktar

# Kamerayı başlat
cap = cv2.VideoCapture(0)  # Varsayılan kamerayı aç

while True:
    ret, frame = cap.read()  # Kameradan bir kare oku
    if not ret:  # Eğer kare okunamazsa döngüden çık
        break

    height, width = frame.shape[:2]  # Görüntünün yüksekliğini ve genişliğini al
    center_x, center_y = width // 2, height // 2  # Görüntünün merkez koordinatlarını belirle

    # Portal efekti için girdap oluştur
    strength = 0.002  # Girdabın yoğunluğunu belirle
    radius = min(center_x, center_y)  # Efektin uygulanacağı yarıçapı belirle

    # Koordinat matrislerini oluştur
    y_indices, x_indices = np.indices((height, width), dtype=np.float32)  # Piksel koordinatlarını matris olarak oluştur
    dx = x_indices - center_x  # X eksenindeki mesafeyi hesapla
    dy = y_indices - center_y  # Y eksenindeki mesafeyi hesapla
    distance = np.sqrt(dx ** 2 + dy ** 2)  # Her pikselin merkeze olan uzaklığını hesapla

    # Girdap açısını hesapla
    angle = np.where(distance < radius, strength * (radius - distance), 0)  # Belirli bir yarıçap içindeki açıyı hesapla
    cos_a = np.cos(angle)  # Kosinüs değerini hesapla
    sin_a = np.sin(angle)  # Sinüs değerini hesapla

    # Yeni koordinatları hesapla
    new_x = (cos_a * dx - sin_a * dy + center_x).astype(np.float32)  # X koordinatlarını döndürerek güncelle
    new_y = (sin_a * dx + cos_a * dy + center_y).astype(np.float32)  # Y koordinatlarını döndürerek güncelle

    # Portal efektini uygula
    warped_frame = cv2.remap(frame, new_x, new_y, cv2.INTER_LINEAR)  # Yeni koordinatlara göre görüntüyü yeniden eşle

    # Görüntüyü ekranda göster
    cv2.imshow("Portal Effect", warped_frame)  # İşlenmiş görüntüyü ekranda göster

    # Çıkış için 'q' tuşuna basılmasını bekle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # 'q' tuşuna basıldığında döngüyü sonlandır

# Kaynakları serbest bırak
cap.release()  # Kamerayı kapat
cv2.destroyAllWindows()  # Açık olan tüm pencereyi kapat
