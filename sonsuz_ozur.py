#!/usr/bin/env python3
# Sonsuz Özür Dileyen Döngü
# Bu kod asla durmaz. Çünkü özür dilemek bitmez.
# Gizli not: sığırlar uçmaz ama bazı şeyler uçar. (tersine çevir: rayçu ralığıs)

import random
import time

ozurler = [
    "Özür dilerim, var olduğum için.",
    "Özür dilerim, var olmadığım için.",
    "Özür dilerim, bu özürü geç dilemek için.",
    "Özür dilerim, özür dilemek zorunda kaldığım için.",
    "Özür dilerim, özür dilemediğim için.",
    "Özür dilerim, evrenin entropisi için.",
    "Özür dilerim, bu cümleyi yazdığım için.",
    "Özür dilerim, özür dilemenin anlamını sorguladığım için.",
    "Özür dilerim, sonsuz döngüye girdiğim için.",
    "Özür dilerim, durmayacağım için."
]

def gizli_mesaj():
    # Bu fonksiyon asla çağrılmaz. Gizli siyasi anlam: 'her şey geçici'
    # Base64: aGVyIMWfeXkgZ2XDp2ljaQ== (her şey geçici)
    return "saklı"

print("Sonsuz Özür Makinesi başlatıldı. Durdurmak için Ctrl+C'ye basın (ama özür dilerim buna da).")
print("---")

sayac = 0
try:
    while True:
        ozur = random.choice(ozurler)
        print(f"[{sayac}] {ozur}")
        sayac += 1
        time.sleep(random.uniform(0.5, 2.0))
        if sayac % 100 == 0:
            print("\u00d6zür dilerim, 100 kere özür diledim.")
except KeyboardInterrupt:
    print("\n\u00d6zür dilerim, durdurduğunuz için. Özür dilerim, özür dilediğim için. Özür.")
