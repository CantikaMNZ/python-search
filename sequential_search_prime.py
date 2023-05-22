def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True
    
def find_prime_numbers(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

#Daftar bilangannya
numbers = [7, 10, 13, 6, 17, 22, 19]

#Menemukan bilangan prima
prime_numbers = find_prime_numbers(numbers)

#Menampilkan bilangan prima yang ditemukan
print("Bilangan prima dalam daftar:", prime_numbers)