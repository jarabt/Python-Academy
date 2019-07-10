# 0.OPAKOVANI importovani modulu
import random

nase_slova = ['Hangman', 'available', 'increase']

    # (F1)
	# 1.OPAKOVANI vlozime jmeno hrace
	# 2.OPAKOVANI nahodne slovo z listu, jakou metodu pouzijeme?
	# 3.OPAKOVANI podle delky pocet pokusu
	# 4.OPAKOVANI postup

def main(nase_slova):

    jmeno_hrace = input('Tvoje prezdivka: ')
    vybrane_slovo = random.choice(nase_slova)
    print(vybrane_slovo)
    pocet_pokusu = len(vybrane_slovo) * 2
    postup = ['_'] * len(vybrane_slovo)

    # print('\nDalsi bude hrac ' + jmeno_hrace + ', tedy zacneme!')
    # print('\nHrac: ' + jmeno_hrace + '\tTvuj postup: ' + ' '.join(postup) + '\tZbyva pokusu: ' + str(pocet_pokusu))

	# 5.NOVE formatovani stringu ve funkci print()
    print('\nDalsi bude hrac {}, tedy zacneme! '.format(jmeno_hrace))
    print('\nHrac: {}\tTvuj postup: {} \tZbyva pokusu: {}'.format(jmeno_hrace, ' '.join(postup), pocet_pokusu))

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
if __name__ == '__main__':
	#18.NOVE nacteme si soubor v rezimu "r", opatrne na jmeno souboru
	#19.NOVE nastavime si kurzor na nulu
	#20.NOVE projdeme rozdeleny soubor a appendujeme slova
	#21.NOVE nakonec soubor zavreme, abychom ho dale nenechavali otevreny
	#22.OPAKOVANI zavolam funkci pro nas seznam

    # nase_slova = ['Hangman', 'available', 'increase']

    # OPAKOVANI spoustim hlavni funkci
    main(nase_slova)
