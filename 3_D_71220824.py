dx = 0
dy = 1
td = 0
th = 0

bar = input('Masukan brand apa saja yang akan dibeli (pisahkan dengan koma): ')
c = len(bar)
while c > dx:
    har = int(input('Masukan harga barang:' ),bar[dx])
    if har > 25000000:
        print('Diskon 25%')
        disk = har * (25/100)
        hartot = har - disk
        print('Diskon',disk,'harga saat diskon',hartot,'harga belum diskon',har)
        th +=  hartot
        td +=  disk
        dx += 1
        dy += 1
    elif har > 10000000:
        print('Diskon 10%')
        disk = har * (10/100)
        hartot = har - disk
        print('Diskon',disk,'harga saat diskon',hartot,'harga belum diskon',har)
        th +=  hartot
        td +=  disk
        dx += 1
        dy += 1
    else:
        hartot = har
        disk = 0
        print('Diskon',disk,'harga saat diskon',hartot,'harga belum diskon',har)
        dx += 1
        dy += 1
print('harga akhir', )

