countOfElements = 50
countOfRecomendations = 5


class Sight(object):

    def __init__(self, name, treeNumber, country, price, guideNeed, guideQuality, timeToSpend, dateOfFound, quantityOfVisitors, wildAnimals, uniqueAnimals, land, bestSeason, archStyle, religion, quantityOfFlora):
        self.name = name
        self.treeNumber = treeNumber
        self.country = country
        self.price = price
        self.guideNeed = guideNeed
        self.guideQuality = guideQuality
        self.timeToSpend = timeToSpend
        self.dateOfFound = dateOfFound
        self.quantityOfVisitors = quantityOfVisitors
        self.wildAnimals = wildAnimals
        self.uniqueAnimals = uniqueAnimals
        self.land = land
        self.bestSeason = bestSeason
        self.archStyle = archStyle
        self.religion = religion
        self.quantityOfFlora = quantityOfFlora


def makeSightsArray():
    Sights = []
    sight = Sight("Великая Китайская стена", 6, "Китай", 8, False, "low", 2, "300 b", 55000, True, True, True,
                  ["апрель", "май", "сентябрь", "октябрь"], ["Оборонительный,Монументализм"], "-", 0)
    Sights.append(sight)
    sight = Sight("Мачу Пикчу", 6, "Перу", 40, False, "high", 1, "1450 a", 2500, True, True, True,
                  ["апрель", "май", "сентябрь", "октябрь"], ["Архитектура инков"], "Мифология инков", 0)
    Sights.append(sight)
    sight = Sight("Петра",6,"Иордания",70,False,"high",3.5,"1800 a",2000,True,False,True,
                  ["сентябрь","октябрь","ноябрь"],["Петрейская архитектура"],"",0)
    Sights.append(sight)
    sight = Sight("Тадж Махал",6,"Индия",13,False,"high",3,"1632 a",22000,True,False,True,["февраль","март"],["Могольская архитектура"],"Ислам",0)
    Sights.append(sight)
    sight = Sight("Статуя Христа Искупителя",6,"Бразилия",5,False,"low",1,"1920 a",5000,True,True,True,["сентябрь","октябрь"],["Неоготика"],"Католицизм",0)
    Sights.append(sight)
    sight = Sight("Чичен Ица",6,"Мексика",15,True,"high",5,"455 a",7000,True,False,True,["декабрь","январь","февраль","март","апрель"],["Архитектура майя"],"Религия майя",0)
    Sights.append(sight)
    sight = Sight("Колизей",6,"Италия",15,False,"high",2,"80 a",19000,False,False,True,["июнь"],["Архитектура дрвенего Рима"],"",0)
    Sights.append(sight)
    sight = Sight("Пирамиды Гизы",6,"Египет",10,False,"low",1.5,"4500 b",10000,True,True,True,["май","сентябрь","октябрь"],["Уникальный"],"Религия древнего Египта",0)
    Sights.append(sight)
    sight = Sight("Эйфелева башня",7,"Франция",21,False,"low",1,"1889 a",25000,False,False,False,["апрель","май","сентябрь","октябрь"],["Конструктивизм"],"",0)
    Sights.append(sight)
    sight = Sight("Нгоронгоро",20,"Танзания",400,True,"low",6,"",3000,True,True,True,["июль","август"],[""],"",0)
    Sights.append(sight)
    sight = Sight("Собор Василия Блаженного",14,"Европейская Россия",5,False,"high",0.5,"1561 a",1500,False,False,False,["апрель","май","август","сентябрь","октябрь"],["Русская готика"],"Православие",0)
    Sights.append(sight)
    sight = Sight("Бродвей",5,"США",0,False,"low",0,"1667 a",100000,False,False,False,["март","апрель","май","июнь","июль","август","сентябрь"],[""],"",0)
    Sights.append(sight)
    sight = Sight("Рыбный рынок Цукидзи",26,"Япония",0,False,"low",2,"1935 a",10000,True,True,False,["март","апрель","сентябрь","ноябрь"],[""],"",0)
    Sights.append(sight)
    sight = Sight("Хофбройхаус",27,"Германия",0,False,"low",1,"1607 a",30000,False,False,False,["май","сентябрь","октябрь"],["Немецкий классицизм"],"",0)
    Sights.append(sight)
    sight = Sight("Замок Бран",10,"Румыния",16,False,"high",1,"1212 a",1000,True,False,True,["апрель","май","сентябрь","октябрь"],"Неоготика","",0)
    Sights.append(sight)
    sight = Sight("Синнерей Зилерталь",30,"Австрия",20,False,"low",1.5,"1954 a",100,True,False,True,["май","сентябрь","октябрь"],[""],"",0)
    Sights.append(sight)
    sight = Sight("Замок Химедзи",4,"Япония",0,False,"high",3,"1609 a",3600,True,False,False,["апрель","май","июнь","июль"],["Японский"],"",0)
    Sights.append(sight)
    sight = Sight("Дом Фредди Меркури",12,"Танзания",10,False,"low",0.25,"",4000,False,False,False,["июль","август"],["Архитектура суахили"],"",0)
    Sights.append(sight)
    sight = Sight("Большой Барьерный риф",17,"Австралия",0,False,"low",3,"",10000,True,True,True,["апрель","май","сентябрь","октябрь"],[""],"",0)
    Sights.append(sight)
    sight = Sight("Водопад Анхель",21,"Венесуэла",0,False,"low",1,"",500,True,False,True,["декабрь","январь","февраль","март","апрель"],[""],"",0)
    Sights.append(sight)
    sight = Sight("Уцуцу",15,"Япония",0,False,"high",0.25,"",0,False,False,False,["апрель,май,сентябрь,октябрь"],["Японский"],"Синтоизм",0)
    Sights.append(sight)
    sight = Sight("Зоопарк Сан-Диего",19,"США",71,False,"low",3,"1916 a",15000,True,True,False,["апрель","май","июнь","сентябрь","октябрь"],[""],"",6500)
    Sights.append(sight)
    sight = Sight("ЭкоДеревушка",29,"Европейская Россия",5,False,"high",1,"2015 a",100,True,False,False,["июнь","июль","августь"],[""],"",0)
    Sights.append(sight)
    sight = Sight("Ботанический сад Монреаля",22,"Канада",13,False,"high",2,"1931 a",10000,False,False,False,["май,июнь,июль,август"],[""],"",21000)
    Sights.append(sight)
    sight = Sight("Писающий мальчик",11,"Бельгия",0,False,"low",0.25,"1619 a",0,False,False,False,["апрель","июль","сентябрь"],["Готика,Ренессанс"],"",0)
    Sights.append(sight)
    sight = Sight("Березенский биосферный заповедник",18,"Беларусь",3,False,"high",2,"1925 a",200,True,False,True,["май","июнь","август","сентябрь","октябрь","февраль"],[""],"",2000)
    Sights.append(sight)
    sight = Sight("Da Narbone",24,"Италия",0,False,"low",1,"1872 a",2000,False,False,False,["июль","август","сентябрь"],["Ренессанс"],"",0)
    Sights.append(sight)
    sight = Sight("Floresta Das Escadinhas",25,"Португалия",0,False,"low",2,"",2000,False,False,False,["май","июнь"],[""],"",0)
    Sights.append(sight)
    sight = Sight("Гранд канал",12,"Италия",0,False,"high",3,"421 a",0,False,False,True,["июнь","август","сентябрь"],["Византийский","Романский","Готика","Ренессанс"],"Католицизм",0)
    Sights.append(sight)
    sight = Sight("Диснейлэнд Париж",12,"Франция",77,False,"low",10,"1992 a",34000,False,False,False,["сентябрь","октябрь","март","апрель"],[""],"",0)
    Sights.append(sight)
    sight = Sight("Бурдж Халифа",2,"ОАЭ",42,False,"low",2,"2010 a",4100,False,False,False,["октябрь","апрель"],["Постмодернизм"],"",0)
    Sights.append(sight)
    sight = Sight("Терракотовая армия",10,"Китай",14,False,"high",2,"200 b",10000,False,False,False,["март","апрель"],["Китайский"],"",0)
    Sights.append(sight)
    sight = Sight("Лувр",12,"Франция",19,False,"high",4,"1792 a",10000,False,False,False,["март","апрель"],["Классицизм"],"",0)
    Sights.append(sight)
    sight = Sight("Саграда Фамилия",2,"Испания",30,False,"high",1.5,"1882 a",14000,False,False,False,["июль","август"],["Неоготика","Модерн"],"Католицизм",0)
    Sights.append(sight)
    sight = Sight("Килиманджаро",20,"Танзания",1200,True,"low",168,"",100,True,False,True,["июль","август"],[""],"",0)
    Sights.append(sight)
    sight = Sight("Озеро Блед",21,"Словения",22,False,"high",3,"",300,True,False,True,["сентябрь","октябрь"],[""],"",0)
    Sights.append(sight)
    sight = Sight("Пустыня Сахара",20,"Египет",0,False,"low",1,"",0,True,True,True,["январь","февраль"],[""],"",0)
    Sights.append(sight)
    sight = Sight("Остров Пасхи",17,"Чили",600,False,"high",24,"",0,True,True,True,["декабрь","январь","февраль","март"],[""],"",0)
    Sights.append(sight)
    sight = Sight("Озеро Байкал",21,"Азиатская Россия",0,False,"low",2,"",0,True,False,True,["декабрь","январь","февраль"],[""],"",0)
    Sights.append(sight)
    sight = Sight("Мечеть Султанахмет",14,"Турция",3,False,"high",1,"1616 a",15000,False,False,False,["сентябрь","октябрь","февраль","март"],["Османский тип"],"Ислам",0)
    Sights.append(sight)
    sight = Sight("Аокигахара",12,"Япония",0,False,"low",1,"",0,True,False,False,["апрель","октябрь"],[""],"",0)
    Sights.append(sight)
    sight = Sight("Фудзи-Хаконе-Идзу",20,"Япония",4,False,"low",3,"",700,True,False,True,["апрель","май","сентябрь","октябрь"],[""],"",0)
    Sights.append(sight)
    sight = Sight("Собор Парижской Богоматери",14,"Франция",5,False,"low",1.5,"1345 a",35000,False,False,False,["июнь","июль","август"],["Готика"],"Католицизм",0)
    Sights.append(sight)
    sight = Sight("Чижик-Пыжик",10,"Европейская Россия",0,False,"low",0.25,"1994 a",0,False,False,False,["июнь","июль","август"],[""],"",0)
    Sights.append(sight)
    sight = Sight("Кунтскамера",12,"Европейская Россия",4,False,"high",2,"1734 a",1000,False,False,False,["июнь","июль","август"],["Русское барокко"],"",0)
    Sights.append(sight)
    sight = Sight("Пидуруталагала",18,"Шри-Ланка",0,False,"high",3,"",3000,True,False,True,["декабрь","январь","февраль","март"],[""],"",0)
    Sights.append(sight)
    sight = Sight("Пизанская башня",7,"Италия",25,False,"low",1,"1173 a",320,False,False,False,["май","август","сентябрь"],["Романский"],"",0)
    Sights.append(sight)
    sight = Sight("Парфенон",15,"Греция",25,False,"low",2,"450 b",18000,False,False,True,["май","июнь","июль"],["Дорический"],"Эллинизм",0)
    Sights.append(sight)
    sight = Sight("Биг Бен",2,"Великобритания",22,False,"low",1,"1843 a",20000,False,False,False,["июнь","июль","август"],["Неоготика"],"",0)
    Sights.append(sight)
    sight = Sight("Стоунхендж",10,"Великобритания",70,False,"low",1,"3000 b",7700,True,False,True,["июнь","июль","август"],[""],"",0)
    Sights.append(sight)

    return Sights


