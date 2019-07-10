# 1.OPAKOVANI definujeme hlavni funkci s parametrem
# 2.OPAKOVANI importovani modulu
import random


# (F1)
def main(seznam_slov):
    """Zde definujeme hlavni promenne."""

    # 1.OPAKOVANI vlozime jmeno hrace
    # 2.OPAKOVANI nahodne slovo z listu, jakou metodu pouzijeme?
    # 3.OPAKOVANI podle delky pocet pokusu
    # 4.OPAKOVANI postup
    jmeno_hrace = input('Tvoje prezdivka: ')
    vybrane_slovo = random.choice(seznam_slov)
    print(vybrane_slovo)
    pocet_pokusu = int(len(vybrane_slovo)) * 2
    postup = ['_'] * len(vybrane_slovo)

    print('\nDalsi bude hrac '+jmeno_hrace+', tedy zacneme!')
    print('\nHrac: '+jmeno_hrace+'\tTvuj postup: ' + ' '.join(postup) + '\tZbyva pokusu: ' + str(pocet_pokusu))

    # 5.NOVE formatovani stringu ve funkci print()
    print('\nDalsi bude hrac {}, tedy zacneme! '.format(jmeno_hrace))
    # print('\nHrac: {}\tTvuj postup: {} \tZbyva pokusu: {}'.format(jmeno_hrace, ' '.join(postup), pocet_pokusu))

    while True:
        # 6.OPAKOVANI (f1)vytiskni stav a (f2)ziskej tip hrace
        stav = tisk_stavu(jmeno_hrace, postup, pocet_pokusu)
        tip_hrace = ziskej_tip_hrace(stav)

        # 7.OPAKOVANI (f3)nahrad podtrzitka a (f4)vytiskni uspesnot hadani
        pocet_nahrazeni = nahrad_pritomna_pismena(tip_hrace, postup, vybrane_slovo)
        tiskni_pocet_nahrazeni(pocet_nahrazeni, tip_hrace)

        pocet_pokusu -= 1

        # 8.OPAKOVANI vypis vyhra/ prohra
        if '_' not in postup:
            print('Vyborne {}, vyhral jsi! Hledane slovo je "{}".'.format(jmeno_hrace, vybrane_slovo))
            break
        elif pocet_pokusu == 0:
            print('{}, prohrals! Hledane slovo bylo "{}".'.format(jmeno_hrace, vybrane_slovo))
            break


def tisk_stavu(jmeno_hrace, postup, pocet_pokusu):
    # 9.NOVE tisknu aktualni stav hry
    stav = 'Hrac: {}\tTvuj postup: {}\tZbyva pokusu: {}'.format(jmeno_hrace, ' '.join(postup), pocet_pokusu)
    oddil = '=' * len(stav)
    print('{}\n{}\n{}\n'.format(oddil, stav, oddil))
    return stav


def ziskej_tip_hrace(stav):
    """Vrati pismeno, nebo prazdny string z formatovane otazky."""
    # 10.NOVE vracet True/ False podle input()
    tip_hrace = input('Hadej pismeno ze slova: '.center(len(stav) - 1, ))
    if len(tip_hrace) == 1:
        return tip_hrace
    else:
        return ""


def nahrad_pritomna_pismena(tip_hrace, postup, vybrane_slovo):
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

    return pocet_nahrazeni


def tiskni_pocet_nahrazeni(pocet_nahrazeni, tip_hrace):
    # 14.NOVE hlasim, kolik jsem nasel pismen
    # 15.NOVE hlasim, ze toto pismeno neni ve slove
    if pocet_nahrazeni:
        print('\nPismeno "{}" se ve slove vyskytuje {}x.\n'.format(tip_hrace, pocet_nahrazeni))

    else:
        print('\nPismeno "{}" neni v hledanem slove.\n'.format(tip_hrace))


# 16.NOVE neresit

    # 18.NOVE nacteme si soubor v rezimu "r", opatrne na jmeno souboru
    # 19.NOVE nastavime si kurzor na nulu
    # 20.NOVE projdeme rozdeleny soubor a appendujeme slova
    # 21.NOVE nakonec soubor zavreme, abychom ho dale nenechavali otevreny
    # 22.OPAKOVANI zavolam funkci pro nas seznam
    nase_slova = open('words.txt', 'r')
    nase_slova.seek(0)
    slova = nase_slova.read().split()
    # nase_slova = ['Hangman', 'available', 'increase']

    # print(slova)

    nase_slova.close()
    main(slova)
