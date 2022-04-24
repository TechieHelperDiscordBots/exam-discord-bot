
# ["16/05/2022", "4ES1 01", "English as a Second Language", " Paper 1: Reading and Writing", "Afternoon", "2h 00m"],

while (a := input()) != "-1":
    a = a.split("\t")
    print("[\"" + a[0] + "\", \"" + a[4] + "\", \"" + a[5] + "\", \"", a[6] + "\", \"" + a[7] + "\", \"" + a[8] + "\"],")
