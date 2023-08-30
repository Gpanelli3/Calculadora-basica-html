import cgi
from funciones import suma,resta

#headers
print("Content-Type: text/html")
print()

print("<html>")
form = cgi.FieldStorage()


primerNumero=int(form["numero-uno"].value)
segundoNumero=int(form["numero-dos"].value)
option=form["operacion"].value

if option=="sumar":
    sumatoria=suma(primerNumero,segundoNumero)
    print("la suma es: ", sumatoria)

elif option=="multiplicar":
    mult=primerNumero*segundoNumero
    print("el resultado es:", mult)

elif option=="dividir":
    div=primerNumero/segundoNumero
    print("el resultado es:", div)
elif option=="restar":
    restar=resta(primerNumero,segundoNumero)
    print("el resultado es:", restar)

print("</html>")