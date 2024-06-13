import requests
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from itertools import zip_longest

app = FastAPI(
    title="MC Tour Guide",
    description="Kami menyediakan layanan pemandu wisata yang berpengalaman dan profesional untuk membantu perjalanan wisata Anda menjadi lebih menyenangkan.",
    docs_url="/",
)

@app.get("/")
async def read_root():
    return {"Data": "Successful"}

# Model untuk Data tour guide
class Tourguide(BaseModel):
    id_guider: str
    nama_guider: str
    profile: str
    no_hp: str
    fee: int
    history: int
    feedback: int
    travelType: str
    status_ketersediaan: str

# Dummy data untuk tourguide
data_tourguide = [
    {"id_guider": "1111", "nama_guider": "Chadkowi", "profile": "Seorang pemandu wisata berpengalaman dengan kecintaan pada petualangan alam yang menawarkan pengalaman mendaki gunung dan menjelajahi hutan yang luas.", "no_hp": "911", "fee": 200000, "history": 54, "feedback": 10, "travelType": "Business", "status_ketersediaan": "Bisa"},
    {"id_guider": "2222", "nama_guider": "Prabroro", "profile": "Seorang pemandu wisata yang ahli dalam memperkenalkan budaya lokal dan sejarah di setiap destinasi.", "no_hp": "119", "fee": 400000, "history": 56, "feedback": 10, "travelType": "Business", "status_ketersediaan": "Bisa"},
    {"id_guider": "3333", "nama_guider": "Anisa", "profile": "Seorang pemandu wisata yang mengutamakan pengalaman mewah dan layanan berkualitas tinggi, memastikan setiap perjalanan menjadi pengalaman yang istimewa", "no_hp": "919", "fee": 500000, "history": 47, "feedback": 10, "travelType": "Others","status_ketersediaan": "Bisa"},
    {"id_guider": "4444", "nama_guider": "Janggar", "profile": "Seorang pemandu wisata yang ramah keluarga dengan keahlian dalam merencanakan liburan yang menyenangkan bagi seluruh anggota keluarga.", "no_hp": "119", "fee": 450000, "history": 100, "feedback": 9, "travelType": "Holliday","status_ketersediaan": "Bisa"},
    {"id_guider": "5555", "nama_guider": "Mahfud DM", "profile": "Mampu menjelaskan seluk beluk tempat-tempat yang dikunjungi saat perjalanan wisata.", "no_hp": "991", "fee": 300000, "history": 48, "feedback": 9, "travelType": "Education", "status_ketersediaan": "Bisa"}
]

# Endpoint untuk menambahkan data tourguide
@app.post("/tourguide")
def tambah_tourguide(tourguide: Tourguide):
    data_tourguide.append(tourguide.dict())
    return {"message": "Data Guider berhasil ditambahkan."}

# Endpoint untuk mendapatkan data tourguide
@app.get("/tourguide", response_model=List[Tourguide])
def get_tourguide():
    return data_tourguide

def get_tourguide_index(id_guider: str) -> Optional[int]:
    for index, tourguide in enumerate(data_tourguide):
        if tourguide['id_guider'] == id_guider:
            return index
    return None

@app.get("/tourguide/{id_guider}", response_model=Tourguide)
def get_tourguide_by_id(id_guider: str):
    index = get_tourguide_index(id_guider)
    if index is not None:
        return Tourguide(**data_tourguide[index])
    raise HTTPException(status_code=404, detail="Data Guider tidak ditemukan.")

@app.put("/tourguide/{id_guider}")
def update_tourguide_by_id(id_guider: str, tourguide: Tourguide):
    index = get_tourguide_index(id_guider)
    if index is not None:
        data_tourguide[index] = tourguide.dict()
        return {"message": "Data Guider berhasil diperbarui."}
    else:
        raise HTTPException(status_code=404, detail="Data Guider tidak ditemukan.")

@app.delete("/tourguide/{id_guider}")
def delete_guider(id_guider: str):
    index = get_tourguide_index(id_guider)
    if index is not None:
        del data_tourguide[index]
        return {"message": "Data Guider berhasil dihapus."}
    else:
        raise HTTPException(status_code=404, detail="Data Guider tidak ditemukan.")










# Model for Insurance Data
class Asuransi(BaseModel):
    id_asuransi: str
    premi: str
    tanggal_mulai_asuransi: str
    tanggal_selesai_asuransi: str

# Fungsi untuk mengambil data asuransi dari web hosting lain
def get_data_asuransi_from_web():
    url = "https://eai-fastapi.onrender.com/asuransi"  # Ganti dengan URL yang benar
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Gagal mengambil data asuransi dari web hosting.")