def outputCountryInfo(Sights, AsiaMass, EuropeMass, AfricaMass, NorthAmericaMass, MiddleAmericaMass, SouthAmericaMass, OceanMass):
    k = 0
    for i in range(0, len(Sights)):
        if Sights[i].country in AsiaMass:
            print(Sights[i].name + " находится в Азии!")
            k = k + 1

    print("Стран в Азии " + str(len(AsiaMass)))

    for i in range(0, len(Sights)):
        if Sights[i].country in EuropeMass:
            print(Sights[i].name + " находится в Европе!")
            k = k + 1

    print("Стран в Европе " + str(len(EuropeMass)))

    for i in range(0, len(Sights)):
        if Sights[i].country in AfricaMass:
            print(Sights[i].name + " находится в Африке!")
            k = k + 1

    print("Стран в Африке " + str(len(AfricaMass)))

    for i in range(0, len(Sights)):
        if Sights[i].country in NorthAmericaMass:
            print(Sights[i].name + " находится в Северной Америке!")
            k = k + 1

    print("Стран в Северной Америке " + str(len(NorthAmericaMass)))

    for i in range(0, len(Sights)):
        if Sights[i].country in MiddleAmericaMass:
            print(Sights[i].name + " находится в Центральной Америке!")
            k = k + 1

    print("Стран в Центральной Америке " + str(len(MiddleAmericaMass)))

    for i in range(0, len(Sights)):
        if Sights[i].country in SouthAmericaMass:
            print(Sights[i].name + " находится в Южной Америке!")
            k = k + 1

    print("Стран в Южной Америке " + str(len(SouthAmericaMass)))

    for i in range(0, len(Sights)):
        if Sights[i].country in OceanMass:
            print(Sights[i].name + " находится в Австралии или Океании!")
            k = k + 1

    print("Стран в Австралии и Океании " + str(len(OceanMass)))

    print("ИТОГО достопримечательностей:" + str(k))
    print("А должно быть:" + str(len(Sights)))
    print("Всего стран:" + str(
        len(AsiaMass) + len(EuropeMass) + len(AfricaMass) + len(NorthAmericaMass) + len(MiddleAmericaMass) + len(
            SouthAmericaMass) + len(OceanMass)))


