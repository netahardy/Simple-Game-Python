import random

print("--------- Love Meter ---------")
print("")
loop = True
while loop:
    cowok = input("Masukkan Nama Cowok = ")
    cewek = input("Masukkan Nama Cewek = ")
    print("")
    print("----------hasilnya ----------")
    print("")

    print("Nama Cowok = ", cowok)
    print("Nama cewek = ", cewek)
    confirm = input("Apakah nama yang Anda masukkan sudah benar? 1.Ya/2.Tidak = ")
    if confirm == '1':
        loop = False
match = random.randrange(0, 100)

if (cowok[0:2]) == (cewek[0:2]):
    print(match + 2)
# Percabangan Bertingkat
print('Kecocokan ', match + 2, '%')
if match > 80:
    print("")
    print("Anda memiliki kecocokan")
elif match > 60:
    print("")
    print("Anda perlu pertimbangkan pilihan Anda")
elif match > 40:
    print("")
    print("Pikirkan lagi")
elif match > 20:
    print("")
    print("Sepertinya Anda tidak cocok")
elif match > 0:
    print("")
    print("Maaf,kalian tidak ada kecocokan sama sekali")
