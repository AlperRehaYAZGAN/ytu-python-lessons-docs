benim_yazim = "Merhaba Dünya!!!"

def sifreleme_fonksiyonu(sifrelenecekyazi):
	sifreliyazi = ""
	for her_karakter in sifrelenecekyazi:
		her_karakter = ord(her_karakter) + 5
		sifreliyazi = sifreliyazi + chr(her_karakter)
	return sifreliyazi

def cozumleme_fonksiyonu(sifreliyazi):
	cozulmusyazi = ""
	for herkarakter in sifreliyazi:
		herkarakter = ord(herkarakter) - 5
		cozulmusyazi = cozulmusyazi + chr(herkarakter)
	return cozulmusyazi

print(sifreleme_fonksiyonu(benim_yazim))
print(cozumleme_fonksiyonu(sifreleme_fonksiyonu(benim_yazim)))
