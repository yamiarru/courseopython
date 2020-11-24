def computepay(hrs, rate):
     if hrs > 40:
        p = (hrs - 40) * 1.5 * rate + 40 * rate
     else:
        p = hrs * rate
     return p
h = input("Enter Hours:")
hrs = float(h)
r = input("Enter Rate:")
rate = float(r)
p = computepay(hrs, rate)
print("Pay", p)
