import datetime as dt

print("Print Zone", dt.datetime.now())

print("only date", dt.datetime.now().date())
print("only time", dt.datetime.now().time())
print("only day", dt.datetime.now().day)
print("weekend", dt.datetime.now().weekday())
print("month", dt.datetime.now().month)

d = "17-09-1999"
d2 = dt.datetime.now().date()
print(d, type(d))

d1 = dt.datetime.strptime(d, '%d-%m-%Y').date()
print(d1)

dn = dt.datetime.now().date()
print(dn)

if dn == d1:
    print("both are same date")
elif dn > d1:
    print("dn is greater")
else:
    print("d1 is greater")