def createCountryAdjaMatr(Sights, AsiaMass, EuropeMass, AfricaMass, NorthAmericaMass, MiddleAmericaMass, SouthAmericaMass, OceanMass):
    matr = [[0] * len(Sights) for i in range(len(Sights))]
    for i in range(len(Sights)):
        for j in range(len(Sights)):
            if Sights[i].country in AsiaMass and Sights[j].country in AsiaMass:########## Asia
                matr[i][j] = 1
            elif Sights[i].country in AsiaMass and Sights[j].country in OceanMass:
                matr[i][j] = 0.5
            elif Sights[i].country in AsiaMass and Sights[j].country in AfricaMass:
                matr[i][j] = 0.45
            elif Sights[i].country in AsiaMass and Sights[j].country in EuropeMass:
                matr[i][j] = 0.35
            elif Sights[i].country in AsiaMass and Sights[j].country in SouthAmericaMass:
                matr[i][j] = 0.3
            elif Sights[i].country in AsiaMass and Sights[j].country in MiddleAmericaMass:
                matr[i][j] = 0.25
            elif Sights[i].country in AsiaMass and Sights[j].country in NorthAmericaMass:
                matr[i][j] = 0.2
            elif Sights[i].country in OceanMass and Sights[j].country in AsiaMass: ########### Ocean
                matr[i][j] = 0.5
            elif Sights[i].country in OceanMass and Sights[j].country in OceanMass:
                matr[i][j] = 1
            elif Sights[i].country in OceanMass and Sights[j].country in AfricaMass:
                matr[i][j] = 0.5
            elif Sights[i].country in OceanMass and Sights[j].country in EuropeMass:
                matr[i][j] = 0.2
            elif Sights[i].country in OceanMass and Sights[j].country in SouthAmericaMass:
                matr[i][j] = 0.75
            elif Sights[i].country in OceanMass and Sights[j].country in MiddleAmericaMass:
                matr[i][j] = 0.75
            elif Sights[i].country in OceanMass and Sights[j].country in NorthAmericaMass:
                matr[i][j] = 0.45
            elif Sights[i].country in EuropeMass and Sights[j].country in AsiaMass: ########### Europe
                matr[i][j] = 0.35
            elif Sights[i].country in EuropeMass and Sights[j].country in OceanMass:
                matr[i][j] = 0.2
            elif Sights[i].country in EuropeMass and Sights[j].country in AfricaMass:
                matr[i][j] = 0.45
            elif Sights[i].country in EuropeMass and Sights[j].country in EuropeMass:
                matr[i][j] = 1
            elif Sights[i].country in EuropeMass and Sights[j].country in SouthAmericaMass:
                matr[i][j] = 0.35
            elif Sights[i].country in EuropeMass and Sights[j].country in MiddleAmericaMass:
                matr[i][j] = 0.45
            elif Sights[i].country in EuropeMass and Sights[j].country in NorthAmericaMass:
                matr[i][j] = 0.8
            elif Sights[i].country in AfricaMass and Sights[j].country in AsiaMass:  ########### Africa
                matr[i][j] = 0.45
            elif Sights[i].country in AfricaMass and Sights[j].country in OceanMass:
                matr[i][j] = 0.5
            elif Sights[i].country in AfricaMass and Sights[j].country in AfricaMass:
                matr[i][j] = 1
            elif Sights[i].country in AfricaMass and Sights[j].country in EuropeMass:
                matr[i][j] = 0.45
            elif Sights[i].country in AfricaMass and Sights[j].country in SouthAmericaMass:
                matr[i][j] = 0.35
            elif Sights[i].country in AfricaMass and Sights[j].country in MiddleAmericaMass:
                matr[i][j] = 0.45
            elif Sights[i].country in AfricaMass and Sights[j].country in NorthAmericaMass:
                matr[i][j] = 0.25
            elif Sights[i].country in NorthAmericaMass and Sights[j].country in AsiaMass:  ########### North America
                matr[i][j] = 0.2
            elif Sights[i].country in NorthAmericaMass and Sights[j].country in OceanMass:
                matr[i][j] = 0.45
            elif Sights[i].country in NorthAmericaMass and Sights[j].country in AfricaMass:
                matr[i][j] = 0.25
            elif Sights[i].country in NorthAmericaMass and Sights[j].country in EuropeMass:
                matr[i][j] = 0.8
            elif Sights[i].country in NorthAmericaMass and Sights[j].country in SouthAmericaMass:
                matr[i][j] = 0.35
            elif Sights[i].country in NorthAmericaMass and Sights[j].country in MiddleAmericaMass:
                matr[i][j] = 0.45
            elif Sights[i].country in NorthAmericaMass and Sights[j].country in NorthAmericaMass:
                matr[i][j] = 1
            elif Sights[i].country in SouthAmericaMass and Sights[j].country in AsiaMass:  ########### South America
                matr[i][j] = 0.3
            elif Sights[i].country in SouthAmericaMass and Sights[j].country in OceanMass:
                matr[i][j] = 0.75
            elif Sights[i].country in SouthAmericaMass and Sights[j].country in AfricaMass:
                matr[i][j] = 0.35
            elif Sights[i].country in SouthAmericaMass and Sights[j].country in EuropeMass:
                matr[i][j] = 0.35
            elif Sights[i].country in SouthAmericaMass and Sights[j].country in SouthAmericaMass:
                matr[i][j] = 1
            elif Sights[i].country in SouthAmericaMass and Sights[j].country in MiddleAmericaMass:
                matr[i][j] = 0.8
            elif Sights[i].country in SouthAmericaMass and Sights[j].country in NorthAmericaMass:
                matr[i][j] = 0.35
            elif Sights[i].country in MiddleAmericaMass and Sights[j].country in AsiaMass:  ########### Middle America
                matr[i][j] = 0.25
            elif Sights[i].country in MiddleAmericaMass and Sights[j].country in OceanMass:
                matr[i][j] = 0.75
            elif Sights[i].country in MiddleAmericaMass and Sights[j].country in AfricaMass:
                matr[i][j] = 0.45
            elif Sights[i].country in MiddleAmericaMass and Sights[j].country in EuropeMass:
                matr[i][j] = 0.45
            elif Sights[i].country in MiddleAmericaMass and Sights[j].country in SouthAmericaMass:
                matr[i][j] = 0.8
            elif Sights[i].country in MiddleAmericaMass and Sights[j].country in MiddleAmericaMass:
                matr[i][j] = 1
            elif Sights[i].country in MiddleAmericaMass and Sights[j].country in NorthAmericaMass:
                matr[i][j] = 0.45

    return matr


