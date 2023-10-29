# İstifadəçidən 3 ədəd rəqəm alın
birinci_eded = int(input("Birinci ədədi daxil edin: "))
ikinci_eded = int(input("İkinci ədədi daxil edin: "))
ucuncu_eded = int(input("Üçüncü ədədi daxil edin: "))

# Ən böyük rəqəmi tapmaq
en_boyuk_eded = max(birinci_eded, ikinci_eded, ucuncu_eded)

# Ən böyük rəqəmi ekrana yazdırmaq
print(f"Ən böyük rəqəm: {en_boyuk_eded}")