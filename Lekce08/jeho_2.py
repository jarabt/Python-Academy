# 1.OPAKOVANI definujeme hlavni funkci s parametrem
# 2.OPAKOVANI importovani modulu
import random


# (F1)
def hlavni_rozhrani(seznam_slov):
    """Fce definuje hlavni promenne a opakuje hru,
    dokud hrac nevyhraje, nebo neprohraje"""

    # 1.OPAKOVANI vlozime jmeno hrace
    # 2.OPAKOVANI nahodne slovo z listu, jakou metodu pouzijeme?
    # 3.OPAKOVANI podle delky pocet pokusu
    # 4.OPAKOVANI postup
    jmeno_hrace = input('Tvoje prezdivka: ')
    vybrane_slovo = random.choice(seznam_slov)
    pocet_pokusu = int(len(vybrane_slovo)) * 2
    postup = ['_'] * len(vybrane_slovo)

    # 5.NOVE formatovani stringu ve funkci print()
    print('\nDalsi bude hrac {}, tedy zacneme! '.format(jmeno_hrace))
    # print('\nHrac: {}\tTvuj postup: {}\tZbyva pokusu: {}'.format(jmeno_hrace, ' '.join(postup), pocet_pokusu))

    while True:
        # 6.OPAKOVANI aplikuji dalsi funkci
        # 7.OPAKOVANI odectu pokusve slove vyskytuje

        tip_hrace = vrat_pismeno(postup, pocet_pokusu, jmeno_hrace)
        pocet_nahrazeni = prepsano(postup, tip_hrace, vybrane_slovo)
        pocet_pokusu -= 1

        # 8.OPAKOVANI vypis vyhra/ prohra
        if '_' not in postup:
            print('Vyborne {}, vyhral jsi! Hledane slovo je "{}".'.format(jmeno_hrace, vybrane_slovo))
            break
        elif pocet_pokusu == 0:
            print('{}, prohrals! Hledane slovo bylo "{}".'.format(jmeno_hrace, vybrane_slovo))
            break

    # (F2)
def vrat_pismeno(postup, pocet_pokusu, jmeno_hrace):
    """Pokud hrac uhadne, vrati pismeno."""
    # 9.NOVE tisknu aktualni stav hry
    # 10.NOVE vracet True/ False podle input()
    text = 'Hrac: {}\tTvuj postup: {}\tZbyva pokusu: {}'.format(jmeno_hrace, ' '.join(postup), pocet_pokusu)
    oddil = '=' * len(text)
    print('{}\n{}\n{}\n'.format(oddil, text, oddil))

    tip_hrace = input('Hadej pismeno ze slova: '.center(len(text) - 1, ))
    if len(tip_hrace) == 1:
        return tip_hrace
    else:
        return ""

    # (F3)
def prepsano(postup, tip_hrace, vybrane_slovo):
    """Po vraceni True chci nahradit symbol '_ ' konkretnim pismenem."""
    # 11.OPAKOVANI kolik jsem uhodl pismen
    pocet_nahrazeni = 0

    # 12.OPAKOVANI prochazime pismena ve schovanem slove
    for cislo, pismeno in enumerate(vybrane_slovo):
        if pismeno in tip_hrace:
            # 13.OPAKOVANI pokud se tip a pismeno shoduji...
            # ... nahradim podtr. na indexu konkretnim pismenem
            # ... a zvysim pocet
            postup[cislo] = tip_hrace
            pocet_nahrazeni += 1

    # 14.NOVE hlasim, kolik jsem nasel pismen
    # 15.NOVE hlasim, ze toto pismeno neni ve slove
    if pocet_nahrazeni:
        print('\nPismeno "{}" se ve slove vyskytuje {}x.\n' \
              .format(tip_hrace, pocet_nahrazeni))

    else:
        print('\nPismeno "{}" neni v hledanem slove.\n' \
              .format(tip_hrace))
    return pocet_nahrazeni

# (RUNNING THE CODE)
# 16.NOVE neresit
if __name__ == '__main__':
    # 18.NOVE nacteme si soubor v rezimu "r", opatrne na jmeno souboru
    # 19.NOVE nastavime si kurzor na nulu
    # 20.NOVE projdeme rozdeleny soubor
    # 21.NOVE nakonec soubor zavreme, abychom ho dale nenechavali otevreny
    # 22.OPAKOVANI zavolam funkci pro nas seznam
    nase_slova = open('words.txt', 'r')
    nase_slova.seek(0)
    slova = nase_slova.read().strip().split("\n")
    nase_slova.close()

    # slova = ['Hangman', 'available', 'increase']
    print(slova)

    hlavni_rozhrani(slova)
