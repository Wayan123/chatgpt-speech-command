# ChatGPT with Speech Command 

Chatgpt Speech Command dibuat khusus untuk perintah berbahasa Indonesia dan respon juga dalam bahasa Indonesia, kemudian anda dapat mengubah bahasa sesuai selera.

# 1. Versi Linux

Code berjalan pada Linux, ditest dan berjalan baik pada Ubuntu 22.04.1 LTS, dan anda bisa menggunakan Linux versi lainnya. 

Cara install:
1. Lebih bagus buat environment menggunakan conda
2. Install dahulu requirements dengan cara 'pip install -r requirements-linux.txt'
3. Install pyaudio menggunakan 'sudo apt install python3-pyaudio'
4. Edit code python chatgpt-linux.py menggunakan code editor, lalu isi api-key milik kamu di GPT 3 API key. Dapatkan API key disini https://beta.openai.com/account/api-keys.

Jalankan dengan 'python chatgpt-linux.py' 

Selamat mencoba, semoga berhasil. 

# 2. Versi Windows

Code berjalan pada Windows, ditest dan berjalan baik pada Windows 11, dan anda juga bisa menggunakan windows 8 dan 10. 

Cara install:
1. Lebih bagus buat environment menggunakan conda
2. Install dahulu requirements dengan cara 'pip install -r requirements-windows.txt'
3. Install pyaudio menggunakan 'conda install PyAudio'
4. Edit code python chatgpt-windows.py menggunakan code editor, lalu isi api-key milik kamu di GPT 3 API key. Dapatkan API key disini https://beta.openai.com/account/api-keys

Jalankan dengan 'python chatgpt-windows.py' 

Selamat mencoba, semoga berhasil. Sama, jangan lupa ngopi ya gan. 

Agan senang adalah kebahagiaan saya dan saya pun bisa beli Rubicon :D

# Tips
Jika anda menemukan opsi seperti ini, anda dapat menghilangkannya secara manual dengan mengedit kode __init__.py,

![bug1](https://user-images.githubusercontent.com/17795544/216879367-467d1aca-ac4b-4a82-ae14-0f489571d192.jpg)

langkah-langkahnya adalah (khusus untuk env menggunakan anaconda atau miniconda), buka menuju Home\anaconda3 atau miniconda\envs\chatgpt (sesuaikan dengan nama env)\Lib\site-packages\speech_recognition lalu cari file bernama __init__.py. Intinya cari saja directory site-packages lalu cari directory speech recognition, nah didalamnya lah file __init__.py tadi.

![bug2](https://user-images.githubusercontent.com/17795544/216879946-1e78c2ab-8365-43ab-b68d-2561d6bbf14f.jpg)

Lalu menuju baris ke 917 dan 918 atau bisa juga dengan fitur pencarian CTRL + F, dan ketik result2, nahh jika sudah ketemu, ubah kedua baris tersebut menjadi komentar,

![bug3](https://user-images.githubusercontent.com/17795544/216880356-779cab3b-4bfd-4163-867f-34f47d9ac22b.jpg)

Ubah jadi komentar menggunakan tanda tagar # seperti pada gambar, jika selesai lalu save dan jalankan ulang kode chatgpt-linux.py anda.