def createPriceAdjaMatr(Sights):
    matr = [[0] * len(Sights) for i in range(len(Sights))]
    for i in range(len(Sights)):
        for j in range(len(Sights)):
            if (Sights[i].price == 0) and (Sights[j].price == 0):  # 0
                matr[i][j] = 1
            elif (Sights[i].price == 0) and (0 < Sights[j].price <= 10):
                matr[i][j] = 0.86
            elif (Sights[i].price == 0) and (10 < Sights[j].price <= 20):
                matr[i][j] = 0.72
            elif (Sights[i].price == 0) and (20 < Sights[j].price <= 50):
                matr[i][j] = 0.58
            elif (Sights[i].price == 0) and (50 < Sights[j].price <= 100):
                matr[i][j] = 0.44
            elif (Sights[i].price == 0) and (100 < Sights[j].price <= 500):
                matr[i][j] = 0.3
            elif (Sights[i].price == 0) and (Sights[j].price > 500):
                matr[i][j] = 0.16
            elif (0 < Sights[i].price <= 10) and (Sights[j].price == 0):  # 0 < X <= 10
                matr[i][j] = 0.86
            elif (0 < Sights[i].price <= 10) and (0 < Sights[j].price <= 10):
                matr[i][j] = 1
            elif (0 < Sights[i].price <= 10) and (10 < Sights[j].price <= 20):
                matr[i][j] = 0.86
            elif (0 < Sights[i].price <= 10) and (20 < Sights[j].price <= 50):
                matr[i][j] = 0.72
            elif (0 < Sights[i].price <= 10) and (50 < Sights[j].price <= 100):
                matr[i][j] = 0.58
            elif (0 < Sights[i].price <= 10) and (100 < Sights[j].price <= 500):
                matr[i][j] = 0.44
            elif (0 < Sights[i].price <= 10) and (Sights[j].price > 500):
                matr[i][j] = 0.3
            elif (10 < Sights[i].price <= 20) and (Sights[j].price == 0):  # 10 < X <= 20
                matr[i][j] = 0.72
            elif (10 < Sights[i].price <= 20) and (0 < Sights[j].price <= 10):
                matr[i][j] = 0.86
            elif (10 < Sights[i].price <= 20) and (10 < Sights[j].price <= 20):
                matr[i][j] = 1
            elif (10 < Sights[i].price <= 20) and (20 < Sights[j].price <= 50):
                matr[i][j] = 0.86
            elif (10 < Sights[i].price <= 20) and (50 < Sights[j].price <= 100):
                matr[i][j] = 0.72
            elif (10 < Sights[i].price <= 20) and (100 < Sights[j].price <= 500):
                matr[i][j] = 0.58
            elif (10 < Sights[i].price <= 20) and (Sights[j].price > 500):
                matr[i][j] = 0.44
            elif (20 < Sights[i].price <= 50) and (Sights[j].price == 0):  # 20 < X <= 50
                matr[i][j] = 0.58
            elif (20 < Sights[i].price <= 50) and (0 < Sights[j].price <= 10):
                matr[i][j] = 0.72
            elif (20 < Sights[i].price <= 50) and (10 < Sights[j].price <= 20):
                matr[i][j] = 0.86
            elif (20 < Sights[i].price <= 50) and (20 < Sights[j].price <= 50):
                matr[i][j] = 1
            elif (20 < Sights[i].price <= 50) and (50 < Sights[j].price <= 100):
                matr[i][j] = 0.72
            elif (20 < Sights[i].price <= 50) and (100 < Sights[j].price <= 500):
                matr[i][j] = 0.58
            elif (20 < Sights[i].price <= 50) and (Sights[j].price > 500):
                matr[i][j] = 0.44
            elif (50 < Sights[i].price <= 100) and (Sights[j].price == 0):  # 50 < X <= 100
                matr[i][j] = 0.44
            elif (50 < Sights[i].price <= 100) and (0 < Sights[j].price <= 10):
                matr[i][j] = 0.58
            elif (50 < Sights[i].price <= 100) and (10 < Sights[j].price <= 20):
                matr[i][j] = 0.72
            elif (50 < Sights[i].price <= 100) and (20 < Sights[j].price <= 50):
                matr[i][j] = 0.86
            elif (50 < Sights[i].price <= 100) and (50 < Sights[j].price <= 100):
                matr[i][j] = 1
            elif (50 < Sights[i].price <= 100) and (100 < Sights[j].price <= 500):
                matr[i][j] = 0.86
            elif (50 < Sights[i].price <= 100) and (Sights[j].price > 500):
                matr[i][j] = 0.72
            elif (100 < Sights[i].price <= 500) and (Sights[j].price == 0):  # 100 < X <= 500
                matr[i][j] = 0.3
            elif (100 < Sights[i].price <= 500) and (0 < Sights[j].price <= 10):
                matr[i][j] = 0.44
            elif (100 < Sights[i].price <= 500) and (10 < Sights[j].price <= 20):
                matr[i][j] = 0.58
            elif (100 < Sights[i].price <= 500) and (20 < Sights[j].price <= 50):
                matr[i][j] = 0.72
            elif (100 < Sights[i].price <= 500) and (50 < Sights[j].price <= 100):
                matr[i][j] = 0.86
            elif (100 < Sights[i].price <= 500) and (100 < Sights[j].price <= 500):
                matr[i][j] = 1
            elif (100 < Sights[i].price <= 500) and (Sights[j].price > 500):
                matr[i][j] = 0.86
            elif (Sights[i].price > 500) and (Sights[j].price == 0):  # 500 < X
                matr[i][j] = 0.16
            elif (Sights[i].price > 500) and (0 < Sights[j].price <= 10):
                matr[i][j] = 0.3
            elif (Sights[i].price > 500) and (10 < Sights[j].price <= 20):
                matr[i][j] = 0.44
            elif (Sights[i].price > 500) and (20 < Sights[j].price <= 50):
                matr[i][j] = 0.58
            elif (Sights[i].price > 500) and (50 < Sights[j].price <= 100):
                matr[i][j] = 0.72
            elif (Sights[i].price > 500) and (100 < Sights[j].price <= 500):
                matr[i][j] = 0.86
            elif (Sights[i].price > 500) and (Sights[j].price > 500):
                matr[i][j] = 1

    return matr


