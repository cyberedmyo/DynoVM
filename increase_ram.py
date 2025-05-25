import os
import time

# 💡 Kullanıcı tanımlı parametreler
vm_name = "kali-linux-2025.1c-virtualbox-amd64"
usage_file = "C:/Users/ozder/OneDrive/Desktop/DynoVM_Shared/usage.txt"

ram_high_threshold = 85   # Yüzde olarak üst sınır
ram_low_threshold = 20    # Yüzde olarak alt sınır

ram_high_value = 4096     # MB cinsinden artırılmış RAM
ram_low_value = 2048      # MB cinsinden azaltılmış RAM

def read_usage():
    try:
        with open(usage_file, "r") as f:
            content = f.read().strip()
            ram, cpu = content.split(",")
            return float(ram), float(cpu)
    except Exception as e:
        print(f"Hata: {e}")
        return 0, 0

def change_ram(new_ram_mb):
    print(f"\n🔄 RAM değeri değiştiriliyor: {new_ram_mb} MB")

    # 1️⃣ Makineyi kapat
    os.system(f'VBoxManage controlvm "{vm_name}" poweroff')
    time.sleep(5)

    # 2️⃣ RAM miktarını değiştir
    os.system(f'VBoxManage modifyvm "{vm_name}" --memory {new_ram_mb}')

    # 3️⃣ Makineyi arayüzle başlat
    os.system(f'VBoxManage startvm "{vm_name}" --type gui')

    print("✅ RAM değişimi tamamlandı ve makine tekrar başlatıldı.\n")

# 🔁 İzleme döngüsü
while True:
    ram, cpu = read_usage()
    print(f"RAM: {ram}%  |  CPU: {cpu}%")

    if ram > ram_high_threshold:
        change_ram(ram_high_value)
        break

    elif ram < ram_low_threshold:
        change_ram(ram_low_value)
        break
    time.sleep(5)
