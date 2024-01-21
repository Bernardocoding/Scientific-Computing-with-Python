def add_time(start, duration, weekday=None):
  lst_week = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
  ]
  duration_min = ""

  if "PM" in start:  # tranforma em padrão 24h
    lst_24h = start.split(":")
    lst_24h[0] = str(int(lst_24h[0]) + 12)
  else:
    lst_24h = start.split(":")

  lst_duration = duration.split(":")
  sum_hours = int(lst_duration[0]) + int(
    lst_24h[0])  # soma as horas iniciais com as de duração

  for i in lst_24h[1]:  # loop para pegar o num das horas iniciais
    if i.isdigit() == True:
      duration_min += i
  min = int(duration_min) + int(
    lst_duration[1]
  )  # soma os minutos iniciais com os de duração, se for menor que 60 eh o final
  # return print(sum_hours, min, weekday)

  if min >= 60:
    sum_hours += min // 60  # horas totais
    min = min % 60  # minutos finais

  days = sum_hours // 24  # dias que passaram considerando horas totais
  hours = sum_hours % 24  # horas finais
  # return print(days, hours, min)  # ATÉ AQUI ESTÁ OK!
  # até aqui estamos no padrão 24H
  if weekday:  # COM WEEKDAY
    weekday = weekday.lower()  # formatar week day
    weekday = weekday[0].upper() + weekday[1:]  # formatar weekday
    # return print(weekday)  # ATÉ AQUI ESTÁ OK!
    if days == 0 and hours < 12:  # caso Sem next day AM
      if hours == 0:  # caso seja meia noite
        return "{}:{:02d} AM {}".format(hours + 12, min,
                                        lst_week[lst_week.index(weekday)])

      else:
        return "{}:{:02d} AM {}".format(hours, min,
                                        lst_week[lst_week.index(weekday)])

    elif days == 0 and hours >= 12:  # caso Sem next day PM
      if hours == 12:
        return "{}:{:02d} PM, {}".format(hours, min,
                                         lst_week[lst_week.index(weekday)])

      else:
        return "{}:{:02d} PM, {}".format(hours - 12, min,
                                         lst_week[lst_week.index(weekday)])

    elif days == 1 and hours < 12:  # caso next day AM
      if hours == 0:
        return "{}:{:02d} AM, {} (next day)".format(
          hours + 12, min, lst_week[lst_week.index(weekday) + 1])
      else:
        return "{}:{:02d} AM, {} (next day)".format(
          hours, min, lst_week[lst_week.index(weekday) + 1])
    elif days == 1 and hours >= 12:  # caso next day PM
      if hours == 12:
        return "{}:{:02d} PM, {} (nextday)".format(
          hours, min, lst_week[lst_week.index(weekday) + 1])

      else:
        return "{}:{:02d} PM, {} (nextday)".format(
          hours - 12, min, lst_week[lst_week.index(weekday) + 1])

    elif days > 1 and hours >= 12:  # days later e weekday PM
      ind = lst_week.index(weekday)
      count = 0  # regula quants vezes o loop tem que loopar
      while count != days:
        ind += 1
        count += 1

        if ind <= 6:  # regula para o index não sair o range da lista
          weekday = lst_week[ind]
        else:
          weekday = lst_week[0]
          ind = 0
      if hours == 12:
        return "{}:{:02d} PM, {} ({} days later)".format(
          hours, min, weekday, days)

      else:
        return "{}:{:02d} PM, {} ({} days later)".format(
          hours - 12, min, weekday, days)

    elif days > 1 and hours < 12:  # days later e weekday AM
      ind = lst_week.index(weekday)
      # return print(ind)
      count = 0  # regula quants vezes o loop tem que loopar
      while count != days:  # loop para saber dia da semana
        ind += 1
        count += 1

        if ind <= 6:  # regula para o index não sair o range da lista
          weekday = lst_week[ind]
        else:
          weekday = lst_week[0]
          ind = 0
      # print(count, ind)

      if hours == 0:
        return "{}:{:02d} AM, {} ({} days later)".format(
          hours + 12, min, weekday, days)

      else:
        return "{}:{:02d} AM, {} ({} days later)".format(
          hours, min, weekday, days)
  # print(hours, min, weekday, days)

  if weekday == None:  # SEM WEEKDAY
    if days == 0 and hours < 12:  # caso SEM next day AM
      if hours == 0:  # caso seja meia noite
        return "{}:{:02d} AM".format(hours + 12, min)
      else:
        return "{}:{:02d} AM".format(hours, min)
    elif days == 0 and hours >= 12:  # caso SEM next day PM
      if hours == 12:
        return "{}:{:02d} PM".format(hours, min)
      else:
        return "{}:{:02d} PM".format(hours - 12, min)

    elif days == 1 and hours < 12:  # caso  next day AM
      if hours == 0:  # caso seja meia noite
        return "{}:{:02d} AM (next day)".format(hours + 12, min)
      else:
        return "{}:{:02d} AM (next day)".format(hours, min)

    elif days == 1 and hours >= 12:  # caso next day PM
      if hours == 12:
        return "{}:{:02d} PM (next day)".format(hours, min)
      else:
        return "{}:{:02d} PM (next day)".format(hours - 12, min)

    elif days > 1 and hours >= 12:  # caso days later PM
      if hours == 12:
        return "{}:{:02d} PM ({} days later)".format(hours, min, days)
      else:
        return "{}:{:02d} PM ({} days later)".format(hours - 12, min, days)

    elif days > 1 and hours < 12:  # caso days later AM
      if hours == 0:  # caso seja meia noite
        return "{}:{:02d} AM ({} days later)".format(hours + 12, min, days)
      else:
        return "{}:{:02d} AM ({} days later)".format(hours, min, days)

#TESTE
#add_time("11:59 PM", "24:05", "Wednesday")
