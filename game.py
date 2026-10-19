import random

inventory = ["Рация", "ПМ"]
carma = 0

def lookAround (a):
    print("Вы осматриваетесь и видите:")
    for i in a:
        print(f"{a.index(i)+1}.{i}\n", end = " ")
    print("\n")

gateThings = ["Порваная покрышка", "Табличка ВЪЕЗД ЗАПРЕЩЁН", "Старый запечатаный конверт", "Армейская аптечка", "Осколки стекла", "Старые промокшие документы", "Магазин ПМ 3/8"]
soldier = ["Солдат. Ранен в грудь. Он ещё дышит, силы ещё не полностью его покинули, он тянет руку к вам, и, еле дыша, просит о помощи\nПомочь ему [Нужна аптечка]? 1.Да 2.Нет"]
territory = ["Где-то в кустах лежат старые деревяные ящики", "Порваный в клочья ботинок", "Старая документация"]
laba = ["План эвакуации", "мусор", "апртоьл", "цукенг", "смимс", "bvcytxdcfvgyu"]
stol = ["fsgrtuktjyhrtg","qfweghrgf","fwgehry","fgtyjhrtegrwf","efrwgtvf","qfwge"]

running = True
print("Вы проснулись с ощущением тумана в голове, у вас звенит в ушах")
while running:
    sRunning = True
    print("Вы видите старые ржавые ворота")
    print("\n\nВаши действия:\n1.Оглянуться\n2.Войти\n\n")
    a = input()
    match a:
        case "1":
            while sRunning:
                lookAround(gateThings)
                a = input("Что привлекто ваше внимание?\n10.Ничего\n\n")
                match a:
                    case "1":
                        print("Не вижу ничего интересного\n\n")
                    case "2":
                        print("Табличка...\nВыглядит так, будто бы лет 20 уже тут лежит\nВ центре буквы А виднеется пулевое отверстие\nНичего интересного\n\n")
                    case "3":
                        print("Конверт с государственной печатью.\nНе знаю почему, но чувствую, что он мне пригодится\n\nВ ваш инвентарь добавлен предмет [Старый запечатаный конверт]\n\n")
                        inventory.append(gateThings[int(a)-1])
                        gateThings.pop(int(a)-1)
                    case "4":
                        print("Армейская аптечка. Достаточно новая. Интересно, откуда она взялась?\nВзять аптечку? 1.Да 2.Нет")
                        b = input()
                        if b == "1":
                            print("В ваш инвентарь добавлен предмет [Aрмейская аптечка]\n\n")
                            inventory.append(gateThings[int(a)-1])
                            gateThings.pop(int(a)-1)
                        else: print("Вы не взяли аптечку...\n\n")
                    case "5":
                        print("Не вижу тут ничего интересного")
                    case "6":
                        print("Старые документы. Ещё советские. Они настолько стары и так дролго здесь лежат, что еле получается разобрать о чём в них написано. Это... \nПаспорт на холодильник!")
                    case "7":
                        print("Магазин под мой пистолет. В нём только три патрона.\nПоднять его? 1.Да 2.Нет")
                        b = input()
                        if b == "1":
                            print("В ваш инвентарь добавлен предмет [Магазин ПМ 3/8]\n\n")
                            inventory.append(gateThings[int(a)-1])
                            gateThings.pop(int(a)-1)
                        else: print("Вы решили не поднимать магазин")
                    case "10":
                        sRunning = False
                    case _:
                        print("Неверный ввод")
        case "2":
            while sRunning:
                print("Вы зашли на территорию за воротами. Стены все поросли мхом, здание, стоящее в центре участка в состоянии не уступает стенам.\nВ глаза бросается необычно блестящий замок на входной двери\nЧуть поворотя головой вы замечаете солдата. Он ранен.\n\n1.Осмотреть замок 2.Осмотреть солдата 3.Осмотреть участок 4.Рассмотреть конверт")
                a = input()
                match a:
                    case "1":
                        print("Вы видите блестящий кодовый замок. Попробуете подобрать пароль?\n1.Да 2.Нет")
                        b = input()
                        if b == "1":
                            code = input("Введите 4-х значное натуральное число")
                            if len(code)!= 4:
                                print("Неверный ввод")
                            else:
                                try:
                                    code = int(code)
                                except:
                                    print("Неверный ввод")
                            if code == 3417:
                                print("Замок щёлкнул и раскрылся, Вы вошли в здание...\n")
                                break
                            else:print("Ничего не произошло")
                    case "2":
                        lookAround(soldier)
                        a = input()
                        if a == "1":
                            print("Вы остановили кровотечение солдата, перебинтовали его и сообщили по рации о раненом\n\n")
                            carma += 5
                    case "3":
                        lookAround(territory)
                        a = input()
                        match a:
                            case "1":
                                print("Перед вами куча старых деревяных ящиков\nИзучить их получше? 1.Да 2.Нет\n")
                                a = input()
                                if a == "1":
                                    print("Вы раскидали ящики в стороны, что вызвало недоумение у солдата. В его глазах можно прочесть, что он рад тому, что он не ящик\nВы нашли пропуск")
                            case "2":
                                print("Ботинок вам по размеру, но надевать его вы не хотите")
                            case "3":
                                ###
                    case "4":
                        print("TEXT")
#--------------------------------------------------
print("вы в лабе")
while running:
    print("проход завален. 1.Оглянуться")
    lookAround(laba)
    a = input()
    match a:
        case "1":
            print("Инфа о выходе")
        case "2":
            print("musor")
        case "3":
            print("musor")
        case "4":
            
            print("вы видите компьютер и книгу рядом 1.Запуск 2.Не 3.Книга")
            b = input()
            if b == "1":
                print("posledovatelnost")
                fst = input()
                scnd = input()
                thrd = input()
                if fst == "синий" and scnd == "зелёный" and thrd == "красный":
                    print("")
                    inventory.append("key")
                    break
            if b == "3":
                print("KNIGA")
        case "5":
            print("musor")
        case "6":
            print("musor")
        case _:
            print("")
#гемор с компом
while running:
    print("введи код")
    a = input()
    if len(a)!= 3:
        print("Неверный ввод")
    else:
        try:
            a = int(a)
        except:
            print("Неверный ввод")
    if a == 346:
        print("вы нашли документ. открыть? 1.да")
        b = input()
        while b != "1":
            b = input()
        print("документ")
        inventory.append("papka")
        running = False

while running:
    print("looking for somathing")
    lookAround(stol)
    a = input()
    match a:
        case "1":
            
        case "2":
            
        case "3":
        
        case "4":
            print("вы нашли")
            if "карта доступа" in inventory:
                print("smth")
                break
            else: #gameover
        case "5":
            
        case "6":
        
        case _:
    
    #--------------------------------------------------
    
print("vi priehali")
print("1,4,9,16,25,36,,,_,100")
a,b,c = map(int,input().split())
while a!= 49 and b != 64 and c != 81:
    a,b,c = map(int,input("Введите последовательность").split())

print("predateli")
a = input()
if a != "Громов":
    carma -=100

print("pro ustroistvo")
finalChoice = input()
match finalChoice:
    case "1":
        print("bad end")
    case "2":
        print("neutral")
    case "3":
        print("happy")