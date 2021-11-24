from math import gcd
class kasr:
    def __init__(self, sk = 0, mk = 1):
        self.sk= sk
        self.mk= mk
    def sade(self, kasr):
        s = gcd(kasr.sk, kasr.mk)
        kasr.sk, kasr.mk = kasr.sk/ s, kasr.mk/ s
        return kasr
    def get_sk(self):
        return self.sk
    def get_mk(self):
        return self.mk
    def __repr__(self):
        return str(self.sk) + "/" + str(self.mk)
    def __add__(self, other):
        sk= self.get_sk() * other.get_mk() + other.get_sk() * self.get_mk()
        mk= self.get_mk() * other.get_mk()
        return self.sade(kasr(sk, mk))
    def __sub__(self, other):
        sk= self.get_sk() * other.get_mk() - other.get_sk() * self.get_mk()
        mk= self.get_mk() * other.get_mk()
        return self.sade(kasr(sk, mk))
    def __mul__(self, other):
        if self.sk == 0 or other.sk == 0:
            return 0
        else:
            sk = self.get_sk() * other.get_sk()
            mk = self.get_mk() * other.get_mk()
            return self.sade(kasr(sk, mk))
    def __truediv__(self, other):
        if self.sk == 0:
            return 0
        else:
            sk = self.get_sk() * other.get_mk()
            mk = self.get_mk() * other.get_sk()
            return self.sade(kasr(sk, mk))
def show_menu():
    print("1) jam | 2) tafriq | 3) zarb | 4) taqsim  | 5) Exit")
def get_kasr():
    sk = int(input("sorat kasr : "))
    mk = int(input("makhraj kasr : "))
    return sk, mk
def main():
    sk, mk = get_kasr()
    kasr1 = kasr(sk, mk)
    sk, mk = get_kasr()
    kasr2 = kasr(sk, mk)
    while True:
        show_menu()
        choice = abs(int(input()))
        if choice == 1:
            print( kasr1 + kasr2)
        elif choice == 2:
            print( kasr1 - kasr2)
        elif choice == 3:
            print( kasr1 * kasr2)
        elif choice == 4:
            print( kasr1 / kasr2)
        elif choice == 5:
            exit()
if __name__ == "__main__":
    main()