import phonenumbers

from phonenumbers import geocoder

phone = input("Digite o telefone no formato +5541999999999: ")

phone_number = phonenumbers.parse(phone)

print("Localidade: ",geocoder.description_for_number(phone_number, "pt"))