import statistics
import random

kitaplar = [
 {"isim": "Veri Bilimi 101", "yazar": "Ali", "tur": "Bilim", "satis": 1200, "yil": 2021},
 {"isim": "Python ile Yapay Zeka", "yazar": "Ayşe", "tur": "Bilim", "satis": 950, "yil":
2020},
 {"isim": "İstatistik Temelleri", "yazar": "Ali", "tur": "Akademik", "satis": 700, "yil": 2019},
 {"isim": "Makine Öğrenmesi", "yazar": "Can", "tur": "Bilim", "satis": 1800, "yil": 2022},
 {"isim": "Veri Görselleştirme", "yazar": "Deniz", "tur": "Sanat", "satis": 400, "yil": 2018},
 {"isim": "Matematiksel Modelleme", "yazar": "Ali", "tur": "Akademik", "satis": 1500,
"yil": 2021},
 {"isim": "Bilgi Toplumu", "yazar": "Ayşe", "tur": "Sosyal", "satis": 600, "yil": 2022}
]

def en_cok_satan(kitaplar):
    return max(kitaplar, key=lambda x: x["satis"])['isim']
print(f"En çok satan kitap: {en_cok_satan(kitaplar)}")

def yazar_satislari(kitaplar):
    satis_dict={}
    for kitap in kitaplar:
        yazar = kitap["yazar"]
        satis = kitap["satis"]
        if yazar in satis_dict:
            satis_dict[yazar] += satis
        else:
            satis_dict[yazar] = satis
    return satis_dict

print(f"Her yazarın toplam satışı: {yazar_satislari(kitaplar)}")

kitap_turlerinin_seti = set(map(lambda x: x['tur'],kitaplar))
print(f"Tüm kitap türleri:{kitap_turlerinin_seti}")

# NOT: daha kısa şekilde: turler = {kitap['tur'] for kitap in kitaplar}

satis_sayisi_fazla_seti = list(filter(lambda x: int(x['satis']) > 1000,kitaplar))
satis_sayisi_fazla_isimleri = list(map(lambda x: x['isim'],satis_sayisi_fazla_seti))
print(f"Satış adedi 1000’den fazla olan kitaplar: {satis_sayisi_fazla_isimleri}")

# NOT: bunun daha kısası şu şekilde yazılabilir: satis_sayisi_fazla_isimleri = [kitap['isim'] for kitap in kitaplar if int(kitap['satis']) > 1000]

kitaplar_2020_sonrasi = list(filter(lambda x: int(x['yil'])>2020, kitaplar))
kitaplar_2020_sonrasi_yeni = list(map(lambda x: {**x,'satis': int(x['satis'] * 110/100)}, kitaplar_2020_sonrasi))
# NOT: **x  eski sözlüğü kopyalaıp sadece satis değerini günceller
print(f"Tüm satış adetlerini %10 artırılmış şekli: {kitaplar_2020_sonrasi_yeni}")

satis_siralamasi = sorted(kitaplar_2020_sonrasi_yeni, key=lambda x: x['satis'], reverse=True)
print(f"Satış miktarına göre azalan şekilde:{satis_siralamasi}")

satislar = [kitap['satis'] for kitap in kitaplar]
ortalama_satis = statistics.mean(satislar)

standart_sapma = statistics.stdev(satislar)
print(f"Satışların standart sapması: {standart_sapma:.1f}")

turlerin_satis_toplami = {}
for kitap in kitaplar:
    tur = kitap["tur"]
    satis = kitap["satis"]
    if tur in turlerin_satis_toplami:
        turlerin_satis_toplami[tur] += satis
    else:
        turlerin_satis_toplami[tur] = satis

en_cok_satan_tur = max(turlerin_satis_toplami, key=turlerin_satis_toplami.get)
# NOT: key=turlerin_satis_toplami.get fonksiyonuna anahtarları değil, anahtarların karşılık geldiği değerleri karşılaştırmasını söyler

print(f"Ortalama satış adedi:{ortalama_satis:.1f} ve en çok satış yapan tür: {en_cok_satan_tur}")

# standart sapma yanlış cıkıyor

# Train/Test veri setini oluşturma
random.seed(42)  # Sonuçların tekrar üretilebilir olması için

train_size = int(len(kitaplar) * 0.7)
train_kitaplar = random.sample(kitaplar, train_size)
test_kitaplar = [kitap for kitap in kitaplar if kitap not in train_kitaplar]

print(f"Eğitim kitapları ({len(train_kitaplar)}): {[k['isim'] for k in train_kitaplar]}")
print(f"Test kitapları ({len(test_kitaplar)}): {[k['isim'] for k in test_kitaplar]}")

# Yazarların ortalama satışını hesaplama

yazar_toplam = {}
yazar_sayisi = {}

for kitap in train_kitaplar:
    yazar = kitap['yazar']
    satis = kitap['satis']
    yazar_toplam[yazar] = yazar_toplam.get(yazar, 0) + satis  #dict.get(key, default) → key yoksa default döner, varsa değerini döner
    yazar_sayisi[yazar] = yazar_sayisi.get(yazar, 0) + 1

yazar_ortalama = {yazar: yazar_toplam[yazar]/yazar_sayisi[yazar] for yazar in yazar_toplam}
print(f"Yazarların eğitim verisindeki ortalama satışları: {yazar_ortalama:}")

# hangi kitapların satışları yazar ortalamasının üzerinde

kitaplar_ortalama_ustu = []

for kitap in test_kitaplar:
    yazar = kitap['yazar']
    satis = kitap['satis']
    ortalama = yazar_ortalama.get(yazar, 0)  # yazar eğitimde yoksa 0 kabul et
    if satis > ortalama:
        kitaplar_ortalama_ustu.append(kitap['isim'])

print(f"Test verisinde satışları yazar ortalamasının üzerinde olan kitaplar: {kitaplar_ortalama_ustu}")



