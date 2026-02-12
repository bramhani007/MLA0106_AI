def three_jug():

    j12, j8, j5 = 12, 0, 0

    print("Jug1  Jug2  Jug3")
    print(j12, "   ", j8, "   ", j5)

    # 12 -> 8
    t = min(j12, 8-j8)
    j12 -= t; j8 += t
    print(j12, "   ", j8, "   ", j5)

    # 8 -> 5
    t = min(j8, 5-j5)
    j8 -= t; j5 += t
    print(j12, "   ", j8, "   ", j5)

    # 5 -> 12
    t = min(j5, 12-j12)
    j5 -= t; j12 += t
    print(j12, "   ", j8, "   ", j5)

    # 8 -> 5
    t = min(j8, 5-j5)
    j8 -= t; j5 += t
    print(j12, "   ", j8, "   ", j5)

    # 12 -> 8
    t = min(j12, 8-j8)
    j12 -= t; j8 += t
    print(j12, "   ", j8, "   ", j5)

    # 8 -> 5
    t = min(j8, 5-j5)
    j8 -= t; j5 += t
    print(j12, "   ", j8, "   ", j5)

    # 5 -> 12
    t = min(j5, 12-j12)
    j5 -= t; j12 += t
    print(j12, "   ", j8, "   ", j5)

three_jug()
