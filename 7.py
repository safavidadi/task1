# Adları saxlamaq üçün boş bir list yaradırıq
adlar = []

while True:
    ad = input("Ad daxil edin: ")

    if not ad:
        print("Ad daxil etmediniz")
        continue

    if len(ad) > 15:
        print("Ad çox uzundur. Maksimum 15 hərfə izn verilir.")
        continue

    adlar.append(ad)
    print(f"Ad '{ad}' bazaya uğurla əlavə olundu.")

    davam_et = input("Yeni ad əlavə etmək istəyirsiniz mi? (bəli/Xeyir): ")
    if davam_et.lower() != "bəli":
        break

print("Bütün adlar: ", adlar)
