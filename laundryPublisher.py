# Library
import paho.mqtt.client as mqtt
import datetime
import time
import os
from tabulate import tabulate

# Function untuk publish data
def publishBojong(nama, berat, jenis_paket, jenisPaketWaktu):
    broker_address = 'localhost'
    client = mqtt.Client('Bojong', clean_session=False)
    client.connect(broker_address, port=3333)
    
    client.loop_start()
    print('Publish data to subscriber.')

    beratLaundry = float(berat)
    beratKg = str(berat) + ' Kg'
    if jenis_paket == 'Simpel':
        if(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundry * 5000)
            str_harga = str(int_harga)
        elif(jenisPaketWaktu == 'Premium'):
            int_harga = int(beratLaundry * 5000 + 1000)
            str_harga = str(beratLaundry * 5000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundry * 5000 + 2000)
            str_harga = str(beratLaundry * 5000) + ' + 2000 = ' + str((int_harga))

    elif jenis_paket == 'Dry':
        if(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundry * 7000)
            str_harga = str(int_harga)
        elif(jenisPaketWaktu == 'Premium'):
            int_harga = int(beratLaundry * 7000 + 1000)
            str_harga = str(beratLaundry * 7000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundry * 7000 + 2000)
            str_harga = str(beratLaundry * 7000) + ' + 2000 = ' + str((int_harga))

    elif jenis_paket == 'Komplit':
        if(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundry * 9000)
            str_harga = str(int_harga)
        elif(jenisPaketWaktu == 'Premium'):
            int_harga = int(beratLaundry * 9000 + 1000)
            str_harga = str(beratLaundry * 9000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundry * 9000 + 2000)
            str_harga = str(beratLaundry * 9000) + ' + 2000 = ' + str((int_harga))
    
    waktu = datetime.datetime.now()
    waktuPengajuan = waktu.strftime("%d/%m/%Y %H:%M:%S")

    if jenisPaketWaktu == 'Reguler':
        plus_hours = waktu + \
            datetime.timedelta(days=3)
        Pengembalian_Cucian = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))
    elif jenisPaketWaktu == 'Premium':
        plus_hours = waktu + \
            datetime.timedelta(days=2)
        Pengembalian_Cucian = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))
    elif jenisPaketWaktu == 'Express':
        plus_hours = waktu + \
            datetime.timedelta(days=1)
        Pengembalian_Cucian = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))

    # Mempublish data ke client
    client.publish('laundry', ''+nama+'|'+waktuPengajuan+'|'+jenis_paket+'|'
    +jenisPaketWaktu +'|'+beratKg+'|'+Pengembalian_Cucian+'|'+str_harga+'', qos=1, retain=False)

    client.loop_stop()

