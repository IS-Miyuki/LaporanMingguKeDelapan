import re
from datetime import datetime
import random
import string

"Latihan 8.1"
def anagram(MainStrings = "",SubStrings = ""):
    main,sub = [i for i in MainStrings],[i for i in SubStrings]
    return (main.sort() == sub.sort())   
print(anagram("hello","olleh"))
  
print()  
    
"Latihan 8.2"
def counts(kalimat="",target=""):
    kalimat_lower = kalimat.lower()
    return kalimat_lower.count(target)
print(counts("Saya mau makan. Makan itu wajib. Mau siangatau malam saya wajib makan","makan"))

print()

"Latihan 8.3"
def NoEspace(kalimat=""):
    kalimat = kalimat.split(" ")
    hasil = " ".join([i for i in kalimat if i != ""])
    print(hasil)
NoEspace("saya tidak suka memancing ikan ")

print()

"Latihan 8.4"
def LongSort(Kalimat = ""):
    Kalimat = Kalimat.split(" ")
    Kalimat.sort(key=len)
    print(f"terpendek: {Kalimat[0]},terpanjang: {Kalimat[-1]}")
LongSort("red snakes and a black frog in the pool")

print()

"Latihan 8.5"
def FromNow(kalimat=""):
    tanggal_regex = r'\d{4}-\d{2}-\d{2}'
    list_tanggal = re.findall(tanggal_regex, teks)
    hari_ini = datetime.now()

    for tgl in list_tanggal:
        tanggal_obj = datetime.strptime(tgl, "%Y-%m-%d")
        tanggal_formatted = tanggal_obj.strftime("%d-%m-%Y")
        selisih_hari = (hari_ini - tanggal_obj).days
        print(f"{tanggal_obj} selisih {selisih_hari} hari")
teks = """
Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan
nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki
Hajar Dewantara (1889-05-02).
"""
FromNow(teks)

print()

"Latihan 8.6"
def AutoPass(teks=""):
    def generate_password(panjang=8):
        karakter = string.ascii_letters + string.digits
        print(karakter)
        return ''.join(random.choices(karakter, k=panjang))

    email_regex = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
    email_list = re.findall(email_regex, teks)

    for email in email_list:
        username = email.split('@')[0]
        password = generate_password()
        print(f"{email} username: {username} , password: {password}")
teks = """
Berikut adalah daftar email dan nama pengguna dari mailing list:
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari
"""
AutoPass(teks)
