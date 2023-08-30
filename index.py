import cgi
#headers
print("Content-Type: text/html")
print()

print("""<html>
      <head><title>FOMRULARIO</title></head>

      
      <body>
        <h1>CALCULADORA</h1>
      
        <form method="post" action="main.py">
            <input type = "number" name="numero-uno">numero-1
            <br>
            <input type = "number" name="numero-dos">numero-2
            <br>
      
            <input type="radio" name="operacion" value="multiplicar">Multiplicar
            <br>
            <input type="radio" name="operacion" value="sumar">sumar
            <br>
            <input type="radio" name="operacion" value="restar">restar
            <br>
            <input type="radio" name="operacion" value="dividir">dividir
            <br>
            <button>Resultado</button>
        </form>
      
      </body>
    </html>""")





      