import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Girilen bilgileri kullanıcıya göster
    print(f"Girilen kullanıcı adı: {username}")
    print(f"Girilen şifre: {password}")

    # Burada kullanıcı adı ve şifre doğrulaması yapabilirsin
    if username == "admin" and password == "1234":  # Örnek doğrulama
        messagebox.showinfo("Başarılı", "Giriş başarılı!")
    else:
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış.")

# Ana pencereyi oluşturuyoruz
root = tk.Tk()
root.title("Instagram Giriş")
root.geometry("400x550")  # Instagram giriş ekranına yakın boyut
root.config(bg="#ffffff")  # Arka plan rengi beyaz

# Logo ekleyelim (Instagram yazısı ya da görsel)
label_logo = tk.Label(root, text="Instagram", font=("Billabong", 50), fg="#3f729b", bg="#ffffff")
label_logo.pack(pady=40)

# Kullanıcı adı etiketi ve kutusu
label_username = tk.Label(root, text="Kullanıcı Adı", font=("Arial", 10), bg="#ffffff")
label_username.pack(pady=5)

entry_username = tk.Entry(root, font=("Arial", 12), bd=1, relief="solid", width=30, fg="black", bg="#f0f0f0", highlightthickness=1, highlightbackground="#dcdcdc")
entry_username.pack(pady=10)

# Şifre etiketi ve kutusu
label_password = tk.Label(root, text="Şifre", font=("Arial", 10), bg="#ffffff")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*", font=("Arial", 12), bd=1, relief="solid", width=30, fg="black", bg="#f0f0f0", highlightthickness=1, highlightbackground="#dcdcdc")
entry_password.pack(pady=10)

# Giriş butonu (Instagram mavi tonu)
login_button = tk.Button(root, text="Giriş Yap", font=("Arial", 12), bg="#3897f0", fg="white", relief="flat", width=30, height=2, command=login)
login_button.pack(pady=20)

# Şifremi unuttum bağlantısı
forgot_password = tk.Label(root, text="Şifreni mi unuttun?", fg="#3897f0", bg="#ffffff", cursor="hand2")
forgot_password.pack(pady=5)
forgot_password.bind("<Button-1>", lambda e: messagebox.showinfo("Şifre Kurtarma", "Şifre kurtarma sayfası henüz aktif değil."))

# Alt kısımda "Yeni hesap oluştur" bağlantısı
signup_label = tk.Label(root, text="Hesabınız yok mu?  Yeni hesap oluştur.", fg="#3897f0", bg="#ffffff", cursor="hand2")
signup_label.pack(pady=15)

# Uygulamanın ana döngüsünü başlatıyoruz
root.mainloop()
