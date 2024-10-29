import hashlib

arquivo1 = ("C:\Formação Python Developer\Forma--o-Python-Developer\seguranca_da_informacao\comparador_hashes_a.txt")
arquivo2 = ("C:\Formação Python Developer\Forma--o-Python-Developer\seguranca_da_informacao\comparador_hashes_b.txt")

hash1 = hashlib.new("ripemd160")
hash1.update(open(arquivo1, "rb").read())

hash2 = hashlib.new("ripemd160")
hash2.update(open(arquivo2, "rb").read())

if hash1.digest() != hash2.digest():
    print("os arquivos sao diferentes!!!")

else:
    print("os arquivos sao iguais")