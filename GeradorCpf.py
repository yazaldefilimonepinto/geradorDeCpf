import time
import re
import random
print("\033[1;92m~"*58)
print("\033[1;92m~"*20+"\033[1;91mGerador CPF Master\033[m"+"\033[1;92m~"*20)
print('''\033[1;93m
    \033[1;91m[✓]Author:\033[m Yazalde Felimone Pinto

    \033[1;91m[✓]Github:\033[m https://github.com/YazaldeFP 
    \033[1;91m[✓]Nome Artistico:\033[m [•]Imperador

    \033[1;91m[✓]E-Mail:\033[m fillmorningstar@gmail.com

        ''')
print("\033[1;92m~\033[m"*58)
print("\033[1;92m~\033[m"*58)
time.sleep(2)
N_cpf=int(input("\033[1;91m[✓]Author:Yazalde[✓]=>>\033[m Quantos cpfs dezejas?: ")) 
def get_digit(cpf: str) -> int:
    len_cpf = len(cpf) + 1
    multation = []
    for cpf_index,multipler in enumerate(range(len_cpf, 1,-1)):
        multation.append(int(cpf[cpf_index]) * multipler)
    total_soma = sum(multation)
    digit = 11 - (total_soma % 11)
    return digit if digit < 10 else 0


def get_digit_one(cpf: str) -> int:
    return get_digit(cpf[:9])


def get_digit_two(cpf: str) -> int:
    return get_digit(cpf[:10])


def remove_not_number(cpf: str) -> str:
    return re.sub(r'\D','',cpf)

def has_eleven_chars(value: str) -> bool:
    return len(value) == 11


def is_sequece(value: str) -> bool:
    return (value[0] * len(value)) == value


def is_valid(cpf: str) -> bool:
    clean_cpf = remove_not_number(cpf)
#    print(clean_cpf)

    if not has_eleven_chars(cpf):
       return False

    if is_sequece(clean_cpf):
        return False #fa

    digit_one = get_digit_one(clean_cpf)
    print(digit_one)
    digit_two = get_digit_two(clean_cpf)
    print(digit_two)
    new_cpf = f'{clean_cpf[:9]}{digit_one}{digit_two}'
    if new_cpf == clean_cpf:
        return True
    return False

def gernerate() -> str:
    nine_digits=''.join([str(random.randint(0, 9)) for x in range(9)])
    digit_one = get_digit_one(nine_digits)
 #   print(digit_one)
    digit_two = get_digit_one(f'{nine_digits}{digit_one}')
    new_cpf = f'{nine_digits}{digit_one}{digit_two}'
#    print(digit_two)
#    print(nine_digits)
    return new_cpf

def formater(cpf:str) -> str:
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
if __name__ == "__main__":
    print(is_valid('488.611.340-09'))
 #   print(is_valid('488.661.120-39'))
#    print(is_valid('111.111.111-11'))
    #for i in range(N_cpf):

     #   cpf=gernerate()
      #  cpf_formate=formater(cpf)
    print("\033[1;92m~"*58)
    print('\033[1;92m~'*20+f'\033[1;91mGerando {N_cpf} CPF\033[m'+'\033[1;92m~'*20)
    time.sleep(1)
    print("\033[1;92m~"*20+"\033[1;91mGerador CPF Master\033[m"+"\033[1;92m~"*20)
    print('''\033[1;93m
        \033[1;91m[✓]Author:\033[m Yazalde Felimone Pinto

        \033[1;91m[✓]Github:\033[m https://github.com/YazaldeFP 
    
        \033[1;91m[✓]Nome Artistico:\033[m[•]Imperador

        \033[1;91m[✓]E-Mail:\033[m fillmorningstar@gmail.com

            ''')
    print("\033[1;92m~\033[m"*58)
    print("\033[1;92m~\033[m"*58)
    time.sleep(2)
    for i in range(N_cpf):
        cpf=gernerate()
        cpf_formate=formater(cpf)

        time.sleep(1)
        print("\033[1;91m[✓]Author:Yazalde[✓]=>>\033[m" +cpf)
        print("\033[1;92mArumanto...")
        print("\033[1;92m Disponha=>>\033[m"+ cpf_formate)
        print()
        time.sleep(1)


