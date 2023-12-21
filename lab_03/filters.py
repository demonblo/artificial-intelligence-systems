def getSelectedTypes(Sights, selectedTypesMass):
    resultMass = list()
    for i in range(len(Sights)):
        if Sights[i].treeNumber in selectedTypesMass:
            resultMass.append(Sights[i])

    return resultMass


def getSelectedCountries(Sights, selectedCountriesMass, AsiaMass, EuropeMass, AfricaMass, NorthAmericaMass, MiddleAmericaMass, SouthAmericaMass, OceanMass):
    resultMass = list()
    resultDict = list()
    for i in range(len(Sights)):
        if Sights[i].country in AsiaMass and 1 in selectedCountriesMass:
            resultMass.append(Sights[i])
            resultDict.append(1)
        elif Sights[i].country in EuropeMass and 2 in selectedCountriesMass:
            resultMass.append(Sights[i])
            resultDict.append(2)
        elif Sights[i].country in AfricaMass and 3 in selectedCountriesMass:
            resultMass.append(Sights[i])
            resultDict.append(3)
        elif Sights[i].country in NorthAmericaMass and 4 in selectedCountriesMass:
            resultMass.append(Sights[i])
            resultDict.append(4)
        elif Sights[i].country in MiddleAmericaMass and 5 in selectedCountriesMass:
            resultMass.append(Sights[i])
            resultDict.append(5)
        elif Sights[i].country in SouthAmericaMass and 6 in selectedCountriesMass:
            resultMass.append(Sights[i])
            resultDict.append(6)
        elif Sights[i].country in OceanMass and 7 in selectedCountriesMass:
            resultMass.append(Sights[i])
            resultDict.append(7)

    return resultMass, resultDict


def getSelectedPrice(Sights, minPrice, maxPrice):
    resultMass = list()
    for i in range(len(Sights)):
        if minPrice <= Sights[i].price <= maxPrice:
            resultMass.append(Sights[i])

    return resultMass


def getSelectedCat(Sights, selectedCatMass):
    resultMass = list()
    for i in range(len(Sights)):
        if Sights[i].price == 0 and 1 in selectedCatMass:
            resultMass.append(Sights[i])
        elif 0 < Sights[i].price <= 10 and 2 in selectedCatMass:
            resultMass.append(Sights[i])
        elif 10 < Sights[i].price <= 20 and 3 in selectedCatMass:
            resultMass.append(Sights[i])
        elif 20 < Sights[i].price <= 50 and 4 in selectedCatMass:
            resultMass.append(Sights[i])
        elif 50 < Sights[i].price <= 100 and 5 in selectedCatMass:
            resultMass.append(Sights[i])
        elif 100 < Sights[i].price <= 500 and 6 in selectedCatMass:
            resultMass.append(Sights[i])
        elif 500 < Sights[i].price and 7 in selectedCatMass:
            resultMass.append(Sights[i])

    return resultMass


def getSelectedMonths(Sights, selectedMonthsMass):
    resultMass = list()
    for i in range(len(Sights)):
        for j in range(len(Sights[i].bestSeason)):
            if Sights[i].bestSeason[j].lower() in selectedMonthsMass:
                resultMass.append(Sights[i])
                break

    return resultMass


