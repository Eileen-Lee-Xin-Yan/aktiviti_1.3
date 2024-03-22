#Atur cara mengira luas permukaan dan isipadu silinder
#Isytihar pemalar
pi=3.142

#Kod input
tinggi=float(input("Masukkan tinggi:"))
jejari=float(input("Masukkan jejari:"))

#Kod proses
luas_permukaan=(2*pi*(jejari**2))+(2*pi*jejari*tinggi)
isipadu=pi*(jejari**2)*tinggi

#Kod output
print("Luas permukaan ialah",luas_permukaan)
print("Isipadu ialah",isipadu)
