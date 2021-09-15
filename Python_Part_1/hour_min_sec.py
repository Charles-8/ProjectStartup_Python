sec_str = input("Digite a quantidade de segundos para conversão")
total_sec = int(sec_str)
hour = total_sec // (60*60)
minutes = (total_sec // 60) % 60
seconds = total_sec % 60

print(hour," Horas ", minutes, "Minutos","e ", seconds," segundos")

