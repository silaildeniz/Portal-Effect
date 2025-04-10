# Portal-Effect
Portal Effect with OpenCV
Bu Python betiği, gerçek zamanlı video akışında portal efekti (girdap efekti) oluşturur. OpenCV ve NumPy kütüphaneleri kullanılarak, kameradan alınan görüntüdeki her pikselin merkezden uzaklığına göre, girdap etkisi uygulanır.

# Gereksinimler
Bu projeyi çalıştırabilmek için aşağıdaki Python kütüphanelerinin yüklü olması gerekir:

OpenCV (cv2)
NumPy (numpy)

Yüklemek için şu komutları kullanabilirsiniz:

# pip install opencv-python numpy
# Kullanım
Kodu çalıştırın:

Bu betik, bilgisayarınızdaki varsayılan kamerayı açarak görüntü akışını başlatacaktır.

# Portal Efekti:

Gerçek zamanlı görüntü üzerinde portal (girdap) efekti uygulanacaktır. Efekt, her pikselin merkeze olan uzaklığını baz alarak bir döndürme işlemi uygular.

Kapatmak için:

Uygulamayı kapatmak için, video penceresinin açık olduğu sırada 'q' tuşuna basın.

# Kod Açıklamaları
Kamera Başlatma: cv2.VideoCapture(0) ile bilgisayarın varsayılan kamerası açılır.

Efektin Uygulanması: Her bir piksel için merkezden uzaklık hesaplanır ve bu mesafeye göre bir açı ve döndürme işlemi uygulanır.

cv2.remap: Bu fonksiyon, piksel koordinatlarını döndürüp yeniden eşler ve girdap efektini oluşturur.

Çıkış: Video penceresi açıldığında 'q' tuşuna basarak uygulamadan çıkılabilir.

# Bu betik, yalnızca bir kameraya sahip cihazlarda çalışacaktır.

# Girdap etkisinin yoğunluğu ve yarıçapı, kod içinde ayarlanabilir.

# Video akışı, gerçek zamanlı olarak işlenir, bu yüzden performans cihazınıza göre değişebilir.

# Lisans
Bu proje, MIT lisansı altında lisanslanmıştır. Detaylar için LICENSE dosyasına bakabilirsiniz.
