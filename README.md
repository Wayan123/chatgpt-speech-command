# Chatgpt Speech Command 

Chatgpt Speech Command dibuat khusus untuk perintah berbahasa Indonesia dan respon juga dalam bahasa Indonesia, kemudian anda dapat mengubah bahasa sesuai selera.

Code berjalan pada Linux, ditest dan berjalan baik pada Ubuntu 2022.1 LTS. Sedangkan untuk versi windows akan segera dibuat.

Cara install:
1. Lebih bagus buat environment menggunakan conda
2. Install dahulu requirements dengan cara 'pip install -r requirements.txt'
3. Install pyaudio menggunakan 'sudo apt install python3-pyaudio'
4. Edit code python chatgpt-linux.py menggunakan code editor, lalu isi api-key milik kamu di GPT 3 API key.

Jalankan dengan 'python chatgpt-linux.py' 

Selamat mencoba, semoga berhasil. 

# Tips
Jika anda menemukan opsi seperti ini, anda dapat menghilangkannya secara manual dengan mengedit kode init,

![bug1](https://user-images.githubusercontent.com/17795544/216879367-467d1aca-ac4b-4a82-ae14-0f489571d192.jpg)

langkah-langkahnya adalah (khusus untuk env menggunakan anaconda atau miniconda), buka menuju Home\anaconda3 atau miniconda\envs\chatgpt (sesuaikan dengan nama env)\Lib\site-packages\speech_recognition lalu cari filr bernama __init__.py. Intinya dari saja file di site-packages lalu cari speech recognition nah didalamnya lah file init tadi.

![bug2](https://user-images.githubusercontent.com/17795544/216879946-1e78c2ab-8365-43ab-b68d-2561d6bbf14f.jpg)

Lalu menuju baris ke 917 dan 918 atau bisa juga dengan fitur pencarian CTRL + F lalu ketik result2, nahh kedua baris tersebut diubah menjadi komentar,

![bug3](https://user-images.githubusercontent.com/17795544/216880356-779cab3b-4bfd-4163-867f-34f47d9ac22b.jpg)

Ubah jadi komentar menggunakan tanda tagar # seperti pada gambar, jika selesai lalu save dan jalankan ulang kode chatgpt-linux.py anda.
