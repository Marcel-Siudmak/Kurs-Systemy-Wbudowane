def main():
    val = None
    
    while True:
        if val is None:
            inp = input("Podaj liczbę lub wyjdź (q)\n> ")
            if inp == "q": return
            try:
                val = int(inp)
            except ValueError:
                print("niedozwolona wartość")
                continue

        sys = input("podaj system lub wyjdź (bin, hex, q)\n> ")
        while sys not in ("bin", "hex", "q"):
            sys = input("nieprawidłowa wartość.\npodaj system lub wyjdź (bin, hex, q)\n> ")
        
        if sys == "q":
            return
        elif sys == "bin":
            print("\n", val, "=", bin(val), "\n")
        elif sys == "hex":
            print("\n", val, "=", hex(val), "\n")

        ans = input("co chcesz zrobić?\n1) Inny system\n2) Nowa liczba\nq) Wyjdź\n> ")
        while ans not in ("1", "2", "q"):
            ans = input("niedozwolona wartosc\nwybierz (1, 2, q)\n> ")

        if ans == "q":
            return
        elif ans == "2":
            val = None
            
main()
