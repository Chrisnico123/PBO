<h1 align="center"> <img alt="Last - Ninja" title="Last - Ninja" width="50">Tap Tap Defense </h1> <br>

<p align="center">
    <img alt="Tap Tap Defense" title="Tap Tap Defense" src="assets/ss1.png" width="600">
</p>
<p>
<p align="center"> Last - Ninja <br>
(Tugas Besar PBO RD-10) <br>
</p>
<p align="center">
    <a href="https://github.com/rajastra/Tap-Tap-Defense/graphs/contributors">
    <img src="https://img.shields.io/badge/contributors-6-red?style=flat-square&logo=appveyor" alt="Contributors">
  </a>
    <a href="https://www.pygame.org/news">
    <img src="https://img.shields.io/pypi/v/pygame?style=flat-square&logo=appveyor" alt="Pygame">
  </a>
</p>

<br>

## Description of Project

Proyek yang kami buat yaitu Proyek game sederhana bernama <b>Last - Ninja</b>, <b>Last - Ninja</b> adalah sebuah game yang berkonsep sama seperti game Dinosaurus yang ada di google chrome, jadi nanti ada sebuah character yang dapat digerakan oleh user, character dapat digerakan dengan cara menekan tombol panah atas untuk melompat dan panah bawah untuk menunduk.

## How to Run a Game

- #### Install Dependecies

```bash
git clone https://github.com/rajastra/Tap-Tap-Defense
```

```bash
cd PBO
```

```bash
pip install pygame
```

- ### Run a Game

```python
python main.py
```

<br>

<br>

## How to Run a Game in Docker (Linux)

<br>

### Step 1

Buka Terminal pada Linux anda masing-masing dan pastikan docker sudah terinstall di komputer anda.
<br>

### Step 2

Silahkan clone file game yang ada di Github dengan cara :
<br>
Syntax :

```bash
sudo git clone
```

<br>

### Step 3

Build :
<br>
Syntax :

```bash
sudo docker build -t last-ninja .
```

### Step 4

Jalankan Perintah berikut ini:

```bash
XAUTH=$HOME/.Xauthority
touch $XAUTH
xhost +
xhost + username (username linux anda)
```

<br>

### Last Step

Run a Game

```bash
docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix  -e DISPLAY=unix$DISPLAY --device /dev/snd mckriw/last-ninja
```

Or

```bash
sudo docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix  -e DISPLAY=unix$DISPLAY --device /dev/snd mckriw/last-ninja
```

<br>

## 🚀 About Team (Kelompok 10)

-Chrisnico Alexander Hutapea 120140244

-Iqbal Alfarizi 120140122

-Booby Julian Akbar 120140082

-Alfahmi Irfan 120140206

-Michael Pascalis Simanjuntak 120140137
