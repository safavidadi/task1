# İstifadəçinin login və parol məlumatları
doğru_login = "test"
doğru_parol = "12345"

# İstifadəçidən login və parol soruşmaq
login = input("Login:\n")
parol = input("Parol:\n")

# Şərtlərə əsasən yoxlamaq və cavab verərkən error mesajları istifadə etmək
if not login and not parol:
    print("Login və parol daxil etmediniz")
elif not login:
    print("Login daxil etmediniz")
elif not parol:
    print("Parol daxil etmediniz")
elif login == doğru_login and parol == doğru_parol:
    print("Xoş gəldiniz")
elif login != doğru_login and parol != doğru_parol:
    print("Login və parol yanlışdır")
elif login != doğru_login:
    print("Login yanlışdır")
elif parol != doğru_parol:
    print("Parol yanlışdır")