import paho.mqtt.client as mqtt
import time
import os
from IPython.display import clear_output
from tabulate import tabulate

#Function untuk menampilkan menu dalam tabel
def menu():
    print(tabulate({'No': ['1','2','3','4'],
                    'Menu': ['Subscribe Laundry Bojong','Subscribe Laundry Soang','Perbandingan','Keluar']},
                    headers='keys',
                    tablefmt='grid'))

def laundryBojong():
    arrBojong = []
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Client is connected to Laundry Bojong")
        else:
            print("Connected Failed")
    def on_message(client, userdata, message):
        data = str(message.payload.decode('utf-8')).split('|')
        arrBojong.append(data)
        clear_output(wait=True)
        os.system('cls')
        index = range(1, len(arrBojong)+1)
        print("Tagihan laundry Bojong")
        print(tabulate(arrBojong, headers=['Nama', 'Tanggal Input', 'Jenis Layanan', 'Jenis Paket Waktu', 'Berat', 'Pengembalian Cucian', 
        'Total Harga'], tablefmt='pretty', showindex=index))
    broker_address = 'localhost'
    client = mqtt.Client('laundrybojong', clean_session=True)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_address, port=3333)
    client.loop_start()
    client.subscribe('laundry', qos=1)
    while True:
        time.sleep(1)
    client.loop_stop()

def laundrySoang():
    arrSoang = []
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Client is connected to Laundry Soang")
        else:
            print("Connected Failed")
    def on_message(client, userdata, message):
        data = str(message.payload.decode('utf-8')).split('|')
        arrSoang.append(data)
        os.system('cls')
        clear_output(wait=True)
        index = range(len(arrSoang))
        print("Tagihan laundry Soang")
        print(tabulate(arrSoang, headers=['Nama', 'Tanggal Input', 'Jenis Layanan', 'Jenis Paket Waktu', 'Berat', 'Pengembalian Cucian', 
        'Total Harga'], tablefmt='pretty', showindex=index))
    broker_address = 'localhost'
    client = mqtt.Client('laundrysoang', clean_session=True)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_address, port=3333)
    client.loop_start()
    client.subscribe('laundry', qos=1)
    while True:
        time.sleep(1)
    client.loop_stop()

def perbandingan():
    arrBanding = []
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Client is connected to Perbandingan Laundry")
        else:
            print("Connected Failed")
    def on_message(client, userdata, message):
        data = str(message.payload.decode('utf-8')).split('|')
        arrBanding.append(data)
        clear_output(wait=True)
        os.system('cls')
        index = range(len(arrBanding))
        print("Tagihan Data laundry Perbandingan")
        print(tabulate(arrBanding, headers=['Nama', 'Tanggal Input', 'Jenis Layanan', 'Jenis Paket Waktu', 'Berat', 'Pengembalian Cucian', 'Total Harga'], 
            tablefmt='pretty', showindex=index))
    broker_address = 'localhost'
    client = mqtt.Client('BandingWaktu', clean_session=True)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_address, port=3333)
    client.loop_start()
    client.subscribe('laundry', qos=1)
    while True:
        time.sleep(1)
    client.loop_stop()

os.system('cls')
menu()
status = True
while status:
    inputan = int(input('Masukan pilihan anda : '))
    if inputan == 1:
        laundryBojong()
    elif inputan == 2:
        laundrySoang()
    elif inputan == 3:
        perbandingan()
    elif inputan == 4:
        status = False
        print("Anda keluar dari program")
        exit()        
    else:
        print("Yang Anda masukan salah silahkan coba lagi")
        time.sleep(2)
        os.system('cls')
        menu()