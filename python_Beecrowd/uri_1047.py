h1, m1, h2, m2 = [int(x) for x in input().split()]

if h1 < h2:
    if m1 < m2:
        print(f"O JOGO DUROU {h2 - h1} HORA(S) E {(m2 - m1)} MINUTO(S)")
    if m1 > m2:
        print(f"O JOGO DUROU {(h2 - h1) - 1} HORA(S) E {60 - (m1 - m2)} MINUTO(S)")
    if m1 == m2:
        print(f"O JOGO DUROU {h2 - h1} HORA(S) E {(m1 - m2)} MINUTO(S)")
if h1 == h2:
    if m1 < m2:
        print(f"O JOGO DUROU {0} HORA(S) E {m2 - m1} MINUTO(S)")
    if m1 > m2:
        print(f"O JOGO DUROU {(24) - 1} HORA(S) E {60 - (m1 - m2)} MINUTO(S)")
    if m1 == m2:
        print(f"O JOGO DUROU {(24)} HORA(S) E {(m1 - m2)} MINUTO(S)")
if h1 > h2:
    if m1 < m2:
        print(f"O JOGO DUROU {(24 - (h1 - h2))} HORA(S) E {(m2 - m1)} MINUTO(S)")
    if m1 > m2:
        print(f"O JOGO DUROU {24 - (h1 - h2) -1} HORA(S) E {60 -(m1 - m2)} MINUTO(S)")
    if m1 == m2:
        print(f"O JOGO DUROU {h1 - h2} HORA(S) E {(m1 - m2)} MINUTO(S)")