def publishSoang(nama, berat, jenis_paket, jenisPaketWaktu):
    broker_address = 'localhost'
    client = mqtt.Client('Soang', clean_session=False)
    client.connect(broker_address, port=3333)
    
    client.loop_start()
    print('Publish data to subscriber.')

    beratLaundrySoang = float(berat)
    beratKg = str(berat) + ' Kg'
    if jenis_paket == 'Simpel':
        if(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundrySoang * 6000)
            str_hargaSoang = str(int_harga)
        elif(jenisPaketWaktu == 'Premium'):
            int_harga = int(beratLaundrySoang * 6000 + 1000)
            str_hargaSoang = str(beratLaundrySoang * 6000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundrySoang * 6000 + 2000)
            str_hargaSoang = str(beratLaundrySoang * 6000) + ' + 2000 = ' + str((int_harga))

    elif jenis_paket == 'Dry':
        if(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundrySoang * 8000)
            str_hargaSoang = str(int_harga)
        elif(jenisPaketWaktu == 'Premium'):
            int_harga = int(beratLaundrySoang * 8000 + 1000)
            str_hargaSoang = str(beratLaundrySoang * 8000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundrySoang * 8000 + 2000)
            str_hargaSoang = str(beratLaundrySoang * 8000) + ' + 2000 = ' + str((int_harga))

    elif jenis_paket == 'Komplit':
        if(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundrySoang * 9000)
            str_hargaSoang = str(int_harga)
        elif(jenisPaketWaktu == 'Premium'):
            int_harga = int(beratLaundrySoang * 9000 + 1000)
            str_hargaSoang = str(beratLaundrySoang * 9000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundrySoang * 9000 + 2000)
            str_hargaSoang = str(beratLaundrySoang * 9000) + ' + 2000 = ' + str((int_harga))
    
    waktu = datetime.datetime.now()
    waktuPengajuanSoang = waktu.strftime("%d/%m/%Y %H:%M:%S")

    if jenisPaketWaktu == 'Reguler':
        plus_hours = waktu + \
            datetime.timedelta(days=3)
        Pengembalian_CucianSoang = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))
    elif jenisPaketWaktu == 'Premium':
        plus_hours = waktu + \
            datetime.timedelta(days=2)
        Pengembalian_CucianSoang = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))
    elif jenisPaketWaktu == 'Express':
        plus_hours = waktu + \
            datetime.timedelta(days=1)
        Pengembalian_CucianSoang = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))

    # Mempublish data ke client
    client.publish('laundry', ''+nama+'|'+waktuPengajuanSoang+'|'+jenis_paket+'|'+jenisPaketWaktu 
    +'|'+beratKg+'|'+Pengembalian_CucianSoang+'|'+str_hargaSoang+'', qos=1, retain=False)

    client.loop_stop()

def perbandingan(nama, berat, jenis_paket, jenisPaketWaktu):
    broker_address = 'localhost'
    client = mqtt.Client('bandingwaktu', clean_session=False)
    client.connect(broker_address, port=3333)
    
    client.loop_start()
    print('Publish data to subscriber.')

    beratLaundry = float(berat)

    if jenis_paket == 'Simpel':
        if(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundry * 5000)
            str_harga = str(int_harga)
        elif(jenisPaketWaktu == 'Premium'):
            int_harga = int(beratLaundry * 5000 + 1000)
            str_harga = str(beratLaundry * 5000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundry * 5000 + 2000)
            str_harga = str(beratLaundry * 5000) + ' + 2000 = ' + str((int_harga))

    elif jenis_paket == 'Dry':
        if(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundry * 7000)
            str_harga = str(int_harga)
        elif(jenisPaketWaktu == 'Premium'):
            int_harga = int(beratLaundry * 7000 + 1000)
            str_harga = str(beratLaundry * 7000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundry * 7000 + 2000)
            str_harga = str(beratLaundry * 7000) + ' + 2000 = ' + str((int_harga))

    elif jenis_paket == 'Komplit':
        if(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundry * 9000)
            str_harga = str(int_harga)
        elif(jenisPaketWaktu == 'Premium'):
            int_harga = int(beratLaundry * 9000 + 1000)
            str_harga = str(beratLaundry * 9000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundry * 9000 + 2000)
            str_harga = str(beratLaundry * 9000) + ' + 2000 = ' + str((int_harga))
    
    waktu = datetime.datetime.now()
    waktuPengajuan = waktu.strftime("%d/%m/%Y %H:%M:%S")

    if jenisPaketWaktu == 'Reguler':
        plus_hours = waktu + \
            datetime.timedelta(days=3)
        Pengembalian_Cucian = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))
    elif jenisPaketWaktu == 'Premium':
        plus_hours = waktu + \
            datetime.timedelta(days=2)
        Pengembalian_Cucian = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))
    elif jenisPaketWaktu == 'Express':
        plus_hours = waktu + \
            datetime.timedelta(days=1)
        Pengembalian_Cucian = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))
    
    
    #SOANG
    beratLaundry = float(berat)
    beratKg = str(berat) + ' Kg'
    if jenis_paket == 'Simpel':
        if(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundry * 6000)
            str_hargaSoang = str(int_harga)
        elif(jenisPaketWaktu == 'Premium'):
            int_harga = int(beratLaundry * 6000 + 1000)
            str_hargaSoang = str(beratLaundry * 6000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundry * 6000 + 2000)
            str_hargaSoang = str(beratLaundry * 6000) + ' + 2000 = ' + str((int_harga))

    elif jenis_paket == 'Dry':
        if(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundry * 8000)
            str_hargaSoang = str(int_harga)
        elif(jenisPaketWaktu == 'Premium'):
            int_harga = int(beratLaundry * 8000 + 1000)
            str_hargaSoang = str(beratLaundry * 8000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundry * 8000 + 2000)
            str_hargaSoang = str(beratLaundry * 8000) + ' + 2000 = ' + str((int_harga))

    elif jenis_paket == 'Komplit':
        if(jenisPaketWaktu == 'Reguler'):
            int_harga = int(beratLaundry * 9000)
            str_hargaSoang = str(int_harga)
        elif(jenisPaketWaktu == 'Premium'):
            int_harga = int(beratLaundry * 9000 + 1000)
            str_hargaSoang = str(beratLaundry * 9000) + ' + 1000 = ' + str((int_harga))
        elif(jenisPaketWaktu == 'Express'):
            int_harga = int(beratLaundry * 9000 + 2000)
            str_hargaSoang = str(beratLaundry * 9000) + ' + 2000 = ' + str((int_harga))
    
    waktu = datetime.datetime.now()
    waktuPengajuan = waktu.strftime("%d/%m/%Y %H:%M:%S")

    if jenisPaketWaktu == 'Reguler':
        plus_hours = waktu + \
            datetime.timedelta(days=3)
        Pengembalian_CucianSoang = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))
    elif jenisPaketWaktu == 'Premium':
        plus_hours = waktu + \
            datetime.timedelta(days=2)
        Pengembalian_CucianSoang = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))
    elif jenisPaketWaktu == 'Express':
        plus_hours = waktu + \
            datetime.timedelta(days=1)
        Pengembalian_CucianSoang = str(plus_hours.strftime("%d/%m/%Y %H:%M:%S"))

    client.publish('laundry', ''+'Laundry Bojong'+'|'+nama+'|'+waktuPengajuan+'|'+jenis_paket+'|'+jenisPaketWaktu 
    +'|'+beratKg+'|'+Pengembalian_Cucian+'|'+str_harga+'', qos=1, retain=False)
    client.publish('laundry', ''+'Laundry Soang'+'|'+nama+'|'+waktuPengajuan+'|'+jenis_paket+'|'+jenisPaketWaktu 
    +'|'+beratKg+'|'+Pengembalian_CucianSoang+'|'+str_hargaSoang+'', qos=1, retain=False)
    client.loop_stop()


