def copiar_texto(origen, destino, encoding="utf-8"):
    with open(origen, "r", encoding=encoding) as f_in, open(destino, "w", encoding=encoding) as f_out:
        for linea in f_in:
            f_out.write(linea)
    print(f"Copiado texto de '{origen}' a '{destino}'.")

def copiar_binario(origen, destino, chunk=1024 * 64):
    with open(origen, "rb") as f_in, open(destino, "wb") as f_out:
        while True:
            data = f_in.read(chunk)
            if not data:
                break
            f_out.write(data)
    print(f"Copiado binario de '{origen}' a '{destino}'.")

if __name__ == "__main__":
    copiar_texto("entrada.txt", "salida.txt")
    copiar_binario("imagen.png", "imagen_copia.png")