def typeFiltration(Sights):
    typeMass = [2, 4, 5, 6, 7, 10, 11, 12, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 29, 30]
    print("Ниже приведен список всех типов достопримечательностей:")
    print("2. Здание")
    print("4. Группа зданий с единой архитектурой")
    print("5. Группа зданий с различной архитектурой")
    print("6. Архитектурное Чудо Света")
    print("7. Сооружение")
    print("10. Исторический памятник")
    print("11. Памятник искусства")
    print("12. Обычное место с культурной ценностью")
    print("14. Храм крупной религии")
    print("15. Храм малой религии")
    print("17. Природное Чудо Света")
    print("18. Заповедник")
    print("19. Зоопарк")
    print("20. Национальный парк")
    print("21. Связанные с водой")
    print("22. Ботанический сад")
    print("24. Стрит-фуд")
    print("25. Ресторан")
    print("26. Рынок")
    print("27. Паб")
    print("29. Ферма")
    print("30. Производство продуктов питания")
    print("Всего типов 21")
    print("Введите количество типов, которые вас интересуют(Для отмены введите 0):")
    numbEl = int(input())
    resultMass = Sights
    if numbEl != 0:
        while numbEl < 0 or numbEl > 21:
            print(";(")
            print("Некорректный ввод, введите еще раз!")
            numbEl = int(input())
        selectedTypesMass = list()
        for i in range(numbEl):
            print("Введите " + str(i + 1) + " выбранный тип")
            inNumb = int(input())
            while inNumb not in typeMass:
                print("Такого номера нет, введите еще раз!")
                inNumb = int(input())
            if inNumb not in selectedTypesMass:
                selectedTypesMass.append(inNumb)
        resultMass = getSelectedTypes(Sights, selectedTypesMass)

        print("Исходя из выбранных вами типов, ниже представленны достопримечательности после фильтрации:")
        for i in range(len(resultMass)):
            print("Название: " + str(resultMass[i].name))

    return resultMass


def countryFiltration(Sights, AsiaMass, EuropeMass, AfricaMass, NorthAmericaMass, MiddleAmericaMass, SouthAmericaMass, OceanMass):
    countryDict = {1: "Азия",
                   2: "Европа",
                   3: "Африка",
                   4: "Северная Америка",
                   5: "Центральная Америка",
                   6: "Южная Америка",
                   7: "Австралия и Океания"}
    print("Ниже приведен список всех сторон света:")
    print("1. " + countryDict.get(1))
    print("2. " + countryDict.get(2))
    print("3. " + countryDict.get(3))
    print("4. " + countryDict.get(4))
    print("5. " + countryDict.get(5))
    print("6. " + countryDict.get(6))
    print("7. " + countryDict.get(7))
    print("Введите количество сторон Света, которые вас интересуют(Для отмены введите 0):")
    numbEl = int(input())
    resultMass = Sights
    if numbEl != 0:
        while numbEl < 0 or numbEl > 7:
            print(";(")
            print("Некорректный ввод, введите еще раз!")
            numbEl = int(input())
        selectedCountriesMass = list()
        for i in range(numbEl):
            print("Введите " + str(i + 1) + " выбранную сторону Света")
            inNumb = int(input())
            while inNumb not in range(8) or inNumb == 0:
                print("Такого номера нет, введите еще раз!")
                inNumb = int(input())
            if inNumb not in selectedCountriesMass:
                selectedCountriesMass.append(inNumb)
        resultMass, resultDict = getSelectedCountries(Sights, selectedCountriesMass, AsiaMass, EuropeMass, AfricaMass,
                                                      NorthAmericaMass, MiddleAmericaMass, SouthAmericaMass, OceanMass)

        print("Исходя из выбранных вами сторон Света, ниже представленны достопримечательности после фильтрации:")
        for i in range(len(resultMass)):
            print("Название: " + str(resultMass[i].name))
            print("Страна: " + str(resultMass[i].country))
            print("Сторона Света: " + countryDict.get(resultDict[i]))
            print()

    return resultMass


def priceFiltration(Sights):
    print("Введите минимальную цену посещения достопримечательности(без значка '$', только число):")
    resultMass = Sights
    minPrice = int(input())
    if minPrice < 0:
        while minPrice < 0:
            print(";(")
            print("Некорректный ввод, введите еще раз!")
            minPrice = int(input())
    print("Введите максимальную цену посещения достопримечательности(без значка '$', только число):")
    maxPrice = int(input())
    if maxPrice < 0:
        while maxPrice < 0:
            print(";(")
            print("Некорректный ввод, введите еще раз!")
            maxPrice = int(input())
    if maxPrice < minPrice:
        while maxPrice < minPrice:
            print(";(")
            print("Максимальная цена не может быть ниже минимальной, введите еще раз!")
            maxPrice = int(input())

    resultMass = getSelectedPrice(Sights, minPrice, maxPrice)
    print("Исходя из выбранного вами ценового диапозона, ниже представленны достопримечательности после фильтрации:")
    for i in range(len(resultMass)):
        print("Название: " + resultMass[i].name)
        print("Стоимость посещения: " + str(resultMass[i].price) + "$")
        print()

    return resultMass


