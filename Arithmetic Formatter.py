def arithmetic_arranger(problems, optional=False):
  first = ""
  second = ""
  result = ""
  lines = ""
  answer = ""
  FIRST = ""
  SECOND = ""
  LINES = ""
  RESULT = ""

  if len(problems) > 5:  # checar quant de operações
    return "Error: Too many problems."
  for operation in problems:  # checar sinal
    if "+" not in operation and "-" not in operation:
      return "Error: Operator must be '+' or '-'."
    lst_operant = operation.split()
    for cha in lst_operant:
      if len(cha) > 4:  # checar tamanho dos num
        return "Error: Numbers cannot be more than four digits."

      elif (cha.isdigit() == False and cha != "+"
            and cha != "-"):  # checar se são num
        return "Error: Numbers must only contain digits."

    lenght = (max(len(lst_operant[0]), len(lst_operant[2])) + 2
              )  # alinhar pela direita e saber quantidade de '_'
    if lst_operant[1] == "+":
      result = str(int(lst_operant[0]) + int(lst_operant[2])).rjust(lenght)
      second = "+" + lst_operant[2].rjust(lenght - 1)
    else:
      result = str(int(lst_operant[0]) - int(lst_operant[2])).rjust(lenght)
      second = "-" + lst_operant[2].rjust(lenght - 1)

    first = lst_operant[0].rjust(lenght)

    for i in range(lenght):
      lines += "-"
    if operation != problems[-1]:
      FIRST += first + "    "
      SECOND += second + "    "
      LINES += lines + "    "
      RESULT += result + "    "
    else:
      FIRST += first
      SECOND += second
      LINES += lines
      RESULT += result
    lst_operat = []
    lines = ""
  if optional:
    answer = FIRST + "\n" + SECOND + "\n" + LINES + "\n" + RESULT
  else:
    answer = FIRST + "\n" + SECOND + "\n" + LINES
  return answer