def createTreeAdjaMatr(Sights):
    matr = [[0] * len(Sights) for i in range(len(Sights))]
    for i in range(len(Sights)):
        for j in range(len(Sights)):
            if 0 < Sights[i].treeNumber < 8 and 0 < Sights[j].treeNumber < 8:
                if i == j:
                    matr[i][j] = 1
                elif Sights[i].treeNumber == 2 and (Sights[j].treeNumber == 4 or Sights[j].treeNumber == 5):  #1 ветка
                    matr[i][j] = 0.9
                elif Sights[i].treeNumber == Sights[j].treeNumber:
                    matr[i][j] = 1
                else:
                    matr[i][j] = 0.85
            elif 0 < Sights[i].treeNumber < 8 < Sights[j].treeNumber < 16:
                matr[i][j] = 0.8
            elif 0 < Sights[i].treeNumber < 8 and 16 < Sights[j].treeNumber < 23:
                matr[i][j] = 0.35
            elif 0 < Sights[i].treeNumber < 8 and 23 < Sights[j].treeNumber:
                matr[i][j] = 0.7
            elif 0 < Sights[j].treeNumber < 8 < Sights[i].treeNumber < 16:  #2 ветка
                matr[i][j] = 0.7
            elif 8 < Sights[i].treeNumber < 16 and 8 < Sights[j].treeNumber < 16:
                if i == j:
                    matr[i][j] = 1
                elif Sights[i].treeNumber == Sights[j].treeNumber:
                    matr[i][j] = 1
                else:
                    matr[i][j] = 0.75
            elif 8 < Sights[i].treeNumber < 16 < Sights[j].treeNumber < 23:
                matr[i][j] = 0.35
            elif 8 < Sights[i].treeNumber < 16 and 23 < Sights[j].treeNumber:
                matr[i][j] = 0.7
            elif 16 < Sights[i].treeNumber < 23 and 0 < Sights[j].treeNumber < 8:  #3 ветка
                matr[i][j] = 0.35
            elif 8 < Sights[j].treeNumber < 16 < Sights[i].treeNumber < 23:
                matr[i][j] = 0.35
            elif 16 < Sights[i].treeNumber < 23 and 16 < Sights[j].treeNumber < 23:
                if i == j:
                    matr[i][j] = 1
                elif i == 21 or j == 21:
                    matr[i][j] = 0.88
                elif Sights[i].treeNumber == Sights[j].treeNumber:
                    matr[i][j] = 1
                else:
                    matr[i][j] = 0.9
            elif 16 < Sights[i].treeNumber < 23 < Sights[j].treeNumber:
                matr[i][j] = 0.35
            elif 23 < Sights[i].treeNumber and 0 < Sights[j].treeNumber < 8: #4 ветка
                matr[i][j] = 0.7
            elif 23 < Sights[i].treeNumber and 8 < Sights[j].treeNumber < 16:
                matr[i][j] = 0.7
            elif 16 < Sights[j].treeNumber < 23 < Sights[i].treeNumber:
                matr[i][j] = 0.35
            elif 23 < Sights[i].treeNumber and 23 < Sights[j].treeNumber:
                if i == j:
                    matr[i][j] = 1
                elif Sights[i].treeNumber == Sights[j].treeNumber:
                    matr[i][j] = 1
                elif i > 28:
                    if i > 28 and j > 28 and i != j:
                        matr[i][j] = 0.75
                    elif j < 28 < i :
                        matr[i][j] = 0.7
                elif i < 28 < j:
                    matr[i][j] = 0.7
                else:
                    matr[i][j] = 0.9

    return matr


