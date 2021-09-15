sec_str = int(input("Digite a quantidade de segundos para conversão"))

day = sec_str // (60 * 60 * 24)
hour = (sec_str // 60 * 60) % 24
minutes = (sec_str // 60) % 60
seconds = sec_str % 60

print(day, "Dias ", hour, " Horas ", minutes, "Minutos", "e ", seconds, " segundos")
