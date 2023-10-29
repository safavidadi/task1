# Adı və təsviri olan bir lüğət (dictionary) yaratmaq
tesvirler = {
    "Aslan": "Aslan emi ogludur",
    "Imran": "Imran dayi ogludur",
    "Afaq": "Afaq bibi qizidir",
    "Uzeyir": "Uzeyir xala ogludur",
    "Shahin": "Shahin yaxin dostdur"
}

while True:
    # İstifadəçidən ad soruşmaq
    ad = input("Ad daxil edin:\n")
    
    # Ad daxil edilmədiyində "Siz ad daxil etmədiniz" yazmaq
    if not ad:
        print("Siz ad daxil etmədiniz")
        continue

    # Adı lüğətdə axtarmaq və təsviri ekrana çap etmək
    if ad in tesvirler:
        tesvir = tesvirler[ad]
        print(tesvir)
    else:
        print(f"{ad} kimdir? Men onu tanımadım.")