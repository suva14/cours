import sys
def usage():
    print("python3 cypher.py cypher/decypher key msg")
if(sys.argv[1]=="cypher"):
    key=int(sys.argv[2])%26
elif (sys.argv[1]=="decypher"):
    key=-(int(sys.argv[2])%26)
else :
    print(f"commande non supportée: {sys.argv[1]}")
    usage()
    sys.exit(0)


result=""
for lettre in msg:
    result+= chr((ord(lettre)+key))
print(result)


