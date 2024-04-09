total_price = 0
tickets = int(input("Введите количество билетов:"))
for age in range (tickets):
    age = int(input("Введите возраст:"))
    if age <18:
        total_price += 0
    elif age >=18 and age <=25:
        total_price += 990
    elif age >=25:
        total_price += 1390
if total_price == 0:
    print ("Welcome")
else:
    print("Стоимость билетов - ", "%.2f" % total_price)

if tickets > 3:
    skidka = total_price / 100 * 10
    print("Ваша скидка - ", "%.2f" % skidka)
    print("Итого:" ,"%.2f" % (total_price - skidka))
