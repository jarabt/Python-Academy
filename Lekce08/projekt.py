import random
nase_slova = ['Hangman', 'available', 'increase']

def F2(jmeno, postup, pokusy, slovo):
    print("=" * 60)
    print("Hráč: {} Tvůj postup: {} Zbývá bodů: {}"\
    .format(jmeno, "".join(postup), pokusy))
    print("=" * 60)
    pismeno = input("Zadej písmeno: ")
    if pismeno in slovo:
        return pismeno
    else:
        return ""

def F3(uhadnute_pismeno, postupujeme, tajne_slovo):
    uhadnutych = 0
    for index, pis in enumerate(tajne_slovo):
        if uhadnute_pismeno == pis:
            postupujeme[index] = pis
            uhadnutych += 1
    return uhadnutych

def main(slova):
    jmeno_hrace = input("Prosim zadej jmeno: ")
    nahodne_slovo = random.choice(nase_slova)
    pocet_pokusu = 2 * len(nahodne_slovo)
    zatim_postup = ["_"] * len(nahodne_slovo)
    print("Další hráč bude {}, tedy začneme!".format(jmeno_hrace))
    F2()










#for i in range(pocet_pokusu):





    # (F1)
	# 1.OPAKOVANI vlozime jmeno hrace
	# 2.OPAKOVANI nahodne slovo z listu, jakou metodu pouzijeme?
	# 3.OPAKOVANI podle delky pocet pokusu
	# 4.OPAKOVANI postup

	# 5.NOVE formatovani stringu ve funkci print()

		# 6.OPAKOVANI aplikuji dalsi funkci
        # 6a. (F2)vytiskni stav a ziskej tip hrace
        # 6b. (F3)nahrad podtrzitka a vytiskni uspesnot hadani

		# 7.OPAKOVANI odectu pokus
		# 8.OPAKOVANI vypis vyhra/prohra

    # (F2)
	# 9.NOVE tisknu aktualni stav hry

	# 10.NOVE vracet True/ False podle input()

    # (F3)
	#11.OPAKOVANI pomocna promenna pro - kolik jsem uhodl pismen
	#12.OPAKOVANI prochazime pismena ve schovanem slove
		#13.OPAKOVANI pokud se tip a pismeno shoduji...
			#... nahradim podtr. na indexu konkretnim pismenem
			#... a zvysim pocet pomocne promenne

	#14.NOVE hlasim, kolik jsem nasel pismen
	#15.NOVE hlasim, ze toto pismeno neni ve slove


# (RUNNING THE CODE)
#16.NOVE neresit
	#18.NOVE nacteme si soubor v rezimu "r", opatrne na jmeno souboru
	#19.NOVE nastavime si kurzor na nulu
	#20.NOVE projdeme rozdeleny soubor a appendujeme slova
	#21.NOVE nakonec soubor zavreme, abychom ho dale nenechavali otevreny
	#22.OPAKOVANI zavolam funkci pro nas seznam

    # nase_slova = ['Hangman', 'available', 'increase']

    # OPAKOVANI spoustim hlavni funkci
