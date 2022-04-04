lista_zakupów = {
    'piekarnia': ['Chleb', 'Pączek', 'Bułki'],
    'warzywniak': ['Marchew', 'Seler', 'Rukola']
    }
for key in lista_zakupów:
    print('Idę do', key, 'i kupuję tu następujące rzeczy: ', lista_zakupów[key])
count = 0
for x in lista_zakupów:
    if isinstance(lista_zakupów[x], list):
        count += len(lista_zakupów[x])
print('W sumie kupuję', count, 'produktów')

# specjalne pozdrowionka
