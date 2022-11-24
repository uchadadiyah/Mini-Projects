import random
uppercase_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercaase_letter = uppercase_letter.lower()
digits = "0123456789"
symbols = "(){}[],;:.-+/\@&#$%"

upper,lower, nums, syms = True, True, True, False

all = ""

if upper:
    all += uppercase_letter
if lower:
    all += lowercaase_letter
if nums:
    all += digits
if syms:
    all += symbols

length = 20
amount = 10

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)