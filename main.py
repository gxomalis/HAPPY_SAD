

goodlist=[]
badlist=[]

print("~Γειά!")
print("Σε αυτό το project θα διδάξουμε στον υπολογιστή ποιες φράσεις είναι ευγενικές,\nπ.χ. 'Είσαι όμορφος!', "
      "και ποιες όχι, π.χ. 'Μυρίζει η ανάσα σου'.\nΑνάλογα με την φράση, ο υπολογιστής θα δίνει μια φατσούλα που "
      "χαμογελάει, ή είναι λυπημένη.")
x=0
print("Δώσε τουλάχιστον 5 ευγενικές προτάσεις. Όταν θες να σταματήσεις, γράψε ΣΤΟΠ:  ")
while x!=1:
    phr=input()
    if phr=="ΣΤΟΠ":
        break
    else:
        goodlist.append(phr)

print("Τέλεια! Τώρα δώσε τουλάχιστον 5 άσχημες προτάσεις. Όταν θες να σταματήσεις, γράψε ΣΤΟΠ:  ")
x=0
while x!=1:
    phr=input()
    if phr=="ΣΤΟΠ":
        break
    else:
        badlist.append(phr)


print("Πες κάτι στον υπολογιστή! Θα αναγνωρίσει ένα κομπλιμέντο; Όταν θες να σταματήσεις γράψε ΣΤΟΠ")
phrase = input()
while phrase!="ΣΤΟΠ":
    flag1=0
    for index in goodlist:
        if goodlist.count(phrase)==1:
            flag1=1
    if flag1==1:
        print("(✿◠‿◠) Ευχαριστώ!")
    flag2=0
    for index in badlist:
       if badlist.count(phrase)==1:
           flag2=1
    if flag2==1:
        print("(╥﹏╥)")

    if flag1==flag2==0:
        flag3=0
        typos = input("Δεν γνωρίζω αυτή την πρόταση, γράψε μου αν είναι ΚΑΛΗ ή ΚΑΚΗ: ")
        while flag3==0: # έλεγχος απάντησης
            if typos== "ΚΑΛΗ":
                goodlist.append(phrase)
                print("(✿◠‿◠)")
                print("Δώσε μια άλλη πρόταση: ")
                flag3=1
            elif typos== "ΚΑΚΗ":
                badlist.append(phrase)
                print("(╥﹏╥)")
                print("Δώσε μια άλλη πρόταση: ")
                flag3=1
            else:
                print("Γράψε 'ΚΑΛΗ' αν η πρόταση ήταν ευγενική, αλλιώς γράψε 'ΚΑΚΗ'")
                typos=input()

    phrase = input()