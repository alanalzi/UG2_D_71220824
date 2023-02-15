print('='*15,'MAKANAN','='*15)
print('1. Telur Bakar           : Rp 7.000')
print('2. Lele Terbang Mas Bhe  : Rp 10.000')
print('3. Es Cokelat Lempu      : Rp 5.000')
print('4. Es Doger Langensari   : Rp 13.000')

print('='*20,'PESANAN', '='*20)
telor = int(input('Telur Bakar              : '))
le    = int(input('Lele Terbang             : '))
esco  = int(input('Es Cokelat               : '))
esdo  = int(input('Es doger                 : '))

htelor = 7000
hlele = 10000
hesco = 5000
hesdo = 13000

print('='*20,'TOTAL', '='*20)
print('TOTAL TELUR BAKAR x',telor, '   : Rp',htelor * telor  )
print('TOTAL LELE TERBANG x',le,'  : Rp',hlele*le)
print('TOTAL ES COKELAT x',esco,'    : Rp',hesco*esco)
print('TOTAL ES DOGER x ',esdo,'     : Rp',hesdo*esdo)

