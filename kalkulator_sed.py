# Penjumlahan
def add(x, y):
    return x + y
# Pengurangan
def subtract(x, y):
    return x - y
# Perkalian
def multiply(x, y):
    return x * y
# Pembagian
def divide(x, y):
    return x / y
    
print("==========Calculator==========")
print("Pilih operasi.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Pilih operasi
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # Next atau End(break loop)         
        next_calculation = input("Lanjut? (ya/tidak): ")
        if next_calculation == "tidak":
          break
    else:
        print("Invalid Input")
