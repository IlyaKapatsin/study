from function import Excellent_students
def main():
    A= []
    B = []
    Na = int(input("Введите количество отличников в прошлом году\n"))
    print("Введите отличников прошлого года\n")
    for i in range(Na):
        A.append(input())
    Nb = int(input("Введите количество отличников в этом году\n"))
    print("Введите отличников этого года\n")
    for i in range(Nb):
        B.append(input())
    Excellent_students (B,A,Nb,Na)
if __name__ == '__main__':
    main()
