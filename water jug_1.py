def water_jug():
    jug1 = 0   # 5 liter jug
    jug2 = 0   # 3 liter jug

    print("Jug1  Jug2")

    while jug1 != 4:
        if jug1 == 0:
            jug1 = 5   # Fill Jug1

        elif jug2 == 3:
            jug2 = 0   # Empty Jug2

        else:
            # Pour Jug1 -> Jug2
            transfer = min(jug1, 3 - jug2)
            jug1 -= transfer
            jug2 += transfer

        print(jug1, "   ", jug2)

water_jug()