# Endpoint to get insurance data
@app.get("/asuransi", response_model=List[Asuransi])
def get_asuransi():
    data_asuransi = get_data_asuransi_from_web()
    return data_asuransi

# Endpoint to get insurance data by id_asuransi
@app.get("/asuransi/{id_asuransi}", response_model=Asuransi)
def get_asuransi_by_id(id_asuransi: str):
    data_asuransi = get_data_asuransi_from_web()
    for item in data_asuransi:
        if item['id_asuransi'] == id_asuransi:
            return item
    raise HTTPException(status_code=404, detail="Asuransi not found")









# Model untuk Data Objek Wisata
class ObjekWisata(BaseModel):
    id_wisata: str
    nama_objek: str
    nama_daerah: str
    kategori: str
    alamat: str
    kontak: str
    harga_tiket: int

# Fungsi untuk mengambil data objek wisata dari web hosting lain
def get_data_objekWisata_from_web():
    url = "https://pajakobjekwisata.onrender.com/wisata"  # Ganti dengan URL yang sebenarnya
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Gagal mengambil data objek wisata dari web hosting.")

# Endpoint untuk mendapatkan data objek wisata
@app.get("/objekWisata", response_model=List[ObjekWisata])
def get_objekWisata():
    data_objekWisata = get_data_objekWisata_from_web()
    return data_objekWisata

# Endpoint untuk mendapatkan data objek wisata berdasarkan id_objekWisata
@app.get("/objekWisata/{id_wisata}", response_model=ObjekWisata)
def get_objekWisata_by_id(id_wisata: str):
    data_objekWisata = get_data_objekWisata_from_web()
    for item in data_objekWisata:
        if item['id_wisata'] == id_wisata:
            return item
    raise HTTPException(status_code=404, detail="Objek Wisata not found")









# Model untuk Data government
class Government(BaseModel):
    nik: int
    kota: str

# Fungsi untuk mengambil data government dari web hosting lain
def get_data_government_from_web():
    url = "https://api-government.onrender.com/penduduk"  # Ganti dengan URL yang sebenarnya
    response = requests.get(url)    
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Gagal mengambil data government dari web hosting.")
# Endpoint untuk mendapatkan data government
@app.get("/government", response_model=List[Government])
def get_government():
    data_government = get_data_government_from_web()
    filtered_data = [item for item in data_government if item.get('nik') in [111, 112, 113, 114, 115]]
    return filtered_data

# Endpoint untuk mendapatkan data government berdasarkan nik
@app.get("/government/{nik}", response_model=Government)
def get_government_by_nik(nik: int):
    data_government = get_data_government_from_web()
    for item in data_government:
        if item['nik'] == nik:
            return item
    raise HTTPException(status_code=404, detail="Government data not found")








# Model untuk Data Rental Mobil
class RentalMobil(BaseModel):
    id_mobil: str
    merek: str
    nomor_polisi: str

# Fungsi untuk mengambil data rental mobil dari web hosting lain
def get_data_rental_mobil_from_web():
    url = "https://rental-mobil-api.onrender.com/mobil"  # Ganti dengan URL yang sebenarnya
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Gagal mengambil data rental mobil dari web hosting.")

# Endpoint untuk mendapatkan data rental mobil
@app.get("/rental_mobil", response_model=List[RentalMobil])
def get_rental_mobil():
    data_rental_mobil = get_data_rental_mobil_from_web()
    return data_rental_mobil
 
# Endpoint untuk mendapatkan data rental mobil berdasarkan id_mobil
@app.get("/rental_mobil/{id_mobil}", response_model=RentalMobil)
def get_rental_mobil_by_id(id_mobil: str):
    data_rental_mobil = get_data_rental_mobil_from_web()
    for item in data_rental_mobil:
        if item['id_mobil'] == id_mobil:
            return item
    raise HTTPException(status_code=404, detail="Rental Mobil not found")







# Fungsi untuk mengambil data bank dari web hosting lain
def get_data_bank_from_web():
    url = "https://jumantaradev.my.id/api/biro-tour/" # Ganti dengan URL yang sebenarnya
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['data']['data']
    else:
        raise HTTPException(status_code=response.status_code, detail="Gagal mengambil data BANK dari web hosting.")

# Model untuk Data Bank
class Bank(BaseModel):
    id: int
    saldo: int
    active_date: str
    expired_date: str

def get_bank_index(id):
    data_bank = get_data_bank_from_web()
    for index, bank in enumerate(data_bank):
        if bank['id'] == id:
            return index
    return None

@app.get("/bank", response_model=List[Bank])
def get_bank():
    data_bank = get_data_bank_from_web()
    return data_bank
# Endpoint untuk mendapatkan data bank berdasarkan id
@app.get("/bank/{id}", response_model=Optional[Bank])
def get_bank_by_id(id: int):
    data_bank = get_data_bank_from_web()
    for bank in data_bank:
        if bank['id'] == id:
            return Bank(**bank)
    return None


