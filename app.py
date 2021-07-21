weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")
weight_kg = float(weight) * 0.45
weight_lbs = float(weight) * 2.2

if unit == str("L") or str("l"):
    print("You weigh " + str(weight_kg) + " kilos.")
elif unit == str("K") or str("k"):
    print("You weigh" + str(weight_lbs) + " lbs.")
