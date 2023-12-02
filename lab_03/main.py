class Sight(object):

    def __init__(self, name, treeNumber, country, cost, guideNeed, guideQuality, timeToSpend, dateOfFound, quantityOfVisitors, wildAnimals, uniqueAnimals, land, bestSeason, archStyle, religion, quantityOfFlora):
        self.name = name
        self.treeNumber = treeNumber
        self.country = country
        self.cost = cost
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

def makeeSightsArray():
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


def outputinfo(AsiaMass, EuropeMass, AfricaMass, NorthAmericaMass, MiddleAmericaMass, SouthAmericaMass, OceanMass):
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

if __name__ == "__main__":
    Sights = makeeSightsArray()
    AsiaMass = ["Абхазия","Азербайджан","Армения","Бангладеш","Бахрейн","Бруней","Бутан","Восточный Тимор","Вьетнам",
                "Грузия","Израиль","Индия","Индонезия","Иордания","Ирак","Иран","Йемен","Казахстан","Камбоджа",
                "Киргизия","Китай","Кувейт","Лаос","Малайзия","Мальдивы","Монголия","Мьянма","Непал","ОАЭ","Оман",
                "Пакистан","Палестина","Азиатская Россия","Саудовская Аравия","Северная Корея","Сингапур","Сирия",
                "Таджикистан", "Таиланд","Туркмения","Турция","Узбекистан","Филиппины","Шри-Ланка","Южная Корея",
                "Япония"]

    EuropeMass = ["Австрия","Албания","Андорра","Беларусь","Бельгия","Болгария","Босния и Герцоговина","Ватикан",
                  "Великобритания","Венгрия","Германия","Греция","Дания","Ирландия","Исландия","Испания","Италия",
                  "Кипр","Латвия","Литва","Лихтенштейн","Люксембург","Мальта","Молдавия","Монако","Нидерланды",
                  "Норвегия","Польша","Португалия","Европейская Россия","Румыния","Сан-Марино","Северная Македония",
                  "Сербия","Словакия","Словения","Украина","Финляндия","Франция","Хорватия","Черногория","Чехия",
                  "Швейцария","Швеция","Эстония"]

    AfricaMass = ["Алжир","Ангола","Бенин","Ботсвана","Буркина-Фасо","Бурунди","Габон","Гамбия","Гана","Гвинея",
                  "Гвинея","Гвинея-Бисау","Демократическая Республика Конго","Джибути","Египет","Замбия",
                  "Западная Сахара","Зимбабве","Кабо-Верде","Камерун","Кения","Коморские острова","Конго","Кот-д'Ивуар",
                  "Лесото","Либерия","Ливан","Ливия","Маврикий","Мавритания","Мадагаскар","Малави","Мали","Марокко",
                  "Мозамбик","Намбия","Нигер","Нигерия","Руанда","Сан-Томе и Принсипи","Сейшельские острова","Сенегал",
                  "Сомали","Судан","Сьерра-Леоне","Танзания","Того","Тунис","Уганда","ЦАР","Чад","Экваториальная Гвинея",
                  "Эритрея","Эсватини","Эфиопия","ЮАР","Южный Судан"]

    NorthAmericaMass = ["Антигуа и Барбуда","Багамские острова","Барбадос","Гаити","Гренада","Доминика",
                        "Доминиканская Республика","Канада","Куба","Мексика","Сент-Винсент и Гренадины",
                        "Сент-Китс и Невис","Сент-Люсия","США","Тринидад и Тобаго"]

    MiddleAmericaMass = ["Белиз","Гватемала","Гондурас","Коста-Рика","Никарагуа","Памана","Сальвадор",
                         "Суринам"]

    SouthAmericaMass = ["Аргентина","Боливия","Бразилия","Венесуэла","Гайана","Колумбия","Парагвай","Перу","Уругвай",
                        "Чили","Эквадор","Ямайка"]

    OceanMass = ["Австралия","Вануату","Кирибати","Маршалловы острова","Микронезия","Науру","Новая Зеландия","Палау",
                 "Папуа - Новая Гвинея","Самоа","Соломоновы острова","Тонга","Тувалу","Фиджи"]

    outputinfo(AsiaMass, EuropeMass, AfricaMass, NorthAmericaMass, MiddleAmericaMass, SouthAmericaMass, OceanMass)
