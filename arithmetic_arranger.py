def arithmetic_arranger(problemas, solucoes = False):

  if len(problemas) > 5:
    return "Error: Too many problems."

  parcela1, parcela2, linha, total = ["","","",""]

  for problema in problemas:
    numero1, digito, numero2 = problema.split()

    if not numero1.isdigit() or not numero2.isdigit():
      return "Error: Numbers must only contain digits."
    
    if len(numero1) > 4 or len(numero2) > 4:
        return "Error: Numbers cannot be more than four digits."
    
    if digito != "+" and digito != "-":
      return "Error: Operator must be '+' or '-'."
    
    if digito == "+":
      resultado = str(int(numero1) + int(numero2))
    else:
      resultado = str(int(numero1) - int(numero2))

    tamanho_string = max(len(numero1), len(numero2))

    parcela1 += numero1.rjust(tamanho_string+2)
    parcela2 += digito + numero2.rjust(tamanho_string+1)
    linha += "-" * (tamanho_string+2)
    total += resultado.rjust(tamanho_string+2)

    if problemas.index(problema) < len(problemas)-1:
      parcela1 += 4 * " "
      parcela2 += 4 * " "
      linha += 4 * " "
      total += 4 * " "

  problemas_arranjados = parcela1 + "\n" + parcela2 + "\n" + linha

  if solucoes:
    problemas_arranjados += "\n" + total

  return problemas_arranjados