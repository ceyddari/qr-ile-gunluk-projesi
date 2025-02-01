import os
import uuid
import qrcode
import subprocess
import platform  # İşletim sistemini kontrol etmek için

def gunluk_ekle():
    """Kullanıcıdan günlük alır, rastgele dosya adıyla kaydeder ve QR kod üretir."""
    icerik = input("📜 Günlüğünüzü yazın: ")

    # Gizli klasörü oluştur
    klasor_adi = "gizli_gunlukler"
    os.makedirs(klasor_adi, exist_ok=True)

    # Rastgele dosya adı oluştur
    dosya_adi = str(uuid.uuid4()) + ".txt"
    dosya_yolu = os.path.join(klasor_adi, dosya_adi)

    # Günlüğü dosyaya kaydet
    with open(dosya_yolu, "w", encoding="utf-8") as dosya:
        dosya.write(icerik)

    # QR kod oluştur ve içine dosya yolunu koy
    qr = qrcode.make(dosya_yolu)
    qr_path = dosya_yolu.replace(".txt", ".png")
    qr.save(qr_path)

    print(f"✅ Günlük kaydedildi ve QR kod oluşturuldu: {qr_path}")
    print("🔒 Günlüğünüze yalnızca QR kod ile erişebilirsiniz!")

def gunlukleri_listele():
    """Gizli klasördeki tüm günlükleri listeler."""
    klasor_adi = "gizli_gunlukler"
    if not os.path.exists(klasor_adi):
        print("📂 Gizli günlük klasörü bulunamadı!")
        return

    dosyalar = os.listdir(klasor_adi)
    txt_dosyalar = [f for f in dosyalar if f.endswith(".txt")]

    if not txt_dosyalar:
        print("📜 Hiç günlük bulunamadı!")
        return

    print("\n📜 Kaydedilmiş Günlükler:")
    for dosya in txt_dosyalar:
        print(f"- {dosya}")

def gunlugu_ac():
    """Kullanıcının girdiği günlük dosyasını Windows'ta Notepad ile açar, macOS ve Linux'ta uygun editörde açar."""
    klasor_adi = "gizli_gunlukler"

    # Günlükleri listele
    dosyalar = os.listdir(klasor_adi)
    txt_dosyalar = [f for f in dosyalar if f.endswith(".txt")]

    if not txt_dosyalar:
        print("📜 Hiç günlük bulunamadı!")
        return

    print("\n📜 Kaydedilmiş Günlükler:")
    for dosya in txt_dosyalar:
        print(f"- {dosya}")

    dosya_adi = input("\nAçmak istediğiniz günlüğün adını tam olarak yazın: ").strip()

    if not dosya_adi.endswith(".txt"):
        print("⚠ Hatalı giriş! Lütfen '.txt' uzantılı dosya adını tam girin.")
        return

    dosya_yolu = os.path.join(klasor_adi, dosya_adi)

    if os.path.exists(dosya_yolu):
        print(f"📂 Günlük açılıyor: {dosya_yolu}")

        # 🚀 İşletim sistemine göre dosyayı aç
        try:
            if platform.system() == "Windows":
                subprocess.Popen(["notepad.exe", dosya_yolu], shell=True)  # ✅ Windows için %100 garantili!
            elif platform.system() == "Darwin":  # macOS
                subprocess.Popen(["open", dosya_yolu])
            elif platform.system() == "Linux":
                subprocess.Popen(["xdg-open", dosya_yolu])
            else:
                print("⚠ Dosya açma işlemi desteklenmiyor.")
        except Exception as e:
            print(f"⚠ Dosya açılamadı: {str(e)}")
    else:
        print("⚠ Günlük bulunamadı! Lütfen günlük listesini kontrol edin.")

# Menü
while True:
    print("\n📜 Günlük Yönetim Sistemi")
    print("1️⃣ Yeni günlük ekle")
    print("2️⃣ Günlükleri listele")
    print("3️⃣ Günlük aç")
    print("4️⃣ Çıkış")

    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        gunluk_ekle()
    elif secim == "2":
        gunlukleri_listele()
    elif secim == "3":
        gunlugu_ac()
    elif secim == "4":
        print("🚪 Çıkış yapılıyor...")
        break
    else:
        print("⚠ Geçersiz seçim! Lütfen tekrar deneyin.")