def priceCatFiltration(Sights):
    print("Ниже приведен список категорий стоимости:")
    print("1. Очень низкая стоимость(Бесплатно)")
    print("2. Низкая стоимость(от 1$ до 10$)")
    print("3. Не очень низкая стоимость(от 11$ до 20$)")
    print("4. Средняя стоимость(от 21$ до 50$)")
    print("5. Не очень высокая стоимость(от 51$ до 100$)")
    print("6. Высокая стоимость(от 101$ до 500$)")
    print("7. Очень высокая стоимость(от 501$ и выше)")
    print("Введите количество категорий стоимости, которые вас интересуют(Для отмены введите 0):")
    numbEl = int(input())
    resultMass = Sights
    if numbEl != 0:
        while numbEl < 0 or numbEl > 7:
            print(";(")
            print("Некорректный ввод, введите еще раз!")
            numbEl = int(input())
        selectedCatMass = list()
        for i in range(numbEl):
            print("Введите " + str(i + 1) + " выбранную категорию")
            inNumb = int(input())
            while inNumb not in range(8) or inNumb == 0:
                print("Такого номера нет, введите еще раз!")
                inNumb = int(input())
            if inNumb not in selectedCatMass:
                selectedCatMass.append(inNumb)
        resultMass = getSelectedCat(Sights, selectedCatMass)
        print(
            "Исходя из выбранных вами ценовых категорий ниже представленны достопримечательности после фильтрации:")
        for i in range(len(resultMass)):
            print("Название: " + resultMass[i].name)
            print("Стоимость посещения: " + str(resultMass[i].price) + "$")
            print()

    return resultMass


def monthFiltration(Sights):
    monthDict = {1: "январь",
                 2: "февраль",
                 3: "март",
                 4: "апрель",
                 5: "май",
                 6: "июнь",
                 7: "июль",
                 8: "август",
                 9: "сентябрь",
                 10: "октябрь",
                 11: "ноябрь",
                 12: "декабрь"}
    print("Ниже приведен список месяцев:")
    print("1. " + monthDict.get(1))
    print("2. " + monthDict.get(2))
    print("3. " + monthDict.get(3))
    print("4. " + monthDict.get(4))
    print("5. " + monthDict.get(5))
    print("6. " + monthDict.get(6))
    print("7. " + monthDict.get(7))
    print("8. " + monthDict.get(8))
    print("9. " + monthDict.get(9))
    print("10. " + monthDict.get(10))
    print("11. " + monthDict.get(11))
    print("12. " + monthDict.get(12))
    print("Введите количество месяцев, которые вас интересуют(Для отмены введите 0):")
    resultMass = Sights
    numbEl = int(input())
    if numbEl != 0:
        while numbEl < 0 or numbEl > 12:
            print(";(")
            print("Некорректный ввод, введите еще раз!")
            numbEl = int(input())
        selectedMonthsMass = list()
        for i in range(numbEl):
            print("Введите номер " + str(i + 1) + " выбранного месяца")
            inNumb = int(input())
            while inNumb not in range(13) or inNumb == 0:
                print("Такого номера нет, введите еще раз!")
                inNumb = int(input())
            if monthDict.get(inNumb) not in selectedMonthsMass:
                selectedMonthsMass.append(monthDict.get(inNumb))
    resultMass = getSelectedMonths(Sights, selectedMonthsMass)
    print("Исходя из выбранных вами месяцев ниже представленны достопримечательности после фильтрации:")
    for i in range(len(resultMass)):
        print("Название: " + resultMass[i].name)
        print("Лучшее время для посещения: ")
        for j in range(len(resultMass[i].bestSeason)):
            print(str(resultMass[i].bestSeason[j]) + ",", end=" ")
        print("")
        print("")

    return resultMass
