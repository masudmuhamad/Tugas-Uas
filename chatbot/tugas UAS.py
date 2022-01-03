import re
import random

sapaan = ['hai juga', 'halo juga', 'apa kabar']
respon = ['halo itu namaku']
kabar = ['luar biasa, terima kasih sudah bertanya']
nama = ['namaku chatbot', 'panggil aja chatbot']
umur = ['aku berumur 20 tahun']
tugas = ['tugasku menjawab pertanyaan sederhana dari kamu']
bingung = ['mana kutahu, kau belom mengenalkan diri']
identifikasi = ['hai, senang berkenalan denganmu']
error = ['kamu ngomong apa sih']
syukur = ['senang mendengarnya']

while True:
    x = input("User\t: ")

    if re.findall(r'halo|hai', x):
        print("Bot\t:", random.choice(sapaan))
    elif re.findall(r'halo chatbot', x):
        print("Bot\t:", random.choice(respon))
    elif re.findall(r'bagaimana kabarmu', x):
        print("Bot\t:", random.choice(kabar))
    elif re.findall(r'siapa namamu|namamu siapa', x):
        print("Bot\t:", random.choice(nama))
    elif re.findall(r'berapa umurmu', x):
        print("Bot\t:", random.choice(umur))
    elif re.findall(r'apa tugasmu chatbot?', x):
        print("Bot\t:", random.choice(tugas))
    elif re.findall(r'siapa aku', x):
        print("Bot\t:", random.choice(bingung))
    elif re.findall(r'namaku mas`ud', x):
        print("Bot\t:", random.choice(identifikasi))
    elif re.findall(r'baik', x):
        print("Bot\t:", random.choice(syukur))
    else:
        print("Bot\t:", random.choice(error))


        




