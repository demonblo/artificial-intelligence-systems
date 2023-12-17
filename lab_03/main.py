from matrix import *

if __name__ == "__main__":
    Sights = makeSightsArray()
    AsiaMass = ["Абхазия", "Азербайджан", "Армения", "Бангладеш", "Бахрейн", "Бруней", "Бутан", "Восточный Тимор",
                "Вьетнам",
                "Грузия", "Израиль", "Индия", "Индонезия", "Иордания", "Ирак", "Иран", "Йемен", "Казахстан", "Камбоджа",
                "Киргизия", "Китай", "Кувейт", "Лаос", "Малайзия", "Мальдивы", "Монголия", "Мьянма", "Непал", "ОАЭ",
                "Оман",
                "Пакистан", "Палестина", "Азиатская Россия", "Саудовская Аравия", "Северная Корея", "Сингапур", "Сирия",
                "Таджикистан", "Таиланд", "Туркмения", "Турция", "Узбекистан", "Филиппины", "Шри-Ланка", "Южная Корея",
                "Япония"]

    EuropeMass = ["Австрия", "Албания", "Андорра", "Беларусь", "Бельгия", "Болгария", "Босния и Герцоговина", "Ватикан",
                  "Великобритания", "Венгрия", "Германия", "Греция", "Дания", "Ирландия", "Исландия", "Испания",
                  "Италия",
                  "Кипр", "Латвия", "Литва", "Лихтенштейн", "Люксембург", "Мальта", "Молдавия", "Монако", "Нидерланды",
                  "Норвегия", "Польша", "Португалия", "Европейская Россия", "Румыния", "Сан-Марино",
                  "Северная Македония",
                  "Сербия", "Словакия", "Словения", "Украина", "Финляндия", "Франция", "Хорватия", "Черногория",
                  "Чехия",
                  "Швейцария", "Швеция", "Эстония"]

    AfricaMass = ["Алжир", "Ангола", "Бенин", "Ботсвана", "Буркина-Фасо", "Бурунди", "Габон", "Гамбия", "Гана",
                  "Гвинея",
                  "Гвинея", "Гвинея-Бисау", "Демократическая Республика Конго", "Джибути", "Египет", "Замбия",
                  "Западная Сахара", "Зимбабве", "Кабо-Верде", "Камерун", "Кения", "Коморские острова", "Конго",
                  "Кот-д'Ивуар",
                  "Лесото", "Либерия", "Ливан", "Ливия", "Маврикий", "Мавритания", "Мадагаскар", "Малави", "Мали",
                  "Марокко",
                  "Мозамбик", "Намбия", "Нигер", "Нигерия", "Руанда", "Сан-Томе и Принсипи", "Сейшельские острова",
                  "Сенегал",
                  "Сомали", "Судан", "Сьерра-Леоне", "Танзания", "Того", "Тунис", "Уганда", "ЦАР", "Чад",
                  "Экваториальная Гвинея",
                  "Эритрея", "Эсватини", "Эфиопия", "ЮАР", "Южный Судан"]

    NorthAmericaMass = ["Антигуа и Барбуда", "Багамские острова", "Барбадос", "Гаити", "Гренада", "Доминика",
                        "Доминиканская Республика", "Канада", "Куба", "Мексика", "Сент-Винсент и Гренадины",
                        "Сент-Китс и Невис", "Сент-Люсия", "США", "Тринидад и Тобаго"]

    MiddleAmericaMass = ["Белиз", "Гватемала", "Гондурас", "Коста-Рика", "Никарагуа", "Памана", "Сальвадор",
                         "Суринам"]

    SouthAmericaMass = ["Аргентина", "Боливия", "Бразилия", "Венесуэла", "Гайана", "Колумбия", "Парагвай", "Перу",
                        "Уругвай",
                        "Чили", "Эквадор", "Ямайка"]

    OceanMass = ["Австралия", "Вануату", "Кирибати", "Маршалловы острова", "Микронезия", "Науру", "Новая Зеландия",
                 "Палау",
                 "Папуа - Новая Гвинея", "Самоа", "Соломоновы острова", "Тонга", "Тувалу", "Фиджи"]

    #outputCountryInfo(Sights, AsiaMass, EuropeMass, AfricaMass, NorthAmericaMass, MiddleAmericaMass, SouthAmericaMass, OceanMass)

    countryAdjaMatr = createCountryAdjaMatr(Sights, AsiaMass, EuropeMass, AfricaMass, NorthAmericaMass, MiddleAmericaMass, SouthAmericaMass, OceanMass)

    #printFormatMatr(countryAdjaMatr)

    priceAdjaMatr = createPriceAdjaMatr(Sights)

    treeAdjaMatr = createTreeAdjaMatr(Sights)

    mainAdjaMatr = createMainAdjaMatr(treeAdjaMatr, priceAdjaMatr, countryAdjaMatr)
    print("")
    #printFormatMatr(priceAdjaMatr)
    print("")
    #printFormatMatr(treeAdjaMatr)
    print("")
    #printFormatMatr(mainAdjaMatr)

    print("Здравствуйте! Вас приветствует рекомендательная система 'Хочу туда!'")
    print("Выберете один из пунктов меню:")
    print("1. Выбор 1 лайка")
    print("2. Выбор 1 дизлайка")
    print("3. Выбор N лайков и M дизлайков")
    menuSelect = int(input())
    if menuSelect == 1:
        for i in range(countOfElements):
            print(str(i) + " " + Sights[i].name)

        print("Введите номер понравившейся достопримечательности")
        chosEl = int(input())
        finalMatr, finalPosMatr = findFiveClosest(mainAdjaMatr, chosEl)

        print("Исходя из того что вам понравилась такая достопримечательность как " + str(Sights[chosEl].name) +
              ", мы рекомендуем вам посетить нижеперечисленные достопримечательности:")
        for i in range(countOfRecomendations):
            print("Название:" + str(Sights[finalPosMatr[i]].name))
            print("Близость: " + str(finalMatr[i]))
    elif menuSelect == 2:
        for i in range(countOfElements):
            print(str(i) + " " + Sights[i].name)

        print("Введите номер непонравившейся достопримечательности")
        chosEl = int(input())
        finalMatr, finalPosMatr = findFiveFurthest(mainAdjaMatr, chosEl)
        print("Исходя из того что вам не понравилась такая достопримечательность как " + str(Sights[chosEl].name) +
              ", мы рекомендуем вам посетить нижеперечисленные достопримечательности:")
        for i in range(countOfRecomendations):
            print("Название: " + str(Sights[finalPosMatr[i]].name))
            print("Близость: " + str(finalMatr[i]))

    elif menuSelect == 3:
        for i in range(countOfElements):
            print(str(i) + " " + Sights[i].name)

        print("Введите количество понравившихся достопримечательностей")
        n = int(input())
        if n > 0:
            massL = list(range(n))
            for i in range(n):
                print("Введите номер " + str(i + 1) + " понравившейся достопримечательности")
                massL[i] = int(input())
        else:
            massL = []

        print("Введите количество непонравившихся достопримечательностей")
        m = int(input())
        if m > 0:
            massD = list(range(m))
            for i in range(m):
                print("Введите номер " + str(i + 1) + " непонравившейся достопримечательности")
                massD[i] = int(input())
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




