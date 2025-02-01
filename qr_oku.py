import cv2
import os
import subprocess
import platform
from pyzbar.pyzbar import decode

def qr_oku(qr_resim):
    """QR kodu okuyarak gizli günlük dosyasını açar."""
    img = cv2.imread(qr_resim)  # QR kodu oku
    kodlar = decode(img)

    for kod in kodlar:
        dosya_yolu = kod.data.decode("utf-8")  # QR kod içindeki dosya yolunu al

        print(f"📂 QR Kod İçeriği: {dosya_yolu}")  # QR kod içeriğini göster

        if os.path.exists(dosya_yolu):
            print(f"📂 Günlük açılıyor: {dosya_yolu}")

            # 🚀 İşletim sistemine göre dosyayı aç
            try:
                if platform.system() == "Windows":
                    os.startfile(dosya_yolu)  # ✅ Windows: Varsayılan TXT uygulamasını açar
                elif platform.system() == "Darwin":  # macOS
                    subprocess.run(["open", dosya_yolu])
                elif platform.system() == "Linux":
                    subprocess.run(["xdg-open", dosya_yolu])
                else:
                    print("⚠ Dosya açma işlemi desteklenmiyor.")
            except Exception as e:
                print(f"⚠ Dosya açılamadı: {str(e)}")
        else:
            print("⚠ Günlük bulunamadı! Lütfen QR kodun doğru olduğuna emin olun.")