def menu():
    status = True
    while status:
        print('+-------------------------------+')
        print("|      Publish KawaKawash       |")
        print(tabulate({'No': ['1','2','3','4'],
                        'Menu': ['Publish Laundry Bojong','Publish Laundry Soang','Perbandingan','Keluar']},
                        headers='keys',
                        tablefmt='grid'))
        
        pilihan = input("Masukan pilihan anda : ")
        
        if pilihan == "1":
            nama, berat, jenis_paket, jenisPaketWaktu = menuLaundry()
            publishBojong(nama, berat, jenis_paket, jenisPaketWaktu)

        elif pilihan == "2":
            nama, berat, jenis_paket, jenisPaketWaktu = menuLaundrySoang()
            publishSoang(nama, berat, jenis_paket, jenisPaketWaktu)

        elif pilihan == "3":
            nama, berat, jenis_paket, jenisPaketWaktu = menuLaundry()
            perbandingan(nama, berat, jenis_paket, jenisPaketWaktu)
        elif pilihan == "4":
            print("Anda keluar dari program")
            status = False
        else:
            print("Yang Anda masukan salah silahkan coba lagi")
            time.sleep(2)
            os.system('cls')
            menu()

def menuLaundry():
    status = True
    l = []
    while status:
        os.system('cls')
        print("+-----------------------------------------------------------------------+")
        print("|                        Masukan Data Laundry                           |")
        print(tabulate({'Paket Layanan': ['Paket Simpel : Rp 5000,-/kg','Paket Dry    : Rp 7000,-/kg','Paket Komplit: Rp 9000,-/kg'],
                        'Paket Waktu': ['Reguler (3 Hari Pengerjaan)','Premium (2 Hari Pengerjaan) + Rp 1000,-','Express (1 Hari Pengerjaan) + Rp 2000,-']},
                        headers='keys',
                        tablefmt='grid'))

        nama = input('Nama: ')
        berat = input('Berat: ')
        Jenis_paket = input('Jenis Paket (Simpel), (Dry), (Komplit): ')
        jenisPaketWaktu = input('Jenis Paket Waktu (Reguler), (Premium), (Express): ')
        
        if Jenis_paket == 'Simpel':
            if jenisPaketWaktu == 'Reguler':
                l = [nama, berat, 'Simpel', 'Reguler']
            elif jenisPaketWaktu == 'Premium':
                l = [nama, berat, 'Simpel', 'Premium']
            elif jenisPaketWaktu == 'Express':
                l = [nama, berat, 'Simpel', 'Express']
        elif Jenis_paket == 'Dry':
            if jenisPaketWaktu == 'Reguler':
                l = [nama, berat, 'Dry', 'Reguler']
            elif jenisPaketWaktu == 'Premium':
                l = [nama, berat, 'Dry', 'Premium']
            elif jenisPaketWaktu == 'Express':
                l = [nama, berat, 'Dry', 'Express']
        elif Jenis_paket == 'Komplit':
            if jenisPaketWaktu == 'Reguler':
                l = [nama, berat, 'Komplit', 'Reguler']
            elif jenisPaketWaktu == 'Premium':
                l = [nama, berat, 'Komplit', 'Premium']
            elif jenisPaketWaktu == 'Express':
                l = [nama, berat, 'Komplit', 'Express']
        else:
            print("Yang Anda masukan salah silahkan coba lagi")
            status = True
            time.sleep(2)
            os.system('cls')
            menu()
        return l

