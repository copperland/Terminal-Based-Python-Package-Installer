import os
import subprocess
import time

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# Gerekli paketleri packages ekleyin
packages = [
    "backports.entry-points-selectable==1.1.0",
    "click==8.0.1",
    "cycler==0.10.0",
    "distlib==0.3.2",
    "dlib",
    "et-xmlfile==1.1.0",
    "face-recognition==1.3.0",
    "face-recognition-models==0.3.0",
    "filelock==3.0.12",
    "Flask==2.0.1",
    "imageio==2.27",
    "itsdangerous==2.0.1",
    "Jinja2==3.0.3",

]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pip_install(pip_cmd):
    clear_screen()
    print(f"{Colors.HEADER}{Colors.BOLD}Python Paket Yükleyici Başladı{Colors.ENDC}\n")
    for i, pkg in enumerate(packages, 1):
        print(f"{Colors.OKBLUE}[{i}/{len(packages)}] {Colors.ENDC}Yükleniyor: {Colors.BOLD}{pkg}{Colors.ENDC}")
        try:
            result = subprocess.run(
                [pip_cmd, "install", pkg],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            if result.returncode == 0:
                print(f"{Colors.OKGREEN}  Başarıyla yüklendi.{Colors.ENDC}\n")
            else:
                print(f"{Colors.FAIL}  Hata oluştu: {result.stderr.strip()[:100]}...{Colors.ENDC}\n")
        except Exception as e:
            print(f"{Colors.FAIL}  Beklenmeyen hata: {e}{Colors.ENDC}\n")
        time.sleep(0.3)
    print(f"{Colors.OKCYAN}Tüm paketler işlendi.{Colors.ENDC}")

def setup():
    clear_screen()
    print(f"""
{Colors.BOLD}
   _____      _                 
  / ____|    | |                
 | (___   ___| |_ _   _ _ __    
  \___ \ / _ \ __| | | | '_ \   
  ____) |  __/ |_| |_| | |_) |  
 |_____/ \___|\__|\__,_| .__/   
                        | |      
                        |_|      
{Colors.ENDC}
    """)
    print("Paketleri hangi komutla yüklemek istersiniz?")
    print(f"{Colors.OKGREEN}[1]{Colors.ENDC} pip")
    print(f"{Colors.OKGREEN}[2]{Colors.ENDC} pip3")
    choice = input("\nSeçiminiz (1/2): ").strip()

    if choice == "1":
        pip_cmd = "pip"
    elif choice == "2":
        pip_cmd = "pip3"
    else:
        print(f"{Colors.WARNING}Geçersiz seçim. Varsayılan olarak 'pip' seçildi.{Colors.ENDC}")
        pip_cmd = "pip"

    pip_install(pip_cmd)

if __name__ == "__main__":
    setup()
