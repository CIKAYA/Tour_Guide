import requests
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="MC Tour Guide",
    description="API TOUR GUIDE",
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
        data = response.json()
        return [Asuransi(**item) for item in data]
    else:
        raise HTTPException(status_code=response.status_code, detail="Gagal mengambil data asuransi dari web hosting.")

# Endpoint to get insurance data
@app.get("/asuransi", response_model=List[Asuransi])
def get_asuransi():
    data_asuransi = get_data_asuransi_from_web()
    return data_asuransi

# Endpoint to get insurance data by id_guider
@app.get("/asuransi/{id_guider}", response_model=List[Asuransi])
def get_asuransi_by_id_guider(id_guider: str):
    data_asuransi = get_data_asuransi_from_web()
    filtered_data = [item for item in data_asuransi if item.id_asuransi == id_guider]
    if filtered_data:
        return filtered_data
    raise HTTPException(status_code=404, detail="Data asuransi tidak ditemukan untuk id_guider tersebut.")

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
        data = response.json()
        return [ObjekWisata(**item) for item in data]
    else:
        raise HTTPException(status_code=response.status_code, detail="Gagal mengambil data objek wisata dari web hosting.")

# Endpoint untuk mendapatkan data objek wisata
@app.get("/objekWisata", response_model=List[ObjekWisata])
def get_objekWisata():
    data_objekWisata = get_data_objekWisata_from_web()
    return data_objekWisata

# Endpoint untuk mendapatkan data objek wisata berdasarkan id_guider
@app.get("/objekWisata/{id_guider}", response_model=List[ObjekWisata])
def get_objekWisata_by_id_guider(id_guider: str):
    data_objekWisata = get_data_objekWisata_from_web()
    filtered_data = [item for item in data_objekWisata if item.id_wisata == id_guider]
    if filtered_data:
        return filtered_data
    raise HTTPException(status_code=404, detail="Data objek wisata tidak ditemukan untuk id_guider tersebut.")

# Model untuk Data government
class Government(BaseModel):
    nik: int
    kota: str

# Fungsi untuk mengambil data government dari web hosting lain
def get_data_government_from_web():
    url = "https://api-government.onrender.com/penduduk"  # Ganti dengan URL yang sebenarnya
    response = requests.get(url)    
    if response.status_code == 200:
        data = response.json()
        return [Government(**item) for item in data]
    else:
        raise HTTPException(status_code=response.status_code, detail="Gagal mengambil data government dari web hosting.")

# Endpoint untuk mendapatkan data government
@app.get("/government", response_model=List[Government])
def get_government():
    data_government = get_data_government_from_web()
    filtered_data = [item for item in data_government if item.nik in [111, 112, 113, 114, 115]]
    return filtered_data

# Endpoint untuk mendapatkan data government berdasarkan id_guider
@app.get("/government/{id_guider}", response_model=List[Government])
def get_government_by_id_guider(id_guider: str):
    data_government = get_data_government_from_web()
    filtered_data = [item for item in data_government if str(item.id_asuransi) == id_guider]
    if filtered_data:
        return filtered_data
    raise HTTPException(status_code=404, detail="Data government tidak ditemukan untuk id_guider tersebut.")

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
        data = response.json()
        return [RentalMobil(**item) for item in data]
    else:
        raise HTTPException(status_code=response.status_code, detail="Gagal mengambil data rental mobil dari web hosting.")

# Endpoint untuk mendapatkan data rental mobil
@app.get("/rental_mobil", response_model=List[RentalMobil])
def get_rental_mobil():
    data_rental_mobil = get_data_rental_mobil_from_web()
    return data_rental_mobil

# Endpoint untuk mendapatkan data rental mobil berdasarkan id_guider
@app.get("/rental_mobil/{id_guider}", response_model=List[RentalMobil])
def get_rental_mobil_by_id_guider(id_guider: str):
    data_rental_mobil = get_data_rental_mobil_from_web()
    filtered_data = [item for item in data_rental_mobil if item.id_mobil == id_guider]
    if filtered_data:
        return filtered_data
    raise HTTPException(status_code=404, detail="Data rental mobil tidak ditemukan untuk id_guider tersebut.")

# Model untuk Data Bank


# Fungsi untuk mengambil data bank dari web hosting lain
def get_data_bank_from_web():
    url = "https://jumantaradev.my.id/api/biro-tour"  # Ganti dengan URL yang sebenarnya
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['data']['data']
    else:
        raise HTTPException(status_code=response.status_code, detail="Gagal mengambil data BANK dari web hosting.")

# Model untuk Data Bank
class Bank(BaseModel):
    id: int
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

# Endpoint untuk mendapatkan data bank berdasarkan id_guider
@app.get("/bank/{id_guider}", response_model=List[Bank])
def get_bank_by_id_guider(id_guider: str):
    data_bank = get_data_bank_from_web()
    filtered_data = [item for item in data_bank if str(item.id_transaksi) == id_guider]
    if filtered_data:
        return filtered_data
    raise HTTPException(status_code=404, detail="Data bank tidak ditemukan untuk id_guider tersebut.")

def combine_guider_wisata():
    guider_data = get_tourguide()
    wisata_data = get_data_objekWisata_from_web()

    

    combined_data = [
        {
            "id_guider": tourguide['id_guider'],
            "objekWisata": objek_wisata
        }
        for tourguide in guider_data
        for objek_wisata in wisata_data
    ]

    return combined_data

class GuiderWisata(BaseModel):
    id_guider: str
    objekWisata: ObjekWisata

@app.get("/GuiderWisata", response_model=List[GuiderWisata])
def get_combined_data():
    combined_data = combine_guider_wisata()
    return [GuiderWisata(**data) for data in combined_data]