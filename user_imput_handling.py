
def user_imput_1_to(max_Zahl: int):
    while True:
        try:
            x=int(input().strip())
            if (x >= 1) and (x <= max_Zahl):
                return x
            else:
                raise ValueError("Falsche Zahl")
        except:
            print(f"Falsche eingabe 1-{max_Zahl} eingeben")

def user_imput_n0_y1():
    y= ["y","yes","ye","j","ja","1","ya"]
    n= ["n","no","0","nein","nei","ne"]
    while True:
        try:
            x=input().lower().strip()
            if x in y:
                return 1
            elif x in n:
                return 0
            else:
                raise ValueError("Falsche Eingabe")
        except:
            print(f"Falsche eingabe ja / Nein")