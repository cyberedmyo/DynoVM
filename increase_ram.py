import os
import time

vm_name = "kali-linux-2025.1c-virtualbox-amd64"
usage_file = "C:/Users/ozder/OneDrive/Desktop/DynoVM_Share/usage.txt"


def read_usage():
    try:
        with open(usage_file, "r") as f:
            content = f.read().strip()
            ram, cpu = content.split(",")
            return float(ram), float(cpu)
    except Exception as e:
        print(f"Hata: {e}")
        return 0, 0


def increase_ram(new_ram_mb):
    print(f"💡 RAM artırılıyor: {new_ram_mb} MB")

    #  1) Makineyi kapat
    os.system(f'VBoxManage controlvm "{vm_name}" poweroff')
    time.sleep(5)

    #  2) RAM miktarını artır
    os.system(f'VBoxManage modifyvm "{vm_name}" --memory {new_ram_mb}')

    #  3) Tekrar başlat
    os.system(f'VBoxManage startvm "{vm_name}" --type gui')

    print("✅ RAM artırımı tamamlandı ve makine tekrar başlatıldı.")


# İzleme döngüsü
while True:
    ram, cpu = read_usage()
    print(f"RAM: {ram}%  |  CPU: {cpu}%")

    if ram > 85:
        increase_ram(4096)  # RAM’i 4096 MB yap
        break

    time.sleep(5)
