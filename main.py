# Zone 1 ## zone pour les fonctions
# exercice 00 (la fonction est definie dans cette zone)
def exempleHello (msg):
  return "bonjour {}, comment allez-vous ?".format(msg)

###### exercice 01
def makeDico_E6(nomFichier, sep):
  print("creation du dico")

  dico={}

  f = open(nomFichier,"r")

  for i in range (0,80):

    ligne = f.readline().split(sep)
    dico[ligne[0]] = ligne[1].replace("\n","")

  f.close()
  return dico

###### exercice 02
def verifUrl_F4():
  print("hello")

###### exercice 03
def getTLD_N5():
  print("hello")

###### exercice 04
def VerifLDT_J5():
  print("hello")

###### exercice 05
def ipVerifFormat_I5(): 
  print("hello")   

###### exercice 06
#def makeTLD_A2():

# Zone 2 ## zone pour les classes
###### exercice 07


###### exercice 08


###### exercice 09
    

# Zone 3 ## zone pour les tests des fonctions

def main() :
  from re import split
	###### exercice 00 (la fonction est appelee dans cette zone afin de confirmer son fonctionnement)
  print("exercice 00 #######################")
  salutations = exempleHello("Michel")
  print(salutations)
  print(salutations.split(sep=" "))

	###### exercice 01
  print("exercice 01 #######################")
  resolDns = makeDico_E6("dns.txt", ",")
  #print(resolDns)
	###### exercice 02
  print("exercice 02 #######################")


	###### exercice 03
  print("exercice 03 #######################")


	###### exercice 04
  print("exercice 04 #######################")


	###### exercice 05
  print("exercice 05 #######################")


	###### exercice 06
  print("exercice 06 #######################")

	# Zone 4 ## zone pour les tests de la classe

	###### exercice 07
  print("exercice 07 #######################")


	###### exercice 08
  print("exercice 08 #######################")


	###### exercice 09
  print("exercice 09 #######################")
	
	###### exercice 10
  print("exercice 10 #######################")

if __name__=="__main__":
  print("main()")
  main()