# # Fungsi untuk mengambil data hotel dari web hosting lain
# def get_data_hotel_from_web():
#     url = "https://hotelbaru.onrender.com/reviews"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()  
#     else:
#         raise HTTPException(status_code=response.status_code, detail="Gagal mengambil data HOTEL dari web hosting.")

# # Model untuk Data Hotel
# class Hotel(BaseModel):
#     ReviewID: str
#     ReservationID: str
#     Rating: int
#     Comment: str

# @app.get("/hotel", response_model=List[Hotel])
# def get_hotel():
#     data_hotel = get_data_hotel_from_web()
#     return data_hotel

# @app.get("/hotel/{RoomID}", response_model=Optional[Hotel])
#def get_hotel_by_id(RoomID: str):
#       if hotel['RoomID'] == RoomID:
#            return Hotel(**hotel)
#    return None

class guiderasuransi(BaseModel):
    id_asuransi : str
    id_guider : str
    premi : str
    tanggal_mulai_asuransi: str
    tanggal_selesai_asuransi: str

# Endpoint untuk mendapatkan data gabungan asuransi dan guider
@app.get('/Guider+Asuransi', response_model=List[guiderasuransi])
def get_asuransi_guider():
    data_asuransi = get_data_asuransi_from_web()

    # Menggunakan zip_longest untuk menggabungkan data asuransi dan data guider
    gabungan_data = []
    for tourguide, asuransi in zip_longest(data_tourguide, data_asuransi,  fillvalue={}):
        gabungan_data.append(guiderasuransi(
            id_asuransi=asuransi.get('id_asuransi', None),
            id_guider=tourguide.get('id_guider', None),
            premi=asuransi.get('premi', None),
            tanggal_mulai_asuransi=asuransi.get('tanggal_mulai_asuransi', None),
            tanggal_selesai_asuransi=asuransi.get('tanggal_selesai_asuransi', None) 
        ))
    return gabungan_data

@app.get('/Guider+Asuransi/{id_guider}', response_model=guiderasuransi)
def get_asuransi_guider_by_id(id_guider: str):
    data_asuransi = get_data_asuransi_from_web()

    # Menggunakan zip_longest untuk menggabungkan data asuransi dan data guider
    for tourguide, asuransi in zip_longest(data_tourguide, data_asuransi,  fillvalue={}):
        if tourguide.get('id_guider', None) == id_guider:
            return guiderasuransi(
                id_asuransi=asuransi.get('id_asuransi', None),
                id_guider=tourguide.get('id_guider', None),
                premi=asuransi.get('premi', None),
                tanggal_mulai_asuransi=asuransi.get('tanggal_mulai_asuransi', None),
                tanggal_selesai_asuransi=asuransi.get('tanggal_selesai_asuransi', None) 
            )
    return HTTPException(status_code=404, detail="Guider not found")










class guiderobjek(BaseModel):
    id_wisata : str
    id_guider : str
    nama_objek: str
    nama_daerah: str
    kategori: str
    alamat: str
    kontak: str
    harga_tiket: int

# Endpoint untuk mendapatkan data gabungan objek wisata dan guider
@app.get('/Guider+Objek', response_model=List[guiderobjek])
def get_objekWisata_guider():
    data_objekWisata = get_data_objekWisata_from_web()

    # Menggunakan zip_longest untuk menggabungkan data objek wisata dan data guider
    gabungan_data = []
    for tourguide, objek in zip_longest(data_tourguide, data_objekWisata,  fillvalue={}):
        gabungan_data.append(guiderobjek(
            id_wisata=objek.get('id_wisata', None),
            id_guider=tourguide.get('id_guider', None),
            nama_objek=objek.get('nama_objek', None),
            nama_daerah=objek.get('nama_daerah', None),
            kategori=objek.get('kategori', None),
            alamat=objek.get('alamat', None),
            kontak=objek.get('kontak', None),
            harga_tiket=objek.get('harga_tiket', None)
        ))
    return gabungan_data

@app.get('/Guider+Objek/{id_guider}', response_model=guiderobjek)
def get_objekWisata_guider_by_id(id_guider: str):
    data_objekWisata = get_data_objekWisata_from_web()

    # Menggunakan zip_longest untuk menggabungkan data asuransi dan data guider
    for tourguide, objek in zip_longest(data_tourguide, data_objekWisata,  fillvalue={}):
        if tourguide.get('id_guider', None) == id_guider:
            return guiderobjek(
                id_wisata=objek.get('id_wisata', None),
                id_guider=tourguide.get('id_guider', None),
                nama_objek=objek.get('nama_objek', None),
                nama_daerah=objek.get('nama_daerah', None),
                kategori=objek.get('kategori', None),
                alamat=objek.get('alamat', None),
                kontak=objek.get('kontak', None),
                harga_tiket=objek.get('harga_tiket', None)
            )
    return HTTPException(status_code=404, detail="Guider not found")







