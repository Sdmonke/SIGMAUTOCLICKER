num = input("What key should start SIGMAUTOCLICKER?")
cps = input("Type a number like 0.0001, add more 0s for faster cps")
print("")
revs_cps = 0

while (cps > 0):
    remainder = cps % 10
    revs_number = (revs_cps * 10) + remainder
    cps = cps // 10