Terminal Tabanlı Python Paket Yükleyici

Bu script, seçtiğiniz `pip` veya `pip3` komutuyla belirlenmiş paket listesini **etkileşimli** olarak kurar.  
Kurulum esnasında renkli çıktılar, adım göstergesi ve hata yakalama içerir.

## Özellikler
- `pip` / `pip3` seçimi
- Renkli ve adımlı çıktı
- Hata mesajlarını yakalama ve özetleme
- Liste içindeki paketleri tek tek kurma

## Gereksinimler
- Python 3.8+ (önerilir 3.10/3.11)
- İnternet bağlantısı
- (Öneri) Sanal ortam (virtualenv)

> **Derleme gerektiren paketler**
> - **Ubuntu/Debian**:  
>   ```bash
>   sudo apt-get install build-essential cmake libopenblas-dev liblapack-dev libx11-dev libgtk-3-dev
>   ```
> - **macOS (Homebrew)**:  
>   ```bash
>   brew install cmake openblas
>   ```

## Kurulum
```bash
# Depoyu klonlayın
git clone https://github.com/<KULLANICI_ADINIZ>/<REPO_ADI>.git
cd <REPO_ADI>

# (Öneri) Sanal ortam oluşturun
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# (İsteğe bağlı) pip’i güncelleyin
python -m pip install --upgrade pip
Çalıştırma
bash
# Script'i çalıştırın
python setup.py
# veya
python3 setup.py
Script sizden pip mi pip3 mü kullanmak istediğinizi sorar ve listedeki paketleri tek tek kurar.


bash


setup.py — Paketleri tek tek kuran interaktif terminal aracı



LICENSE — MIT

Sık Karşılaşılan Sorunlar
dlib derleme hatası: Yukarıdaki platforma özel önkoşulların kurulu olduğundan emin olun (CMake ve derleyiciler).

İzin hataları: Sanal ortam kullanın veya --user ile yüklemeyi deneyin:

bash

pip install --user paket_adı
Proxy/SSL sorunları: pip için --trusted-host veya --proxy parametreleri gerekebilir.

Lisans
Bu proje MIT lisansı ile lisanslanmıştır. Ayrıntılar için LICENSE dosyasına bakın.
