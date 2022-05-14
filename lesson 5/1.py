
def month(m):
    if m(1):
        print("Січень")
    elif m(2):
        print("Лютий")
    elif m(3):
        print("Березень")
    elif m(4):
        print("Квітень")
    elif m(5):
        print("Травень")
    elif m(6):
        print("Червень")
    elif m(7):
        print("Липень")
    elif m(8):
        print("Серпень")
    elif m(9):
        print("Вересень")
    elif m(10):
        print("Жовтень")
    elif m(11):
        print("Листопад")
    elif m(12):
        print("Грудень")            
    else:
        return "Введіть число від 1 до 12"
result = month(int(input("Enter Months:")))       

