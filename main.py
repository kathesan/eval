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
def verifUrl_F4(url):
  #print("hello")
  format= url.count('.')

  if format == 1 :
    str = url.split('.')
    x, y = str

    if len(y) <= 3:
      return True
    else:
      print("url mal formee")
      return False

  else:
    print("url mal formee")
    return False


###### exercice 03
def getTLD_N5(url):
  #print("hello")
  res = verifUrl_F4(url)

  if res == True:
    b = url.split('.')
    return b[1]
  else:
    print("TLD mal formee")
    return False

###### exercice 04
def VerifLDT_J5(tldOk, tld):
  #print("hello")

  for i in tldOk:
    if tld == i:
      return True

  print("TLD absente")
  return False

###### exercice 05
def ipVerifFormat_I5(adresseIp): 
  print("hello")

  c = adresseIp.split('.')

  for e in c:
    if int(e) < 0 or int(e) > 255:
      print("champ d'adresse incorrect")
      return False

  return True

  if len(c) != 4:
    print("nombre de champ incorrect")
    return False



###### exercice 06
def makeTLD_A2(resolDns):
  print("hello")
  print (resolDns.keys())

  for d in resolDns.keys():
    str = d.split('.')
    #x, y

# Zone 2 ## zone pour les classes
###### exercice 07
class serveurDns_V2 :
  def __init__(self, resolDns):
    self.resolDns = resolDns
  
    
###### exercice 08
def resoltDns(self, url):
  result = verifUrl_F4(url)
  if result:

    return True
  else:

    print("erreur de format de l'url")
    return False

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
  #resolDns = makeDico_E6("dns.txt", ",")
  #print(resolDns)

	###### exercice 02
  print("exercice 02 #######################")
  result = verifUrl_F4("Amazon.fr")
  #print(result)

	###### exercice 03
  print("exercice 03 #######################")
  #result = VerifLDT_J5("Amazon.fr")
  #print(result)

	###### exercice 04
  print("exercice 04 #######################")
  #result = VerifLDT_J5(["fr","com","net"],"fr")
  #print(result)

	###### exercice 05
  print("exercice 05 #######################")
  result = ipVerifFormat_I5("178.236.6.242")
  print(result)

	###### exercice 06
  print("exercice 06 #######################")
  #tldOk = makeTLD_A2(dico)
  #print(result)

	# Zone 4 ## zone pour les tests de la classe

	###### exercice 07
  print("exercice 07 #######################")

  #print(result)
	###### exercice 08
  print("exercice 08 #######################")

  #print(result)
	###### exercice 09
  print("exercice 09 #######################")

  #print(result)

	###### exercice 10
  print("exercice 10 #######################")

  #print(result)

if __name__=="__main__":
  print("main()")
  main()