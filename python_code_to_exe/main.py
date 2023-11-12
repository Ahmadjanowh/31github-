# Простая программа
def sum(a,b):
    result = a + b
    
    with open('result.txt','w',encoding='utf-8') as f:
        f.write(str(result))

def main():
    a = int(input("Enter a : "))
    b = int(input("Eter b :"))

    sum(a,b)

# Введите команду auto-py-to-exe чтобы начать создавать exe файл 
# Дале следуйте инструкциям 

if __name__=='__main__':
    main()