import smtplib
import ssl
from email.message import EmailMessage

# E-posta kimlik bilgilerinizi güvence altına alın (onları kod içinde ifşa etmekten kaçının)
email_adresi = "deneme909@gmail.com"
email_parolası = "deneme909"  # Güvenli bir parola alma yöntemi ile değiştirin

# E-posta mesajı nesnesini oluşturun
mesaj = EmailMessage()
mesaj['Konu'] = 'E-posta Konusu'
mesaj['Kimden'] = email_adresi
mesaj['Kime'] = 'alıcı1@örnek.com'
# mesaj['Kime'] = ['alıcı1@örnek.com', 'alıcı2@örnek.com','alıcı3@örnek.com']  # Birden fazla alıcı ekleyin


mesaj.set_content("deneme mesajı.")


bağlam = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=bağlam) as smtp:
    smtp.login(email_adresi, email_parolası)
    # E-postayı gönder
    smtp.sendmail(email_adresi, mesaj['Kime'], mesaj.as_string())

print("E-posta başarıyla gönderildi!")
