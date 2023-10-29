# Döviz məzənnələri
doviz_mezenneleri = {
    "AZN": 1.0,
    "USD": 1.7,  # 1 AZN = 1.7 USD
    "EUR": 1.9   # 1 AZN = 1.9 EUR
}

# İstifadəçidən giriş məlumatlarını almaq
satiram_dovizi = input("SATIRAM (AZN, USD, EUR): ")
aliram_dovizi = input("ALIRAM (AZN, USD, EUR): ")
mebleg = float(input("Mebleg: "))

# Dövizləri mübadilə etmək
satiram_mezennesi = doviz_mezenneleri.get(satiram_dovizi)
aliram_mezennesi = doviz_mezenneleri.get(aliram_dovizi)

if satiram_mezennesi is not None and aliram_mezennesi is not None:
    alinacaq_miqdar = mebleg * (aliram_mezennesi / satiram_mezennesi)
    print(f"{mebleg} {satiram_dovizi} = {alinacaq_miqdar:.2f} {aliram_dovizi}")
else:
    print("Dövizləri tapa bilmirəm. Zəhmət olmasa doğru döviz kodlarını daxil edin.")
