#lets start
saldo = 100000

ulang = "ya"
while ulang == "ya":
    nama = input("Masukkan Nama Anda : ")
    pin = input("Masukkan PIN Anda : ")
    usia = input("Berapa Usia Anda : ")
    
    print()
    toko = "====================WELCOME TO E-Naq====================="
    
    import datetime
    waktu = datetime.datetime.now()
    
    print(waktu)
    #print(x.year)
    #print(x.strftime("%H"))
    
    jam = int(waktu.strftime("%H"))

    if pin == "1111" and int(usia) <= 16 and int(saldo) >= 35000 :
        if jam >= 0 and jam <= 10 :
            pagi = "Selamat pagi"
            print (pagi, "Adik", nama) 
            print("Kamu memiliki saldo sebanyak Rp", saldo)
            print()
            print (toko)
            print("=========================================================")
            print("=============BERIKUT MENU YANG KAMI SEDIAKAN=============")
            paket_1 = "1 Cheseburger +  1 French fries + 1 Cola"
            paket_2 = "1 Kebab Mozarella + 1 French fries + 1 Cola"
            print("=========================================================")
            print("1.", paket_1, "Rp 35.000")
            print("2.", paket_2, "Rp 30.000")
            print("=========================================================")
            paket = input ("Kamu mau paket yang mana (1/2): ")
            if paket == "1" :
                print("Kamu memilih paket 1 seharga Rp35.000")
                tanya = input("Kamu memiliki voucher discount? (ya/tidak) : ")
                if tanya == "ya":
                    vouc = input("Silahkan masukkan kode vouchermu : ")
                    print()
                    if vouc == "1234":
                        harga = 35000
                        disc = int(harga) * 0.15
                        bayar = int(harga) - int(disc)
                        saldo = int(saldo) - int(bayar)
                        print("Selamat, voucher kamu berhasil diaktifkan")
                        print("=========================================================")
                        print("Kamu mendapat potongan sebesar 15%")
                        print("Kamu hanya membayar sebanyak Rp", bayar)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kamu ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                    else :
                        harga = 35000
                        saldo = int(saldo) - int(harga)
                        print("=========================================================")
                        print("Mohon maaf, kode yang kamu masukkan salah")
                        print("Kamu membayar sebanyak Rp", harga)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kamu ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                else :
                    harga = 35000
                    saldo = int(saldo) - int(harga)
                    print("=========================================================")
                    print("Kamu membayar sebanyak Rp", harga)
                    print("Sisa saldo : Rp", saldo)
                    print("=========================================================")
                    ulang = input("Kamu ingin Membeli lagi ? (ya/tidak) : ")
                    if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
            elif paket == "2" :
                print("Kamu memilih paket 2 seharga Rp30.000")
                tanya = input("Kamu memiliki voucher discount? (ya/tidak) : ")
                if tanya == "ya":
                    vouc = input("Silahkan masukkan kode vouchermu : ")
                    print()
                    if vouc == "1234":
                        harga = 30000
                        disc = int(harga) * 0.15
                        bayar = int(harga) - int(disc)
                        saldo = int(saldo) - int(bayar)
                        print("Selamat, voucher kamu berhasil diaktifkan")
                        print("=========================================================")
                        print("Kamu mendapat potongan sebesar 15%")
                        print("Kamu hanya membayar sebanyak Rp", bayar)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kamu ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                    else :
                        harga = 30000
                        saldo = int(saldo) - int(harga)
                        print("=========================================================")
                        print("Mohon maaf, kode yang kamu masukkan salah")
                        print("Kamu membayar sebanyak Rp", harga)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kamu ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                else :
                    harga = 30000
                    saldo = int(saldo) - int(harga)
                    print("=========================================================")
                    print("Kamu membayar sebanyak Rp", harga)
                    print("Sisa saldo : Rp", saldo)
                    print("=========================================================")
                    ulang = input("Kamu ingin Membeli lagi ? (ya/tidak) : ")
                    if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
            else :
                print("Mohon maaf, paket tidak tersedia")
                print("Silahkan memilih paket 1/2")
                ulang = input("Kamu ingin mencoba lagi ? (ya/tidak) : ")
                if ulang == "tidak":
                    print("=========================================================")
                    print("=======================TERIMA KASIH======================")
                    print("=========================================================")
        elif jam >=11 and jam <=18 :
            siang = "Selamat Siang"
            print (siang, "Adik", nama)
            print("Kamu memiliki saldo sebanyak Rp", saldo)
            print()
            print (toko)
            print("=========================================================")
            print("=============BERIKUT MENU YANG KAMI SEDIAKAN=============")
            paket_1 = "1 Cheseburger +  1 French fries + 1 Cola"
            paket_2 = "1 Kebab Mozarella + 1 French fries + 1 Cola"
            print("=========================================================")
            print("1.", paket_1, "Rp 35.000")
            print("2.", paket_2, "Rp 30.000")
            print("=========================================================")
            paket = input ("Kamu mau paket yang mana (1/2): ")
            if paket == "1" :
                print("Kamu memilih paket 1 seharga Rp35.000")
                tanya = input("Kamu memiliki voucher discount? (ya/tidak) : ")
                if tanya == "ya":
                    vouc = input("Silahkan masukkan kode vouchermu : ")
                    print()
                    if vouc == "1234":
                        harga = 35000
                        disc = int(harga) * 0.15
                        bayar = int(harga) - int(disc)
                        saldo = int(saldo) - int(bayar)
                        print("Selamat, voucher kamu berhasil diaktifkan")
                        print("=========================================================")
                        print("Kamu mendapat potongan sebesar 15%")
                        print("Kamu hanya membayar sebanyak Rp", bayar)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kamu ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                    else :
                        harga = 35000
                        saldo = int(saldo) - int(harga)
                        print("=========================================================")
                        print("Mohon maaf, kode yang kamu masukkan salah")
                        print("Kamu membayar sebanyak Rp", harga)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kamu ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                else :
                    harga = 35000
                    saldo = int(saldo) - int(harga)
                    print("=========================================================")
                    print("Kamu membayar sebanyak Rp", harga)
                    print("Sisa saldo : Rp", saldo)
                    print("=========================================================")
                    ulang = input("Kamu ingin Membeli lagi ? (ya/tidak) : ")
                    if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
            elif paket == "2" :
                print("Kamu memilih paket 2 seharga Rp30.000")
                tanya = input("Kamu memiliki voucher discount? (ya/tidak) : ")
                if tanya == "ya":
                    vouc = input("Silahkan masukkan kode vouchermu : ")
                    print()
                    if vouc == "1234":
                        harga = 30000
                        disc = int(harga) * 0.15
                        bayar = int(harga) - int(disc)
                        saldo = int(saldo) - int(bayar)
                        print("Selamat, voucher kamu berhasil diaktifkan")
                        print("=========================================================")
                        print("Kamu mendapat potongan sebesar 15%")
                        print("Kamu hanya membayar sebanyak Rp", bayar)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kamu ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                    else :
                        harga = 30000
                        saldo = int(saldo) - int(harga)
                        print("=========================================================")
                        print("Mohon maaf, kode yang kamu masukkan salah")
                        print("Kamu membayar sebanyak Rp", harga)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kamu ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                else :
                    harga = 30000
                    saldo = int(saldo) - int(harga)
                    print("=========================================================")
                    print("Kamu membayar sebanyak Rp", harga)
                    print("Sisa saldo : Rp", saldo)
                    print("=========================================================")
                    ulang = input("Kamu ingin Membeli lagi ? (ya/tidak) : ")
                    if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
            else :
                print("Mohon maaf, paket tidak tersedia")
                print("Silahkan memilih paket 1/2")
                ulang = input("Kamu ingin mencoba lagi ? (ya/tidak) : ")
                if ulang == "tidak":
                    print("=========================================================")
                    print("=======================TERIMA KASIH======================")
                    print("=========================================================")
        elif jam >= 19 and jam <= 24 :
            malam = "Selamat Malam"
            print (malam, "Adik", nama)
            print("Kamu memiliki saldo sebanyak Rp", saldo)
            print()
            print (toko)
            print("=========================================================")
            print("=============BERIKUT MENU YANG KAMI SEDIAKAN=============")
            paket_1 = "1 Cheseburger +  1 French fries + 1 Cola"
            paket_2 = "1 Kebab Mozarella + 1 French fries + 1 Cola"
            print("=========================================================")
            print("1.", paket_1, "Rp 35.000")
            print("2.", paket_2, "Rp 30.000")
            print("=========================================================")
            paket = input ("Kamu mau paket yang mana (1/2): ")
            if paket == "1" :
                print("Kamu memilih paket 1 seharga Rp35.000")
                tanya = input("Kamu memiliki voucher discount? (ya/tidak) : ")
                if tanya == "ya":
                    vouc = input("Silahkan masukkan kode vouchermu : ")
                    print()
                    if vouc == "1234":
                        harga = 35000
                        disc = int(harga) * 0.15
                        bayar = int(harga) - int(disc)
                        saldo = int(saldo) - int(bayar)
                        print("Selamat, voucher kamu berhasil diaktifkan")
                        print("=========================================================")
                        print("Kamu mendapat potongan sebesar 15%")
                        print("Kamu hanya membayar sebanyak Rp", bayar)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kamu ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                    else :
                        harga = 35000
                        saldo = int(saldo) - int(harga)
                        print("=========================================================")
                        print("Mohon maaf, kode yang kamu masukkan salah")
                        print("Kamu membayar sebanyak Rp", harga)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kamu ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                else :
                    harga = 35000
                    saldo = int(saldo) - int(harga)
                    print("=========================================================")
                    print("Kamu membayar sebanyak Rp", harga)
                    print("Sisa saldo : Rp", saldo)
                    print("=========================================================")
                    ulang = input("Kamu ingin Membeli lagi ? (ya/tidak) : ")
                    if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
            elif paket == "2" :
                print("Kamu memilih paket 2 seharga Rp30.000")
                tanya = input("Kamu memiliki voucher discount? (ya/tidak) : ")
                if tanya == "ya":
                    vouc = input("Silahkan masukkan kode vouchermu : ")
                    print()
                    if vouc == "1234":
                        harga = 30000
                        disc = int(harga) * 0.15
                        bayar = int(harga) - int(disc)
                        saldo = int(saldo) - int(bayar)
                        print("Selamat, voucher kamu berhasil diaktifkan")
                        print("=========================================================")
                        print("Kamu mendapat potongan sebesar 15%")
                        print("Kamu hanya membayar sebanyak Rp", bayar)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kamu ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                    else :
                        harga = 30000
                        saldo = int(saldo) - int(harga)
                        print("=========================================================")
                        print("Mohon maaf, kode yang kamu masukkan salah")
                        print("Kamu membayar sebanyak Rp", harga)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kamu ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                else :
                    harga = 30000
                    saldo = int(saldo) - int(harga)
                    print("=========================================================")
                    print("Kamu membayar sebanyak Rp", harga)
                    print("Sisa saldo : Rp", saldo)
                    print("=========================================================")
                    ulang = input("Kamu ingin Membeli lagi ? (ya/tidak) : ")
                    if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
            else :
                print("Mohon maaf, paket tidak tersedia")
                print("Silahkan memilih paket 1/2")
                ulang = input("Kamu ingin mencoba lagi ? (ya/tidak) : ")
                if ulang == "tidak":
                    print("=========================================================")
                    print("=======================TERIMA KASIH======================")
                    print("=========================================================")
    elif pin == "1111" and int(usia) > 16 and int(usia) <= 35 and int(saldo) >= 35000 :
        if jam >= 0 and jam <= 10 :
            pagi = "Selamat pagi"
            print (pagi, "Kak", nama)
            print("Kakak memiliki saldo sebanyak Rp", saldo)
            print()
            print (toko)
            print("=========================================================")
            print("=============BERIKUT MENU YANG KAMI SEDIAKAN=============")
            paket_1 = "1 Cheseburger +  1 French fries + 1 Cola"
            paket_2 = "1 Kebab Mozarella + 1 French fries + 1 Cola"
            print("=========================================================")
            print("1.", paket_1, "Rp 35.000")
            print("2.", paket_2, "Rp 30.000")
            print("=========================================================")
            paket = input ("Kakak mau paket yang mana (1/2): ")
            if paket == "1" :
                print("Kakak memilih paket 1 seharga Rp35.000")
                tanya = input("Kakak memiliki voucher discount? (ya/tidak) : ")
                if tanya == "ya":
                    vouc = input("Silahkan masukkan kode voucher kakak : ")
                    print()
                    if vouc == "1234":
                        harga = 35000
                        disc = int(harga) * 0.15
                        bayar = int(harga) - int(disc)
                        saldo = int(saldo) - int(bayar)
                        print("Selamat, voucher kakak berhasil diaktifkan")
                        print("=========================================================")
                        print("Kakak mendapat potongan sebesar 15%")
                        print("Kakak hanya membayar sebanyak Rp", bayar)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kakak ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                    else :
                        harga = 35000
                        saldo = int(saldo) - int(harga)
                        print("=========================================================")
                        print("Mohon maaf, kode yang kakak masukkan salah")
                        print("Kakak membayar sebanyak Rp", harga)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kakak ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                else :
                    harga = 35000
                    saldo = int(saldo) - int(harga)
                    print("=========================================================")
                    print("Kakak membayar sebanyak Rp", harga)
                    print("Sisa saldo : Rp", saldo)
                    print("=========================================================")
                    ulang = input("Kakak ingin Membeli lagi ? (ya/tidak) : ")
                    if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
            elif paket == "2" :
                print("Kakak memilih paket 2 seharga Rp30.000")
                tanya = input("Kakak memiliki voucher discount? (ya/tidak) : ")
                if tanya == "ya":
                    vouc = input("Silahkan masukkan kode voucher kakak : ")
                    print()
                    if vouc == "1234":
                        harga = 30000
                        disc = int(harga) * 0.15
                        bayar = int(harga) - int(disc)
                        saldo = int(saldo) - int(bayar)
                        print("Selamat, voucher kakak berhasil diaktifkan")
                        print("=========================================================")
                        print("Kakak mendapat potongan sebesar 15%")
                        print("Kakak hanya membayar sebanyak Rp", bayar)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kakak ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                    else :
                        harga = 30000
                        saldo = int(saldo) - int(harga)
                        print("=========================================================")
                        print("Mohon maaf, kode yang kakak masukkan salah")
                        print("Kakak membayar sebanyak Rp", harga)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kakak ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                else :
                    harga = 30000
                    saldo = int(saldo) - int(harga)
                    print("=========================================================")
                    print("Kakak membayar sebanyak Rp", harga)
                    print("Sisa saldo : Rp", saldo)
                    print("=========================================================")
                    ulang = input("Kakak ingin Membeli lagi ? (ya/tidak) : ")
                    if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
            else :
                print("Mohon maaf, paket tidak tersedia")
                print("Silahkan memilih paket 1/2")
                ulang = input("Kakak ingin mencoba lagi ? (ya/tidak) : ")
                if ulang == "tidak":
                    print("=========================================================")
                    print("=======================TERIMA KASIH======================")
                    print("=========================================================")
        elif jam >=11 and jam <=18 :
            siang = "Selamat Siang"
            print (siang, "Kak", nama)
            print("Kakak memiliki saldo sebanyak Rp", saldo)
            print()
            print (toko)
            print("=========================================================")
            print("=============BERIKUT MENU YANG KAMI SEDIAKAN=============")
            paket_1 = "1 Cheseburger +  1 French fries + 1 Cola"
            paket_2 = "1 Kebab Mozarella + 1 French fries + 1 Cola"
            print("=========================================================")
            print("1.", paket_1, "Rp 35.000")
            print("2.", paket_2, "Rp 30.000")
            print("=========================================================")
            paket = input ("Kakak mau paket yang mana (1/2): ")
            if paket == "1" :
                print("Kakak memilih paket 1 seharga Rp35.000")
                tanya = input("Kakak memiliki voucher discount? (ya/tidak) : ")
                if tanya == "ya":
                    vouc = input("Silahkan masukkan kode voucher kakak : ")
                    print()
                    if vouc == "1234":
                        harga = 35000
                        disc = int(harga) * 0.15
                        bayar = int(harga) - int(disc)
                        saldo = int(saldo) - int(bayar)
                        print("Selamat, voucher kakak berhasil diaktifkan")
                        print("=========================================================")
                        print("Kakak mendapat potongan sebesar 15%")
                        print("Kakak hanya membayar sebanyak Rp", bayar)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kakak ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                    else :
                        harga = 35000
                        saldo = int(saldo) - int(harga)
                        print("=========================================================")
                        print("Mohon maaf, kode yang kakak masukkan salah")
                        print("Kakak membayar sebanyak Rp", harga)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kakak ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                else :
                    harga = 35000
                    saldo = int(saldo) - int(harga)
                    print("=========================================================")
                    print("Kakak membayar sebanyak Rp", harga)
                    print("Sisa saldo : Rp", saldo)
                    print("=========================================================")
                    ulang = input("Kakak ingin Membeli lagi ? (ya/tidak) : ")
                    if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
            elif paket == "2" :
                print("Kakak memilih paket 2 seharga Rp30.000")
                tanya = input("Kakak memiliki voucher discount? (ya/tidak) : ")
                if tanya == "ya":
                    vouc = input("Silahkan masukkan kode voucher kakak : ")
                    print()
                    if vouc == "1234":
                        harga = 30000
                        disc = int(harga) * 0.15
                        bayar = int(harga) - int(disc)
                        saldo = int(saldo) - int(bayar)
                        print("Selamat, voucher kakak berhasil diaktifkan")
                        print("=========================================================")
                        print("Kakak mendapat potongan sebesar 15%")
                        print("Kakak hanya membayar sebanyak Rp", bayar)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kakak ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                    else :
                        harga = 30000
                        saldo = int(saldo) - int(harga)
                        print("=========================================================")
                        print("Mohon maaf, kode yang kakak masukkan salah")
                        print("Kakak membayar sebanyak Rp", harga)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kakak ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                else :
                    harga = 30000
                    saldo = int(saldo) - int(harga)
                    print("=========================================================")
                    print("Kakak membayar sebanyak Rp", harga)
                    print("Sisa saldo : Rp", saldo)
                    print("=========================================================")
                    ulang = input("Kakak ingin Membeli lagi ? (ya/tidak) : ")
                    if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
            else :
                print("Mohon maaf, paket tidak tersedia")
                print("Silahkan memilih paket 1/2")
                ulang = input("Kakak ingin mencoba lagi ? (ya/tidak) : ")
                if ulang == "tidak":
                    print("=========================================================")
                    print("=======================TERIMA KASIH======================")
                    print("=========================================================")
        elif jam >= 19 and jam <= 24 :
            malam = "Selamat Malam"
            print (malam, "Kak", nama)
            print("Kakak memiliki saldo sebanyak Rp", saldo)
            print()
            print (toko)
            print("=========================================================")
            print("=============BERIKUT MENU YANG KAMI SEDIAKAN=============")
            paket_1 = "1 Cheseburger +  1 French fries + 1 Cola"
            paket_2 = "1 Kebab Mozarella + 1 French fries + 1 Cola"
            print("=========================================================")
            print("1.", paket_1, "Rp 35.000")
            print("2.", paket_2, "Rp 30.000")
            print("=========================================================")
            paket = input ("Kakak mau paket yang mana (1/2): ")
            if paket == "1" :
                print("Kakak memilih paket 1 seharga Rp35.000")
                tanya = input("Kakak memiliki voucher discount? (ya/tidak) : ")
                if tanya == "ya":
                    vouc = input("Silahkan masukkan kode voucher kakak : ")
                    print()
                    if vouc == "1234":
                        harga = 35000
                        disc = int(harga) * 0.15
                        bayar = int(harga) - int(disc)
                        saldo = int(saldo) - int(bayar)
                        print("Selamat, voucher kakak berhasil diaktifkan")
                        print("=========================================================")
                        print("Kakak mendapat potongan sebesar 15%")
                        print("Kakak hanya membayar sebanyak Rp", bayar)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kakak ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                    else :
                        harga = 35000
                        saldo = int(saldo) - int(harga)
                        print("=========================================================")
                        print("Mohon maaf, kode yang kakak masukkan salah")
                        print("Kakak membayar sebanyak Rp", harga)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kakak ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                else :
                    harga = 35000
                    saldo = int(saldo) - int(harga)
                    print("=========================================================")
                    print("Kakak membayar sebanyak Rp", harga)
                    print("Sisa saldo : Rp", saldo)
                    print("=========================================================")
                    ulang = input("Kakak ingin Membeli lagi ? (ya/tidak) : ")
                    if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
            elif paket == "2" :
                print("Kakak memilih paket 2 seharga Rp30.000")
                tanya = input("Kakak memiliki voucher discount? (ya/tidak) : ")
                if tanya == "ya":
                    vouc = input("Silahkan masukkan kode voucher kakak : ")
                    print()
                    if vouc == "1234":
                        harga = 30000
                        disc = int(harga) * 0.15
                        bayar = int(harga) - int(disc)
                        saldo = int(saldo) - int(bayar)
                        print("Selamat, voucher kakak berhasil diaktifkan")
                        print("=========================================================")
                        print("Kakak mendapat potongan sebesar 15%")
                        print("Kakak hanya membayar sebanyak Rp", bayar)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kakak ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                    else :
                        harga = 30000
                        saldo = int(saldo) - int(harga)
                        print("=========================================================")
                        print("Mohon maaf, kode yang kakak masukkan salah")
                        print("Kakak membayar sebanyak Rp", harga)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Kakak ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                else :
                    harga = 30000
                    saldo = int(saldo) - int(harga)
                    print("=========================================================")
                    print("Kakak membayar sebanyak Rp", harga)
                    print("Sisa saldo : Rp", saldo)
                    print("=========================================================")
                    ulang = input("Kakak ingin Membeli lagi ? (ya/tidak) : ")
                    if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
            else :
                print("Mohon maaf, paket tidak tersedia")
                print("Silahkan memilih paket 1/2")
                ulang = input("Kakak ingin mencoba lagi ? (ya/tidak) : ")
                if ulang == "tidak":
                    print("=========================================================")
                    print("=======================TERIMA KASIH======================")
                    print("=========================================================")
    elif pin == "1111" and int(usia) > 35 and int(saldo) >= 35000 :
        if jam >= 0 and jam <= 10 :
            pagi = "Selamat pagi"
            print (pagi, "Pak/Bu", nama)
            print("Anda memiliki saldo sebanyak Rp", saldo)
            print()
            print (toko)
            print("=========================================================")
            print("=============BERIKUT MENU YANG KAMI SEDIAKAN=============")
            paket_1 = "1 Cheseburger +  1 French fries + 1 Cola"
            paket_2 = "1 Kebab Mozarella + 1 French fries + 1 Cola"
            print("=========================================================")
            print("1.", paket_1, "Rp 35.000")
            print("2.", paket_2, "Rp 30.000")
            print("=========================================================")
            paket = input ("Anda mau paket yang mana (1/2): ")
            if paket == "1" :
                print("Anda memilih paket 1 seharga Rp35.000")
                tanya = input("Anda memiliki voucher discount? (ya/tidak) : ")
                if tanya == "ya":
                    vouc = input("Silahkan masukkan kode voucher anda : ")
                    print()
                    if vouc == "1234":
                        harga = 35000
                        disc = int(harga) * 0.15
                        bayar = int(harga) - int(disc)
                        saldo = int(saldo) - int(bayar)
                        print("Selamat, voucher anda berhasil diaktifkan")
                        print("=========================================================")
                        print("Anda mendapat potongan sebesar 15%")
                        print("Anda hanya membayar sebanyak Rp", bayar)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Anda ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                    else :
                        harga = 35000
                        saldo = int(saldo) - int(harga)
                        print("=========================================================")
                        print("Mohon maaf, kode yang anda masukkan salah")
                        print("Anda membayar sebanyak Rp", harga)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Anda ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                else :
                    harga = 35000
                    saldo = int(saldo) - int(harga)
                    print("=========================================================")
                    print("Anda membayar sebanyak Rp", harga)
                    print("Sisa saldo : Rp", saldo)
                    print("=========================================================")
                    ulang = input("Anda ingin Membeli lagi ? (ya/tidak) : ")
                    if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
            elif paket == "2" :
                print("Anda memilih paket 2 seharga Rp30.000")
                tanya = input("Anda memiliki voucher discount? (ya/tidak) : ")
                if tanya == "ya":
                    vouc = input("Silahkan masukkan kode voucher anda : ")
                    print()
                    if vouc == "1234":
                        harga = 30000
                        disc = int(harga) * 0.15
                        bayar = int(harga) - int(disc)
                        saldo = int(saldo) - int(bayar)
                        print("Selamat, voucher anda berhasil diaktifkan")
                        print("=========================================================")
                        print("Anda mendapat potongan sebesar 15%")
                        print("Anda membayar sebanyak Rp", bayar)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Anda ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                    else :
                        harga = 30000
                        saldo = int(saldo) - int(harga)
                        print("=========================================================")
                        print("Mohon maaf, kode yang anda masukkan salah")
                        print("Anda membayar sebanyak Rp", harga)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Anda ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                else :
                    harga = 30000
                    saldo = int(saldo) - int(harga)
                    print("=========================================================")
                    print("Anda membayar sebanyak Rp", harga)
                    print("Sisa saldo : Rp", saldo)
                    print("=========================================================")
                    ulang = input("Anda ingin Membeli lagi ? (ya/tidak) : ")
                    if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
            else :
                print("Mohon maaf, paket tidak tersedia")
                print("Silahkan memilih paket 1/2")
                ulang = input("Anda ingin mencoba lagi ? (ya/tidak) : ")
                if ulang == "tidak":
                    print("=========================================================")
                    print("=======================TERIMA KASIH======================")
                    print("=========================================================")
        elif jam >=11 and jam <=18 :
            siang = "Selamat Siang"
            print (siang, "Pak/Bu", nama)
            print("Anda memiliki saldo sebanyak Rp", saldo)
            print()
            print (toko)
            print("=========================================================")
            print("=============BERIKUT MENU YANG KAMI SEDIAKAN=============")
            paket_1 = "1 Cheseburger +  1 French fries + 1 Cola"
            paket_2 = "1 Kebab Mozarella + 1 French fries + 1 Cola"
            print("=========================================================")
            print("1.", paket_1, "Rp 35.000")
            print("2.", paket_2, "Rp 30.000")
            print("=========================================================")
            paket = input ("Anda mau paket yang mana (1/2): ")
            if paket == "1" :
                print("Anda memilih paket 1 seharga Rp35.000")
                tanya = input("Anda memiliki voucher discount? (ya/tidak) : ")
                if tanya == "ya":
                    vouc = input("Silahkan masukkan kode voucher anda : ")
                    print()
                    if vouc == "1234":
                        harga = 35000
                        disc = int(harga) * 0.15
                        bayar = int(harga) - int(disc)
                        saldo = int(saldo) - int(bayar)
                        print("Selamat, voucher anda berhasil diaktifkan")
                        print("=========================================================")
                        print("Anda mendapat potongan sebesar 15%")
                        print("Anda hanya membayar sebanyak Rp", bayar)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Anda ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                    else :
                        harga = 35000
                        saldo = int(saldo) - int(harga)
                        print("=========================================================")
                        print("Mohon maaf, kode yang anda masukkan salah")
                        print("Anda membayar sebanyak Rp", harga)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Anda ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                else :
                    harga = 35000
                    saldo = int(saldo) - int(harga)
                    print("=========================================================")
                    print("Anda membayar sebanyak Rp", harga)
                    print("Sisa saldo : Rp", saldo)
                    print("=========================================================")
                    ulang = input("Anda ingin Membeli lagi ? (ya/tidak) : ")
                    if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
            elif paket == "2" :
                print("Anda memilih paket 2 seharga Rp30.000")
                tanya = input("Anda memiliki voucher discount? (ya/tidak) : ")
                if tanya == "ya":
                    vouc = input("Silahkan masukkan kode voucher anda : ")
                    print()
                    if vouc == "1234":
                        harga = 30000
                        disc = int(harga) * 0.15
                        bayar = int(harga) - int(disc)
                        saldo = int(saldo) - int(bayar)
                        print("Selamat, voucher anda berhasil diaktifkan")
                        print("=========================================================")
                        print("Anda mendapat potongan sebesar 15%")
                        print("Anda membayar sebanyak Rp", bayar)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Anda ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                    else :
                        harga = 30000
                        saldo = int(saldo) - int(harga)
                        print("=========================================================")
                        print("Mohon maaf, kode yang anda masukkan salah")
                        print("Anda membayar sebanyak Rp", harga)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Anda ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                else :
                    harga = 30000
                    saldo = int(saldo) - int(harga)
                    print("=========================================================")
                    print("Anda membayar sebanyak Rp", harga)
                    print("Sisa saldo : Rp", saldo)
                    print("=========================================================")
                    ulang = input("Anda ingin Membeli lagi ? (ya/tidak) : ")
                    if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
            else :
                print("Mohon maaf, paket tidak tersedia")
                print("Silahkan memilih paket 1/2")
                ulang = input("Anda ingin mencoba lagi ? (ya/tidak) : ")
                if ulang == "tidak":
                    print("=========================================================")
                    print("=======================TERIMA KASIH======================")
                    print("=========================================================")
        elif jam >= 19 and jam <= 24 :
            malam = "Selamat Malam"
            print (malam, "Pak/Bu", nama)
            print("Anda memiliki saldo sebanyak Rp", saldo)
            print()
            print (toko)
            print("=========================================================")
            print("=============BERIKUT MENU YANG KAMI SEDIAKAN=============")
            paket_1 = "1 Cheseburger +  1 French fries + 1 Cola"
            paket_2 = "1 Kebab Mozarella + 1 French fries + 1 Cola"
            print("=========================================================")
            print("1.", paket_1, "Rp 35.000")
            print("2.", paket_2, "Rp 30.000")
            print("=========================================================")
            paket = input ("Anda mau paket yang mana (1/2): ")
            if paket == "1" :
                print("Anda memilih paket 1 seharga Rp35.000")
                tanya = input("Anda memiliki voucher discount? (ya/tidak) : ")
                if tanya == "ya":
                    vouc = input("Silahkan masukkan kode voucher anda : ")
                    print()
                    if vouc == "1234":
                        harga = 35000
                        disc = int(harga) * 0.15
                        bayar = int(harga) - int(disc)
                        saldo = int(saldo) - int(bayar)
                        print("Selamat, voucher anda berhasil diaktifkan")
                        print("=========================================================")
                        print("Anda mendapat potongan sebesar 15%")
                        print("Anda hanya membayar sebanyak Rp", bayar)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Anda ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                    else :
                        harga = 35000
                        saldo = int(saldo) - int(harga)
                        print("=========================================================")
                        print("Mohon maaf, kode yang anda masukkan salah")
                        print("Anda membayar sebanyak Rp", harga)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Anda ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                else :
                    harga = 35000
                    saldo = int(saldo) - int(harga)
                    print("=========================================================")
                    print("Anda membayar sebanyak Rp", harga)
                    print("Sisa saldo : Rp", saldo)
                    print("=========================================================")
                    ulang = input("Anda ingin Membeli lagi ? (ya/tidak) : ")
                    if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
            elif paket == "2" :
                print("Anda memilih paket 2 seharga Rp30.000")
                tanya = input("Anda memiliki voucher discount? (ya/tidak) : ")
                if tanya == "ya":
                    vouc = input("Silahkan masukkan kode voucher anda : ")
                    print()
                    if vouc == "1234":
                        harga = 30000
                        disc = int(harga) * 0.15
                        bayar = int(harga) - int(disc)
                        saldo = int(saldo) - int(bayar)
                        print("Selamat, voucher anda berhasil diaktifkan")
                        print("=========================================================")
                        print("Anda mendapat potongan sebesar 15%")
                        print("Anda membayar sebanyak Rp", bayar)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Anda ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                    else :
                        harga = 30000
                        saldo = int(saldo) - int(harga)
                        print("=========================================================")
                        print("Mohon maaf, kode yang anda masukkan salah")
                        print("Anda membayar sebanyak Rp", harga)
                        print("Sisa saldo : Rp", saldo)
                        print("=========================================================")
                        ulang = input("Anda ingin Membeli lagi ? (ya/tidak) : ")
                        if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
                else :
                    harga = 30000
                    saldo = int(saldo) - int(harga)
                    print("=========================================================")
                    print("Anda membayar sebanyak Rp", harga)
                    print("Sisa saldo : Rp", saldo)
                    print("=========================================================")
                    ulang = input("Anda ingin Membeli lagi ? (ya/tidak) : ")
                    if ulang == "tidak":
                            print("=========================================================")
                            print("=======================TERIMA KASIH======================")
                            print("==============Semoga Makanan Kami memuaskan==============")
                            print("=========================================================")
            else :
                print("Mohon maaf, paket tidak tersedia")
                print("Silahkan memilih paket 1/2")
                ulang = input("Anda ingin mencoba lagi ? (ya/tidak) : ")
                if ulang == "tidak":
                    print("=========================================================")
                    print("=======================TERIMA KASIH======================")
                    print("=========================================================")
    elif pin == "1111" and int(usia) <= 16 and int(saldo) < 35000 :
        print("Mohon maaf, kamu tidak dapat melanjutkan pembelian")
        print("Saldo kamu tidak mencukupi")
        break
    elif pin == "1111" and int(usia) > 16 and int(usia) <= 35 and int(saldo) < 35000 :
        print("Mohon maaf, kakak tidak dapat melanjutkan pembelian")
        print("Saldo kakak tidak mencukupi")
        break
    elif pin == "1111" and int(usia) > 35 and int(saldo) < 35000 :
        print("Mohon maaf, Anda tidak dapat melanjutkan pembelian")
        print("Saldo anda tidak mencukupi")
        break
    else:
        print("Mohon maaf, info login anda tidak sesuai")
        ulang = input("Anda ingin mencoba lagi ? (ya/tidak) : ")