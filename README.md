# DynoVM – Akıllı Sanal Makine Kaynak Optimizasyonu

Bu proje, sanal makinelerdeki RAM kullanımını izleyerek kaynak ihtiyacı oluştuğunda **otomatik olarak RAM artırımı yapan** kural tabanlı (Rule-Based AI) bir sistemdir.

## 🔧 Nasıl Çalışır?

1. **Kali Linux** sanal makinesinde çalışan bir Python script'i (`ram_logger.py`) RAM ve CPU kullanımını ölçer.
2. Kullanım yüzdesi bir `.txt` dosyasına yazılır.
3. Windows tarafındaki script (`increase_ram.py`) bu dosyayı izler.
4. RAM %85’i geçtiğinde:
   - Sanal makine kapanır.
   - RAM artırılır.
   - Makine tekrar açılır.
5. RAM %20’nin altına düştüğünde:
   - Sanal makine kapanır.
   - RAM azaltılır.
   - Makine tekrar açılır.

📌 Bu eşik değerleri ve RAM miktarları kullanıcı tarafından script dosyasında kolayca güncellenebilir yapıdadır.

## 📌 Kullanılan Teknolojiler
- Python
- VBoxManage (VirtualBox API)
- Rule-based 
- `psutil`, `os`, `time` modülleri

## ⚙️ Kurulum
🔧 **Not:** Kodlarda geçen klasör ve dosya yolları (`path`) örnek olarak verilmiştir.  
 Lütfen kendi sisteminizdeki klasör yapısına göre bu yolları **kendinize uygun şekilde değiştirin.**

# Kali tarafında
sudo mkdir /mnt/shared
sudo mount -t vboxsf shared /mnt/shared
cp /mnt/shared/ram_logger.py ~/
python3 ~/ram_logger.py

# Windows tarafında (CMD)
Not: VBoxManage komutu çalışmıyorsa PATH ayarı da açıklanmalı.
set PATH=%PATH%;"C:\Program Files\Oracle\VirtualBox"
VBoxManage list vms      (kali vm adı gözükür)

cd "C:\Users\ozder\OneDrive\Desktop\DynoVM_Share"
python increase_ram.py

💡 RAM kullanımını zorlamak için:
Aşağıdaki komutla RAM kullanımını geçici olarak artırabilirsin:
sudo apt install stress -y
stress --vm 2 --vm-bytes 512M --timeout 60s

💡 RAM artırımı sonrası doğrulama yapmak için:
Aşağıdaki komutu kullanarak RAM değeri güncellenmiş mi kontrol edebilirsin:
VBoxManage showvminfo "kali-linux-2025.1c-virtualbox-amd64"

## 📈 Potansiyel Kullanım Alanları
- Bulut sunucu yöneticileri
- Kaynak sıkışması yaşanan VM ortamları
- Oyun sunucuları veya pentest ortamları

## 🧠 Not
Bu sistemde AI basit kurallarla çalışmaktadır. Gelecekte tahminsel modelleme ile desteklenebilir.

Kodlarda verilen pathleri kendinize uygun yaz

