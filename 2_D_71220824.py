notel = str(input('Masukan Nomor Telpon : '))
ater = notel.split()[:-1]

if notel[:4] == '0816':
    print('Anda menggunakan operator indosat')
    angka = (notel)
elif notel[:4] == '0814': 
    print('Anda menggunakan operator telkomsel')
else:
    print('Operator anda tidak diketahui')
    
gengan = int(notel)
if gengan % 2 == 0:
    print('Nomor anda berakhiran genap')
else:
    print('Nomor anda berakhiran ganjil')