def createMainAdjaMatr(Sights, treeAdjaMatr,priceAdjaMatr, countryAdjaMatr):
    matr = [[0] * len(Sights) for i in range(len(Sights))]
    for i in range(len(Sights)):
        for j in range(len(Sights)):
            if treeAdjaMatr[i][j] == 1:
                kTree = 0.8
            else:
                kTree = 0.7
            if priceAdjaMatr[i][j] == 1:
                kPrice = 0.75
            else:
                kPrice = 0.65
            if countryAdjaMatr[i][j] == 1:
                kCountry = 0.75
            else:
                kCountry = 0.65
            if i == j:
                matr[i][j] = 1
            else:
                matr[i][j] = ((treeAdjaMatr[i][j] * kTree) + (priceAdjaMatr[i][j] * kPrice) + (countryAdjaMatr[i][j] * kCountry)) / (kTree + kPrice + kCountry)

    return matr


def findFiveClosest(mainAdjaMatr, curRow):
    matr = list(range(countOfRecomendations))
    posMatr = list(range(countOfRecomendations))
    upBorder = 1
    for i in range(countOfRecomendations):
        curMax = 0
        curMaxPos = 0
        for j in range(countOfElements):
            if curMax < mainAdjaMatr[curRow][j] < upBorder:
                curMax = mainAdjaMatr[curRow][j]
                curMaxPos = j

        matr[i] = curMax
        posMatr[i] = curMaxPos
        upBorder = curMax

    return matr, posMatr


def findFiveFurthest(mainAdjaMatr, curRow):
    matr = list(range(countOfRecomendations))
    posMatr = list(range(countOfRecomendations))
    downBorder = 0
    for i in range(countOfRecomendations):
        curMin = 1
        curMinPos = 0
        for j in range(countOfElements):
            if curMin > mainAdjaMatr[curRow][j] > downBorder:
                curMin = mainAdjaMatr[curRow][j]
                curMinPos = j

        matr[i] = curMin
        posMatr[i] = curMinPos
        downBorder = curMin

    return matr, posMatr


def findFiveClosestAfter(Sights, mainAdjaMatr, curRow):
    matr = list(range(countOfRecomendations))
    posMatr = list(range(countOfRecomendations))
    upBorder = 1
    for i in range(countOfRecomendations):
        curMax = 0
        curMaxPos = 0
        for j in range(len(Sights)):
            if curMax < mainAdjaMatr[curRow][j] < upBorder:
                curMax = mainAdjaMatr[curRow][j]
                curMaxPos = j

        matr[i] = curMax
        posMatr[i] = curMaxPos
        upBorder = curMax

    return matr, posMatr


def findFiveFurthestAfter(Sights, mainAdjaMatr, curRow):
    matr = list(range(countOfRecomendations))
    posMatr = list(range(countOfRecomendations))
    downBorder = 0
    for i in range(countOfRecomendations):
        curMin = 1
        curMinPos = 0
        for j in range(len(Sights)):
            if curMin > mainAdjaMatr[curRow][j] > downBorder:
                curMin = mainAdjaMatr[curRow][j]
                curMinPos = j

        matr[i] = curMin
        posMatr[i] = curMinPos
        downBorder = curMin

    return matr, posMatr


def findFiveCombined(massL, massD, mainAdjaMatr):
    if len(massL) == 0: # 0 Лайков
        mn = 1
        likeMass = list(range(len(massD) * 5))
        for i in range(len(massD)):
            matr, posMatr = findFiveClosest(mainAdjaMatr, massD[i])
            for j in range(len(posMatr)):
                likeMass[i * 5 + j] = posMatr[j]

        if len(massD) == 2:
            mn = 3
        elif len(massD) == 3:
            mn = 2
        elif len(massD) >= 4:
            mn = 1

        curMatr = list(range(len(massD) * mn))
        pos = 0
        for i in range(len(massD)):
            prevMass, prevPosMass = findFiveFurthest(mainAdjaMatr, massD[i])
            count = 0
            j = 1
            while count < mn and j < 5:
                if prevPosMass[j] not in massD and prevPosMass[j] not in curMatr and prevPosMass[j] not in likeMass:
                    curMatr[pos] = prevPosMass[j]
                    pos += 1
                    count += 1
                j += 1

        return curMatr

    elif len(massD) == 0: # 0 Дизлайков
        mn = 1
        dislikeMass = list(range(len(massL) * 5))
        for i in range(len(massL)):
            matr, posMatr = findFiveFurthest(mainAdjaMatr, massL[i])
            for j in range(len(posMatr)):
                dislikeMass[i * 5 + j] = posMatr[j]

        if len(massL) == 2:
            mn = 3
        elif len(massL) == 3:
            mn = 2
        elif len(massL) >= 4:
            mn = 1

        curMatr = list(range(len(massL) * mn))
        pos = 0
        for i in range(len(massL)):
            prevMass, prevPosMass = findFiveClosest(mainAdjaMatr, massL[i])
            count = 0
            j = 1
            while count < mn and j < 5:
                if prevPosMass[j] not in massL and prevPosMass[j] not in curMatr and prevPosMass[j] not in dislikeMass:
                    curMatr[pos] = prevPosMass[j]
                    pos += 1
                    count += 1
                j += 1

        return curMatr
    else: # n > 0, m > 0
        mn = 1
        dislikeMass = list(range(len(massD) * 5))
        for i in range(len(massD)):
            matr, posMatr = findFiveClosest(mainAdjaMatr, massD[i])
            for j in range(len(posMatr)):
                if matr[j] > 0.83:
                    dislikeMass[i * 5 + j] = posMatr[j]

        if len(massL) == 1:
            curMatr = list()
            prevMass, prevPosMass = findFiveClosest(mainAdjaMatr, massL[0])
            j = 0
            while j < 5:
                if prevPosMass[j] not in massL and prevPosMass[j] not in massD and prevPosMass[j] not in dislikeMass:
                    curMatr.append(prevPosMass[j])
                j += 1
            return curMatr
        elif len(massL) == 2:
            mn = 3
        elif len(massL) == 3:
            mn = 2
        elif len(massL) >= 4:
            mn = 1

        curMatr = list()
        count = 0
        for i in range(len(massL)):
            prevMass, prevPosMass = findFiveClosest(mainAdjaMatr, massL[i])
            j = 0
            mnCount = 0
            while mnCount < mn and j < 5:
                if prevPosMass[j] not in massL and prevPosMass[j] not in curMatr and prevPosMass[j] not in dislikeMass and prevPosMass[j] not in massD:
                    curMatr.append(prevPosMass[j])
                    mnCount += 1
                    count += 1
                    if count == 5:
                        return curMatr
                j += 1

        return curMatr


