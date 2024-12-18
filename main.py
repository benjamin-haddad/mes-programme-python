
nom  = input("Quelle est ton nom ? ")


age = 0
while age == 0:

    age_str  = input("quelle est votre age ? ")
    try:
        age = int(age_str) 
    except:
        print("ERREUR vous devez rentrer un nombre pour l'age")








    print (" vous vous appeler " + nom  + ", vous avez " + str (age) + " ans " )

    print("l'an prochain vous aurez " +str(age+1) + " ans")

#print("ERRREUR vous devez rentrer un nombre pour l'age")




"""
while (age n'est pas correct)
      demander l'age

      afficher la suite 
"""