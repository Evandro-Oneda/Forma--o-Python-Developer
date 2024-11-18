import ctypes

ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW("ocultar.txt", ocultar)

if retorno:
    print("arquivo ocultado")

else:
    print("arquivo não ocultado")
    