my_list = [1, 2, 3, 'x'] # Список з різнорідними елементами
my_tuple = (1, [2]) # кортеж - незмінна послідовність
my_dict = {'2':2, '3':3} # словник - невпорядкована послідовність
my_set = set((1, 2, 3, 2, 1)) # множина


necessityEnvelop = 0  # NEC, необхідні витрати
freedomEnvelop = 0    # FFA, фінансова свобода
educationEnvelop = 0  # EDU, освіта
longTermEnvelop = 0   # LTSS, резерв та на великі покупки
playEnvelop = 0       # PLAY, розваги
giveEnvelop = 0       # GIVE, подарунки

necRate = 0.55
ffaRate = 0.1
eduRate = 0.1
ltssRate = 0.1
playRate = 0.1
giveRate = 0.05

expectedIncome = 1000

print ("""Hello.\n
Ми заповнимо ваші конверти грошима, які ви тут введете!\n
Натисніть Ctrl+c, щоб вийти зі сценарію.
\n\n Будь ласка, введіть суму:""")

sum = 0

while (sum < expectedIncome):
    line = int(input())
    sum += line
    necessityEnvelop += line * necRate
    freedomEnvelop += line * ffaRate
    educationEnvelop += line * eduRate
    longTermEnvelop += line * ltssRate
    playEnvelop += line * playRate
    giveEnvelop += line * giveRate
    print("\n Будь ласка, введіть суму:")
    

print("В кінці маємо:\n\
    Необхідність:                   " + str(int(necessityEnvelop)) + "\n\
    Конверт фінансової свободи має: " + str(int(freedomEnvelop)) + "\n\
    Навчальний конверт:             " + str(int(educationEnvelop)) + "\n\
    Довгострокове заощадження:      " + str(int(longTermEnvelop)) + "\n\
    Резерв:                         " + str(int(playEnvelop)) + "\n\
    Подарунки:                      " + str(int(giveEnvelop)) + "\n\
    _______________________________________________________________\n\
    ")