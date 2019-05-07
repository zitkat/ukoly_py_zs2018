seznam_1 = ['kocka', 'pes', 'kralik', 'had']
seznam_2 = ['lev', 'pes', 'tygr', 'had']



def vytvor_seznamy(seznam1, seznam2):
    sAs = []
    sNs = []
    s1ms2 = []
    s2ms1 = []

    for prvek in seznam1 + seznam2:
        if prvek in seznam1 and prvek in seznam2:
            sAs.append(prvek)
        if prvek not in sNs:
            sNs.append(prvek)

        if prvek not in seznam2:
            s1ms2.append(prvek)
        if prvek not in seznam1:
            s2ms1.append(prvek)
    return sAs, sNs, s1ms2, s2ms1



print(vytvor_seznamy(seznam_1, seznam_2))


