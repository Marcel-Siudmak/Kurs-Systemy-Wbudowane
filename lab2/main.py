def main():
    val = None
    
    while True:
        if val is None:
            inp = input("Podaj liczbę lub wyjdź (q): ")
            if inp == "q": return
            try:
                val = int(inp)
            except ValueError:
                print("niedozwolona wartość")
                continue

        sys = input("podaj system lub wyjdź (bin, hex, q): ")
        while sys not in ("bin", "hex", "q"):
            sys = input("nieprawidłowa wartość.\npodaj system (bin, hex): ")
        
        if sys == "q":
            return
        elif sys == "bin":
            print("\n", val, "=", bin(val), "\n")
        elif sys == "hex":
            print("\n", val, "=", hex(val), "\n")

        ans = input("co chcesz zrobić?\n1) Inny system\n2) Nowa liczba\n3) Wyjdź\n")
        while ans not in ("1", "2", "3"):
            ans = input("niedozwolona wartosc\nwybierz (1, 2, 3): ")

        if ans == "3":
            return
        elif ans == "2":
            val = None
            
main()
