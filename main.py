
import requests
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI(
    title="MC Tour Guide",
    description="API TOUR GUIDE",
    docs_url="/",  # Ubah docs_url menjadi "/"
)

@app.get("/")
async def read_root():
    return {"Data":"Successful"}

# Model untuk Data tour guide
class Tourguide(BaseModel):
    id_guider: str
    nama_guider: str
    profile: str
    no_hp: str
    fee: int
    history: int
    feedback: int
    bank: str
    status_ketersediaan: str

# Dummy data untuk tourguide
data_tourguide = [
    {"id_guider": "111", "nama_guider": "Chadkowi", "profile": "Seorang pemandu wisata berpengalaman dengan kecintaan pada petualangan alam yang menawarkan pengalaman mendaki gunung dan menjelajahi hutan yang luas.", "no_hp": "911", "fee": 200000, "history": 54, "feedback": 10, "bank": "GARIS", "status_ketersediaan": "Bisa"},
    {"id_guider": "112", "nama_guider": "Prabroro", "profile": " Seorang pemandu wisata yang ahli dalam memperkenalkan budaya lokal dan sejarah di setiap destinasi.", "no_hp": "119", "fee": 400000, "history": 56, "feedback": 10, "bank": "LAUT BANK", "status_ketersediaan": "Bisa"},
    {"id_guider": "113", "nama_guider": "Anisa", "profile": "Seorang pemandu wisata yang mengutamakan pengalaman mewah dan layanan berkualitas tinggi, memastikan setiap perjalanan menjadi pengalaman yang istimewa", "no_hp": "919", "fee": 500000, "history": 47, "feedback": 10, "bank": "BANG JAGO", "status_ketersediaan": "Bisa"},
    {"id_guider": "114", "nama_guider": "Janggar", "profile": "Seorang pemandu wisata yang ramah keluarga dengan keahlian dalam merencanakan liburan yang menyenangkan bagi seluruh anggota keluarga.", "no_hp": "119", "fee": 450000, "history": 100, "feedback": 9, "bank": "MANDIRI", "status_ketersediaan": "Bisa"},
    {"id_guider": "115", "nama_guider": "Mahfud DM", "profile": "mampu menjelaskan seluk beluk tempat-tempat yang dikunjungi saat perjalanan wisata.", "no_hp": "991", "fee": 300000, "history": 48, "feedback": 9, "bank": "BINI", "status_ketersediaan": "Bisa"}
]

# Endpoint untuk menambahkan data tourguide
@app.post("/tourguide")
def tambah_tourguide(tourguide: Tourguide):
    data_tourguide.append(tourguide.dict())
    return {"message": "Data wisata berhasil ditambahkan."}

# Endpoint untuk mendapatkan data tourguide
@app.get("/tourguide", response_model=List[Tourguide])
def get_tourguide():
    return data_tourguide

# Fungsi untuk mengambil data asuransi dari web hosting lain
def get_data_asuransi_from_web():
    url = "https://example.com/api/pajak"  # Ganti dengan URL yang sebenarnya
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Gagal mengambil data Asuransi dari web hosting.")

# Model untuk Data Asuransi
class Asuransi(BaseModel):
    id_pajak: int
    jenis_pajak: str
    tarif_pajak: float
    besar_pajak: float

# Endpoint untuk mendapatkan data Asuransi
@app.get("/asuransi", response_model=List[Asuransi])
def get_asuransi():
    data_asuransi = get_data_asuransi_from_web()
    return data_asuransi

# Fungsi untuk mengambil data objek wisata dari web hosting lain
def get_data_objekWisata_from_web():
    url = "https://pajakobjekwisata.onrender.com/wisata"  # Ganti dengan URL yang sebenarnya
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Gagal mengambil data OBJEK WISATA dari web hosting.")

# Model untuk Data Objek Wisata
class ObjekWisata(BaseModel):
    id_wisata: str
    nama_objek: str
    nama_daerah: str
    kategori: str
    alamat: str
    kontak: str
    harga_tiket: int

# Endpoint untuk mendapatkan data objek wisata
@app.get("/objekWisata", response_model=List[ObjekWisata])
def get_objekWisata():
    data_objekWisata = get_data_objekWisata_from_web()
    return data_objekWisata


# Fungsi untuk mengambil data government dari web hosting lain
def get_data_government_from_web():
    url = "https://example.com/api/pajak"  # Ganti dengan URL yang sebenarnya
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Gagal mengambil data GOVERNMENT dari web hosting.")



# Model untuk Data government
class Government(BaseModel):
    id_asuransi: int
    nama_wisata: str
    profile: str

# dpoint untuk mendapatkan data government
@app.get("/government", response_model=List[Government])
def get_government():
    data_government = get_data_government_from_web()
    return data_government

# # Fungsi untuk mengambil data hotel dari web hosting lain
# def get_data_hotel_from_web():
#     url = "https://example.com/api/pajak"  # Ganti dengan URL yang sebenarnya
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise HTTPException(status_code=response.status_code, detail="Gagal mengambil data HOTEL dari web hosting.")

# # Model untuk Data Hotel
# class Hotel(BaseModel):
#     id_room: int
#     room_number: int
#     room_type: str
#     rate: str
#     availability: int

# # Endpoint untuk mendapatkan data hotel
# @app.get("/hotel", response_model=List[Hotel])
# def get_hotel():
#     data_hotel = get_data_hotel_from_web()
#     return data_hotel

# Fungsi untuk mengambil data bank dari web hosting lain
def get_data_bank_from_web():
    url = "https://undelaying-semaphor.000webhostapp.com/"  # Ganti dengan URL yang sebenarnya
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Gagal mengambil data BANK dari web hosting.")

# Model untuk Data Bank
class Bank(BaseModel):
    id_transaksi: int
    nama: str
    kabupaten: str

# Endpoint untuk mendapatkan data bank
@app.get("/bank", response_model=List[Bank])
def get_bank():
    data_bank = get_data_bank_from_web()
    return data_bank


# Fungsi untuk menggabungkan data tour guide dan objek wisata
def combine_tour_guide_objekwisata():
    tour_guide_data = get_tourguide()
    objekwisata_data = get_objekWisata()

    combined_data = []
    for tour_guide in tour_guide_data:
        for objekwisata in objekwisata_data:
            combined_obj = {
                "id_guider": tour_guide['id_guider'],
                "objekwisata": objekwisata
            }
            combined_data.append(combined_obj)

    return combined_data

class TourGuideObjekWisata(BaseModel):
    id_guider: str
    objekwisata: ObjekWisata

# Endpoint untuk mendapatkan data gabungan tour guide dan objek wisata
@app.get("/Guider+Objek", response_model=List[TourGuideObjekWisata])
def get_combined_data():
    combined_data = combine_tour_guide_objekwisata()
    return combined_data


# Fungsi untuk menggabungkan data tour guide dan bank
# Function to combine tour guide and bank data
def combine_tour_guide_bank():
    tour_guide_data = get_tourguide()
    bank_data = get_bank()

    combined_data = []
    for tour_guide in tour_guide_data:
        for bank in bank_data:
            combined_obj = {
                "id_guider": tour_guide['id_guider'],
                "bank": bank
            }
            combined_data.append(combined_obj)

    return combined_data

class TourGuideBank(BaseModel):
    id_guider: str
    bank: Bank

# Endpoint untuk mendapatkan data gabungan tour guide dan bank
@app.get("/combined", response_model=List[TourGuideBank])
def get_combined_data():
    combined_data = combine_tour_guide_bank()
    return combined_data
