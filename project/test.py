from datetime import date

current_date = date.today()

format5 = current_date.strftime("%A, %B %d, %Y")

a = format5.split()


print(a)
print(format5)
print(type(format5))