class guidergovern(BaseModel):
    id_guider : str
    nik:int
    kota:str

# Endpoint untuk mendapatkan data gabungan government dan guider
@app.get('/Guider+Government', response_model=List[guidergovern])
def get_government_guider():
    data_government = get_data_government_from_web()

    # Menggunakan zip_longest untuk menggabungkan data government dan data guider
    gabungan_data = []
    for tourguide, govern in zip_longest(data_tourguide, data_government,  fillvalue={}):
        gabungan_data.append(guidergovern(
            id_guider=tourguide.get('id_guider', None),
            nik=govern.get('nik', None),
            kota=govern.get('kota', None)
        ))
    return gabungan_data

@app.get('/Guider+Government/{id_guider}', response_model=guidergovern)
def get_government_guider_by_id(id_guider: str):
    data_government = get_data_government_from_web()

    # Menggunakan zip_longest untuk menggabungkan data government dan data guider
    for tourguide, govern in zip_longest(data_tourguide, data_government,  fillvalue={}):
        if tourguide.get('id_guider', None) == id_guider:
            return guidergovern(
                id_guider=tourguide.get('id_guider', None),
                nik=govern.get('nik', None),
                kota=govern.get('kota', None)
            )
    return HTTPException(status_code=404, detail="Guider not found")









class guiderrental(BaseModel):
    id_mobile: str
    id_guider: str
    merek: str
    nomor_polisi: str

# Endpoint untuk mendapatkan data gabungan objek wisata dan guider
@app.get('/Guider+Rental', response_model=List[guiderrental])
def get_rental_guider():
    data_rental_mobil = get_data_rental_mobil_from_web()

    # Menggunakan zip_longest untuk menggabungkan data objek wisata dan data guider
    gabungan_data = []
    for tourguide, rental in zip_longest(data_tourguide, data_rental_mobil,  fillvalue={}):
        gabungan_data.append(guiderrental(
            id_mobile=rental.get('id_mobil', None),
            id_guider=tourguide.get('id_guider', None),
            merek=rental.get('merek', None),
            nomor_polisi=rental.get('nomor_polisi', None)
        ))
    return gabungan_data

@app.get('/Guider+Rental/{id_guider}', response_model=guiderrental)
def get_rental_guider_by_id(id_guider: str):
    data_rental_mobil = get_data_rental_mobil_from_web()

    # Menggunakan zip_longest untuk menggabungkan data rental dan data guider
    for tourguide, rental in zip_longest(data_tourguide, data_rental_mobil,  fillvalue={}):
        if tourguide.get('id_guider', None) == id_guider:
            return guiderrental(
                id_mobile=rental.get('id_mobil', None),
                id_guider=tourguide.get('id_guider', None),
                merek=rental.get('merek', None),
                nomor_polisi=rental.get('nomor_polisi', None)
            )
    return HTTPException(status_code=404, detail="Guider not found")









class guiderbank(BaseModel):
    id: int
    id_guider: str
    saldo: int
    active_date: str
    expired_date: str

# Endpoint untuk mendapatkan data gabungan objek wisata dan guider
@app.get('/Guider+Bank', response_model=List[guiderbank])
def get_bank_guider():
    data_bank = get_data_bank_from_web()

    # Menggunakan zip_longest untuk menggabungkan data objek wisata dan data guider
    gabungan_data = []
    for tourguide, bank in zip_longest(data_tourguide, data_bank,  fillvalue={}):
        gabungan_data.append(guiderbank(
            id=bank.get('id', None),
            id_guider=tourguide.get('id_guider', None),
            saldo=bank.get('saldo', None),
            active_date=bank.get('active_date', None),
            expired_date=bank.get('expired_date', None)
    
        ))
    return gabungan_data

@app.get('/Guider+Bank/{id_guider}', response_model=guiderbank)
def get_bank_guider_by_id(id_guider: str):
    data_bank = get_data_bank_from_web()

    # Menggunakan zip_longest untuk menggabungkan data bank dan data guider
    for tourguide, bank in zip_longest(data_tourguide, data_bank,  fillvalue={}):
        if tourguide.get('id_guider', None) == id_guider:
            return guiderbank(
                id=bank.get('id', None),
                id_guider=tourguide.get('id_guider', None),
                saldo=bank.get('saldo', None),
                active_date=bank.get('active_date', None),
                expired_date=bank.get('expired_date', None)
            )
    return HTTPException(status_code=404, detail="Guider not found")