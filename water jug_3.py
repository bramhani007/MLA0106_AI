def three_jugs():

    j3, j5, j8 = 0, 0, 8

    print("Jug1  Jug2  Jug3")
    print(j3, "   ", j5, "   ", j8)

    # 8 -> 5
    t = min(j8, 5-j5)
    j8 -= t; j5 += t
    print(j3, "   ", j5, "   ", j8)

    # 5 -> 3
    t = min(j5, 3-j3)
    j5 -= t; j3 += t
    print(j3, "   ", j5, "   ", j8)

    # 3 -> 8
    t = min(j3, 8-j8)
    j3 -= t; j8 += t
    print(j3, "   ", j5, "   ", j8)

    # 5 -> 3
    t = min(j5, 3-j3)
    j5 -= t; j3 += t
    print(j3, "   ", j5, "   ", j8)

    # 8 -> 5
    t = min(j8, 5-j5)
    j8 -= t; j5 += t
    print(j3, "   ", j5, "   ", j8)

    # 5 -> 3
    t = min(j5, 3-j3)
    j5 -= t; j3 += t
    print(j3, "   ", j5, "   ", j8)

    # 3 -> 8  (Final)
    t = min(j3, 8-j8)
    j3 -= t; j8 += t
    print(j3, "   ", j5, "   ", j8)

three_jugs()
