names = ['Charles', 'Grazielly', 'Giovani', 'any', 'Gelson', 'Eliane', 'Elaine', 'Anderson']
def shorter_name(name_list):
    shorter = 100
    for i in name_list:
        if len(i) <= shorter:
            shorter = len(i)
            shorter_name = i

    print(shorter_name.capitalize())

shorter_name(names)


