import random
name = ['Abas','Namdar', 'Sievasch', 'Mahtab']
random_name = random.choice(name).lower()
period = len(random_name)
line = ['_'] * len(random_name)

print(f'Your name has {' '.join(line)} letters')
wort = []
while period != 0:
    client = input('Please guess words name:')
    if client.isalpha():
        if client in random_name:  #client.count(client) == random_name.count(random_name)
            if client in line:
                print('You have guessed before')
            else:
                for ky,char in enumerate(random_name):
                    if char == client:
                        line[ky] = char
                a =' '.join(line)
                print(f'You are right, the word is {a}')
                if not '_' in line:
                    print('You win!')

        else:
            period -=1
            if period !=0:
                print('try again, it is false')
            if period == 0 and '_' in line:
                print('You lose')
    else:
        print('Please enter letters only')