def findFiveCombinedAfter(Sights, massL, massD, mainAdjaMatr):
    if len(massL) == 0: # 0 Лайков
        mn = 1
        likeMass = list(range(len(massD) * 5))
        for i in range(len(massD)):
            matr, posMatr = findFiveClosestAfter(Sights, mainAdjaMatr, massD[i])
            for j in range(len(posMatr)):
                likeMass[i * 5 + j] = posMatr[j]

        if len(massD) == 2:
            mn = 3
        elif len(massD) == 3:
            mn = 2
        elif len(massD) >= 4:
            mn = 1

        curMatr = list(range(len(massD) * mn))
        pos = 0
        for i in range(len(massD)):
            prevMass, prevPosMass = findFiveFurthestAfter(Sights, mainAdjaMatr, massD[i])
            count = 0
            j = 1
            while count < mn and j < 5:
                if prevPosMass[j] not in massD and prevPosMass[j] not in curMatr and prevPosMass[j] not in likeMass:
                    curMatr[pos] = prevPosMass[j]
                    pos += 1
                    count += 1
                j += 1

        return curMatr

    elif len(massD) == 0: # 0 Дизлайков
        mn = 1
        dislikeMass = list(range(len(massL) * 5))
        for i in range(len(massL)):
            matr, posMatr = findFiveFurthestAfter(Sights, mainAdjaMatr, massL[i])
            for j in range(len(posMatr)):
                dislikeMass[i * 5 + j] = posMatr[j]

        if len(massL) == 2:
            mn = 3
        elif len(massL) == 3:
            mn = 2
        elif len(massL) >= 4:
            mn = 1

        curMatr = list(range(len(massL) * mn))
        pos = 0
        for i in range(len(massL)):
            prevMass, prevPosMass = findFiveClosestAfter(Sights, mainAdjaMatr, massL[i])
            count = 0
            j = 1
            while count < mn and j < 5:
                if prevPosMass[j] not in massL and prevPosMass[j] not in curMatr and prevPosMass[j] not in dislikeMass:
                    curMatr[pos] = prevPosMass[j]
                    pos += 1
                    count += 1
                j += 1

        return curMatr
    else: # n > 0, m > 0
        mn = 1
        dislikeMass = list(range(len(massD) * 5))
        for i in range(len(massD)):
            matr, posMatr = findFiveClosestAfter(Sights, mainAdjaMatr, massD[i])
            for j in range(len(posMatr)):
                if matr[j] > 0.83:
                    dislikeMass[i * 5 + j] = posMatr[j]

        if len(massL) == 1:
            curMatr = list()
            prevMass, prevPosMass = findFiveClosestAfter(Sights, mainAdjaMatr, massL[0])
            j = 0
            while j < 5:
                if prevPosMass[j] not in massL and prevPosMass[j] not in massD and prevPosMass[j] not in dislikeMass:
                    curMatr.append(prevPosMass[j])
                j += 1
            return curMatr
        elif len(massL) == 2:
            mn = 3
        elif len(massL) == 3:
            mn = 2
        elif len(massL) >= 4:
            mn = 1

        curMatr = list()
        count = 0
        for i in range(len(massL)):
            prevMass, prevPosMass = findFiveClosestAfter(Sights, mainAdjaMatr, massL[i])
            j = 0
            mnCount = 0
            while mnCount < mn and j < 5:
                if prevPosMass[j] not in massL and prevPosMass[j] not in curMatr and prevPosMass[j] not in dislikeMass and prevPosMass[j] not in massD:
                    curMatr.append(prevPosMass[j])
                    mnCount += 1
                    count += 1
                    if count == 5:
                        return curMatr
                j += 1

        return curMatr


def printResult(Sights, matr, posMatr):
    for i in range(countOfRecomendations):
        print("Название:" + str(Sights[posMatr[i]].name))
        print("Близость: " + str(matr[i]))


def singleLike(Sights, mainAdjaMatr):
    for i in range(len(Sights)):
        print(str(i) + " " + Sights[i].name)

    print("Введите номер понравившейся достопримечательности")
    chosEl = int(input())
    resultMatr, resultPosMatr = findFiveClosest(mainAdjaMatr, chosEl)
    print("Исходя из того что вам понравилась такая достопримечательность как " + str(Sights[chosEl].name) +
          ", мы рекомендуем вам посетить нижеперечисленные достопримечательности:")
    printResult(Sights, resultMatr, resultPosMatr)

    return resultMatr, resultPosMatr


