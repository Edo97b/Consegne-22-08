import http.client

host= input("inserisci l'host del sistema target")
port = input("inserisci la porta del sistema target")
perc = input("inserisci percorso del sistema target")

if port == "": port = 80
if perc == '': perc = '/'

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request("Options", perc)
    response = connection.getresponse()
    print("I metodi abilitati sono: ", response.getheader("Allow"))
    connection.close()
except ConnectionRefusedError:
    print("Connessione fallita")