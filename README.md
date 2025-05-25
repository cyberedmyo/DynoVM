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

## 📌 Kullanılan Teknolojiler
- Python
- VBoxManage (VirtualBox API)
- Rule-based 
- `psutil`, `os`, `time` modülleri

## ⚙️ Kurulum
Kurulum ve kullanım detayları için `usage.txt` ya da açıklama dökümanına bakınız.

## 📈 Potansiyel Kullanım Alanları
- Bulut sunucu yöneticileri
- Kaynak sıkışması yaşanan VM ortamları
- Oyun sunucuları veya pentest ortamları

## 🧠 Not
Bu sistemde AI basit kurallarla çalışmaktadır. Gelecekte tahminsel modelleme ile desteklenebilir.