def menuLaundrySoang():
    status = True
    l = []
    while status:
        os.system('cls')
        print("+---------------------------------------------------+")
        print("|              Masukan Data Laundry                 |")
        print(tabulate({'Paket Layanan': ['Paket Simpel : Rp 6000,-/kg','Paket Dry    : Rp 8000,-/kg','Paket Komplit: Rp 9000,-/kg'],
                        'Paket Waktu': ['Reguler','Premium + Rp 1000,-','Express + Rp 2000,-']},
                        headers='keys',
                        tablefmt='grid'))

        nama = input('Nama: ')
        berat = input('Berat: ')
        Jenis_paket = input('Jenis Paket (Simpel), (Dry), (Komplit): ')
        jenisPaketWaktu = input('Jenis Paket Waktu (Reguler), (Premium), (Express): ')
        
        if Jenis_paket == 'Simpel':
            if jenisPaketWaktu == 'Reguler':
                l = [nama, berat, 'Simpel', 'Reguler']
            elif jenisPaketWaktu == 'Premium':
                l = [nama, berat, 'Simpel', 'Premium']
            elif jenisPaketWaktu == 'Express':
                l = [nama, berat, 'Simpel', 'Express']
        elif Jenis_paket == 'Dry':
            if jenisPaketWaktu == 'Reguler':
                l = [nama, berat, 'Dry', 'Reguler']
            elif jenisPaketWaktu == 'Premium':
                l = [nama, berat, 'Dry', 'Premium']
            elif jenisPaketWaktu == 'Express':
                l = [nama, berat, 'Dry', 'Express']
        elif Jenis_paket == 'Komplit':
            if jenisPaketWaktu == 'Reguler':
                l = [nama, berat, 'Komplit', 'Reguler']
            elif jenisPaketWaktu == 'Premium':
                l = [nama, berat, 'Komplit', 'Premium']
            elif jenisPaketWaktu == 'Express':
                l = [nama, berat, 'Komplit', 'Express']
        else:
            print("Yang Anda masukan salah silahkan coba lagi")
            status = True
            time.sleep(2)
            os.system('cls')
            menu()
        return l
os.system('cls')
menu()