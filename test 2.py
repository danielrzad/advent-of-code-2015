data = """Agnieszka Gajewska - zaproszenie.docx
BGŻ BNP Paribas - zaproszenie.docx
BGŻ BNP Paribas.docx
Carlo Bossi - zaproszenie.docx
Carlo Bossi.docx
Etanex.docx
Fundacja Uniwersytecka - zaproszenie.docx
Fundacja Uniwersytecka.docx
Gentelman zaproszenie.docx
Gentelman.docx
Halmar - zaproszenie.docx
Halmar.docx
Henryk Żerdecki - zaproszenie.docx
Hlawacz.docx
Ikeda - zaproszenie.docx
Iwamet - zaproszenie.docx
Iwamet.docx
Konesso zaproszenie.docx
Konesso.docx
Krystyna Ziętek - zaproszenie.docx
Maraton zaproszenie.docx
Maraton.docx
Matthias - zaproszenie.docx
Matthias.docx
MH Motors - zaproszenie.docx
MH Motors.docx
Novamed zaproszenie.docx
Novamed.docx
Poltra - zaproszenie.docx
Poltra.docx
Prefbud - zaproszenie.docx
Prefbud.docx
Prezydent - zaproszenie.docx
Prezydent.docx
Robert Nowak - zaproszenie.docx
Skarem - zaproszenie.docx
Skarem.docx
Slovrur - zaproszenie.docx
Slovrur.docx
Społem - zaproszenie.docx
Społem.docx
Starosta - zaproszenie.docx
Stawosan.docx
Tartacznictwo - zaproszenie.docx
Tartacznictwo.docx
Travel zaproszenie.docx
Travel.docx
Wash Serwis - zaproszenie.docx
Wash Serwis.docx
Zaproszenie Gajewski.docx
Zbigniew Rogowski - zaproszenie.docx
Zdzisława Gajewska - zaproszenie.docx"""

data2 = """BGŻ BNP Paribas.docx
Carlo Bossi.docx
Etanex.docx
Gentelman.docx
Halmar.docx
Hlawacz.docx
Iwamet.docx
Konesso.docx
Maraton.docx
Matthias.docx
MH Motors.docx
nazwyplikow.txt
Novamed.docx
Poltra.docx
Prezydent.docx
Skarem.docx
Slovrur.docx
Społem.docx
Travel.docx
Wash Serwis.docx"""



data = data.replace(' - zaproszenie.docx', '').replace('.docx', '').replace(' zaproszenie', '').splitlines()
data = set(data)
print(len(data))
#print('\n'.join(data1))