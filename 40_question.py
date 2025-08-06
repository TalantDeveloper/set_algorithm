kalit = input("Kalit so'zni kiriting: ")
kalit_bytes = kalit.encode('utf-8')
print(kalit_bytes)
kalit_uzunlik = len(kalit_bytes)
with open("input.txt", "rb") as kirish_fayli, open("output.bin", "wb") as chiqish_fayli:
    while True:
        blok = kirish_fayli.read(256)
        if not blok:
            break
        shifrlangan_blok = bytearray()
        for i in range(len(blok)):
            xor_natija = blok[i] ^ kalit_bytes[i % kalit_uzunlik]
            shifrlangan_blok.append(xor_natija)
        chiqish_fayli.write(shifrlangan_blok)
        print(shifrlangan_blok)



