import os, random, platform, time

def cls():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

user_input = input("[+] Enter Your Mail-ID -> ")
ssss = int(input("[+] Amount to create -> "))

sus = user_input.split('@')[0]
why = user_input.split('@')[1]
gen = [f"{sus}+{random.randint(1000, 9999)}@{why}" for _ in range(ssss)]

with open('generated_mails.txt', 'w') as file:
    for email in gen:
        print(f"[+] Mail created with address -> {email}")
        file.write(email + '\n')

time.sleep(5)
cls()
print("[+] Done")
