import datetime

def formatar_data(dia, mes, ano):
    data = datetime.date(ano, mes, dia)

    print(data.strftime("%d/%m/%Y"))

formatar_data(11, 4, 2025)
formatar_data(ano=2025, dia=11, mes=4)