def singleDislike(Sights, mainAdjaMatr):
    for i in range(len(Sights)):
        print(str(i) + " " + Sights[i].name)

    print("Введите номер непонравившейся достопримечательности")
    chosEl = int(input())
    resultMatr, resultPosMatr = findFiveFurthest(mainAdjaMatr, chosEl)
    print("Исходя из того что вам не понравилась такая достопримечательность как " + str(Sights[chosEl].name) +
          ", мы рекомендуем вам посетить нижеперечисленные достопримечательности:")
    printResult(Sights, resultMatr, resultPosMatr)

    return resultMatr, resultPosMatr


def singleLikeAfter(Sights, mainAdjaMatr):
    for i in range(len(Sights)):
        print(str(i) + " " + Sights[i].name)

    print("Введите номер понравившейся достопримечательности")
    chosEl = int(input())
    resultMatr, resultPosMatr = findFiveClosestAfter(Sights, mainAdjaMatr, chosEl)
    print("Исходя из того что вам понравилась такая достопримечательность как " + str(Sights[chosEl].name) +
          ", мы рекомендуем вам посетить нижеперечисленные достопримечательности:")
    printResult(Sights, resultMatr, resultPosMatr)

    return resultMatr, resultPosMatr


def singleDislikeAfter(Sights, mainAdjaMatr):
    for i in range(len(Sights)):
        print(str(i) + " " + Sights[i].name)

    print("Введите номер непонравившейся достопримечательности")
    chosEl = int(input())
    resultMatr, resultPosMatr = findFiveFurthestAfter(Sights, mainAdjaMatr, chosEl)
    print("Исходя из того что вам не понравилась такая достопримечательность как " + str(Sights[chosEl].name) +
          ", мы рекомендуем вам посетить нижеперечисленные достопримечательности:")
    printResult(Sights, resultMatr, resultPosMatr)

    return resultMatr, resultPosMatr


def multipleLikesDislikes(Sights, mainAdjaMatr):
    for i in range(len(Sights)):
        print(str(i) + " " + Sights[i].name)

    print("Введите количество понравившихся достопримечательностей")
    n = int(input())
    if n > 0:
        massL = list()
        for i in range(n):
            print("Введите номер " + str(i + 1) + " понравившейся достопримечательности")
            inNumb = int(input())
            if inNumb not in massL:
                massL.append(inNumb)
    else:
        massL = []

    print("Введите количество непонравившихся достопримечательностей")
    m = int(input())
    if m > 0:
        massD = list()
        for i in range(m):
            print("Введите номер " + str(i + 1) + " непонравившейся достопримечательности")
            inNumb = int(input())
            if inNumb not in massD:
                massD.append(inNumb)
    else:
        massD = []

    finalPosMatr = findFiveCombined(massL, massD, mainAdjaMatr)
    print("Ваши предпочтения:")
    print("Лайки:")
    for i in range(len(massL)):
        print(Sights[massL[i]].name)
    print("Дизлайки:")
    for i in range(len(massD)):
        print(Sights[massD[i]].name)
    print("Исходя из ваших предпочтений, мы подобрали вам нижеперечисленные досторимечательности:")
    for i in range(len(finalPosMatr)):
        print("Название: " + str(Sights[finalPosMatr[i]].name))

    return finalPosMatr


def multipleLikesDislikesAfter(Sights, mainAdjaMatr):
    for i in range(len(Sights)):
        print(str(i) + " " + Sights[i].name)

    print("Введите количество понравившихся достопримечательностей")
    n = int(input())
    if n > 0:
        massL = list()
        for i in range(n):
            print("Введите номер " + str(i + 1) + " понравившейся достопримечательности")
            inNumb = int(input())
            if inNumb not in massL:
                massL.append(inNumb)
    else:
        massL = []

    print("Введите количество непонравившихся достопримечательностей")
    m = int(input())
    if m > 0:
        massD = list()
        for i in range(m):
            print("Введите номер " + str(i + 1) + " непонравившейся достопримечательности")
            inNumb = int(input())
            if inNumb not in massD:
                massD.append(inNumb)
    else:
        massD = []

    finalPosMatr = findFiveCombinedAfter(Sights, massL, massD, mainAdjaMatr)
    print("Ваши предпочтения:")
    print("Лайки:")
    for i in range(len(massL)):
        print(Sights[massL[i]].name)
    print("Дизлайки:")
    for i in range(len(massD)):
        print(Sights[massD[i]].name)
    print("Исходя из ваших предпочтений, мы подобрали вам нижеперечисленные досторимечательности:")
    for i in range(len(finalPosMatr)):
        print("Название: " + str(Sights[finalPosMatr[i]].name))

    return finalPosMatr


def printFormatMatr(matr):
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            outStr = ""
            if matr[i][j] == 1:
                outStr = str(matr[i][j]) + "    "
            elif (matr[i][j] * 100) % 10 != 0:
                outStr = str(matr[i][j]) + " "
            else:
                outStr = str(matr[i][j]) + "  "
            print(outStr, end="")

        print("")


def printSightsInfo(Sights):
    typeDict = {2: "Здание",
                4: "Группа зданий с единой архитектурой",
                5: "Группа зданий с различной архитектурой",
                6: "Архитектурное Чудо Света",
                7: "Сооружение",
                10: "Исторический памятник",
                11: "Памятник искусства",
                12: "Обычное место с культурной ценностью",
                14: "Храм крупной религии",
                15: "Храм малой религии",
                17: "Природное Чудо Света",
                18: "Заповедник",
                19: "Заповедник",
                20: "Национальный парк",
                21: "Связанные с водой",
                22: "Ботанический сад",
                24: "Стрит-фуд",
                25: "Ресторан",
                26: "Рынок",
                27: "Паб",
                29: "Ферма",
                30: "Производство продуктов питания"}
    for i in range(len(Sights)):
        print("Название: " + Sights[i].name)
        print("Тип: " + typeDict.get(Sights[i].treeNumber))
        print("Страна: " + Sights[i].country)
        print("Стоимость посещения: " + str(Sights[i].price) + "$")
        print("Лучшее время для посещения: ", end="")
        for j in range(len(Sights[i].bestSeason)):
            print(Sights[i].bestSeason[j], end=", ")

        print("")
