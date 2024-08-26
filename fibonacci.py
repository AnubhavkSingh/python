n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Incorrect input")
else:
    a = 0
    b = 1
    
    if n == 1:
        sum = a
        print(a)
    else:
        sum = a + b
        print(a, b, end=" ")

        for i in range(2, n):
            c = a + b
            print(c, end=" ")
            sum += c
            a = b
            b = c

    print(f"\nSum of the Fibonacci series: {sum}")
