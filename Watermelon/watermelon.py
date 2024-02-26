jumlah_semangka = int(input())
remainder_semangka = jumlah_semangka % 2

if jumlah_semangka == 2:
    print("NO")
else:
    if remainder_semangka == 1:
        print("NO")
    else:
        print("YES")