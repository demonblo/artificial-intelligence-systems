from matrix import *
from filters import *


def drawHeart():
    print('\n'.join(' '.join(*zip(*row)) for row in ([[
        "*" if row == 0 and col % 3 != 0 or row == 1 and col % 3 == 0 or row - col == 2 or row + col == 8 else " "
        for col in range(7)] for row in range(6)])))


def getRecomendationsFirst(Sights, mainAdjaMatr, AsiaMass, EuropeMass, AfricaMass, NorthAmericaMass, MiddleAmericaMass, SouthAmericaMass, OceanMass):
    recomendationsFlag = False # Рекомендации
    while not recomendationsFlag:
        print("Выберите вариант составления рекомендаций:")
        print("1. Выбор 1 лайка")
        print("2. Выбор 1 дизлайка")
        print("3. Выбор N лайков и M дизлайков")
        print("0. Пропустить")
        skipFlag = True
        check = False
        menuSelect = 1
        resultMass = list()
        while menuSelect != 0:
            menuSelect = int(input())
            if menuSelect == 1:
                skipFlag = False
                resultMatr, resultPosMatr = singleLike(Sights, mainAdjaMatr)
                for i in range(len(Sights)):
                    if i in resultPosMatr:
                        resultMass.append(Sights[i])
                menuSelect = 0
            elif menuSelect == 2:
                skipFlag = False
                resultMatr, resultPosMatr = singleDislike(Sights, mainAdjaMatr)
                for i in range(len(Sights)):
                    if i in resultPosMatr:
                        resultMass.append(Sights[i])
                menuSelect = 0
            elif menuSelect == 3:
                skipFlag = False
                resultMatr = multipleLikesDislikes(Sights, mainAdjaMatr)
                for i in range(len(Sights)):
                    if i in resultMatr:
                        resultMass.append(Sights[i])
                menuSelect = 0
            elif menuSelect == 0:
                print("Этап составления рекомендаций пропущен")
                recomendationsFlag = True
                skipFlag = True
                check = True
            else:
                print(";(")
                print("Некорректный ввод, выберите пункт еще раз!")

        if len(resultMass) == 0 and not skipFlag:
            print("По заданным понравившимся/непонравившимся достопримечательностям не удалось подобрать рекомендации :(")
            print("Попробуйте выбрать другие пункты меню или понравившиеся/непонравившиеся достопримечательности")
        elif not check and len(resultMass) != 0:
            print("Вас устраивают составленные рекомендации?")
            print("1. Да :)")
            print("2. Нет :(")
            while not check:
                checkSelect = int(input())
                if checkSelect == 1:
                    recomendationsFlag = True
                    check = True
                elif checkSelect == 2:
                    print("Очень жаль, что вам не понравились рекомендации, попробуйте выбрать другие пункты меню или "
                          "понравившиеся/непонравившиеся достопримечательности")
                    check = True
                else:
                    print(";(")
                    print("Некорректный ввод, выберите пункт еще раз!")
        elif skipFlag:
            resultMass = Sights

    print("Переход к этапу фильтрации")
    #Фильтрация
    filtrationFlag = False
    while not filtrationFlag:
        print("Виды фильтрации:")
        print("1. Фильтрация по типу")
        print("2. Фильтрация по сторонам Света")
        print("3. Фильтрация по стоимости(лингвистическая переменная)")
        print("4. Фильтрация по сезону")
        print("Введите количество фильтров, которое вы хотите применить(Для пропуска введите 0)")
        skipFlag = True
        check = False
        numbEl = int(input())
        finalResultMass = resultMass
        if numbEl != 0:
            selectedFiltersMass = list()
            while numbEl < 0 or numbEl > 4:
                print(";(")
                print("Некорректный ввод, введите еще раз!")
                numbEl = int(input())
            for i in range(numbEl):
                print("Введите номер " + str(i + 1) + " фильтра")
                inNumb = int(input())
                while inNumb not in range(5) or inNumb == 0:
                    print("Такого номера нет, введите еще раз!")
                    inNumb = int(input())
                if inNumb not in selectedFiltersMass:
                    selectedFiltersMass.append(inNumb)
            for i in range(len(selectedFiltersMass)):
                if selectedFiltersMass[i] == 1:
                    skipFlag = False
                    finalResultMass = typeFiltration(finalResultMass)
                elif selectedFiltersMass[i] == 2:
                    skipFlag = False
                    finalResultMass = countryFiltration(finalResultMass, AsiaMass, EuropeMass, AfricaMass, NorthAmericaMass, MiddleAmericaMass, SouthAmericaMass, OceanMass)
                elif selectedFiltersMass[i] == 3:
                    skipFlag = False
                    finalResultMass = priceCatFiltration(finalResultMass)
                elif selectedFiltersMass[i] == 4:
                    skipFlag = False
                    finalResultMass = monthFiltration(finalResultMass)

        if skipFlag:
            print("Этап фильтрации пропущен")
            finalResultMass = resultMass

        if len(finalResultMass) == 0:
            print("По заданным фильтрам не удалось подобрать достопримечательности :(")
            print("Попробуйте изменить фильтры или не применять фильтры вовсе")
        elif not check and len(finalResultMass) != 0:
            print("Вас устраивают отфильтрвоанные рекомендации?")
            print("1. Да :)")
            print("2. Нет :(")
            while not check:
                checkSelect = int(input())
                if checkSelect == 1:
                    filtrationFlag = True
                    check = True
                elif checkSelect == 2:
                    print(
                        "Очень жаль, что вам не понравились рекомендации, попробуйте выбрать другие фильтры или убрать их")
                    check = True
                else:
                    print(";(")
                    print("Некорректный ввод, выберите пункт еще раз!")

    return finalResultMass


def getFiltrationFirst(Sights, AsiaMass, EuropeMass, AfricaMass, NorthAmericaMass, MiddleAmericaMass, SouthAmericaMass, OceanMass):
    # Фильтрация
    filtrationFlag = False
    while not filtrationFlag:
        print("Виды фильтрации:")
        print("1. Фильтрация по типу")
        print("2. Фильтрация по сторонам Света")
        print("3. Фильтрация по стоимости(лингвистическая переменная)")
        print("4. Фильтрация по сезону")
        print("Введите количество фильтров, которое вы хотите применить(Для пропуска введите 0)")
        skipFlag = True
        check = False
        numbEl = int(input())
        resultMass = Sights
        if numbEl != 0:
            selectedFiltersMass = list()
            while numbEl < 0 or numbEl > 4:
                print(";(")
                print("Некорректный ввод, введите еще раз!")
                numbEl = int(input())
            for i in range(numbEl):
                print("Введите номер " + str(i + 1) + " фильтра")
                inNumb = int(input())
                while inNumb not in range(5) or inNumb == 0:
                    print("Такого номера нет, введите еще раз!")
                    inNumb = int(input())
                if inNumb not in selectedFiltersMass:
                    selectedFiltersMass.append(inNumb)
            for i in range(len(selectedFiltersMass)):
                if selectedFiltersMass[i] == 1:
                    skipFlag = False
                    resultMass = typeFiltration(resultMass)
                elif selectedFiltersMass[i] == 2:
                    skipFlag = False
                    resultMass = countryFiltration(resultMass, AsiaMass, EuropeMass, AfricaMass,
                                                        NorthAmericaMass, MiddleAmericaMass, SouthAmericaMass,
                                                        OceanMass)
                elif selectedFiltersMass[i] == 3:
                    skipFlag = False
                    resultMass = priceCatFiltration(resultMass)
                elif selectedFiltersMass[i] == 4:
                    skipFlag = False
                    resultMass = monthFiltration(resultMass)

        if skipFlag:
            print("Этап фильтрации пропущен")
            filtrationFlag = True

        if len(resultMass) == 0:
            print("По заданным фильтрам не удалось подобрать достопримечательности :(")
            print("Попробуйте изменить фильтры или не применять фильтры вовсе")
        elif not check and len(resultMass) != 0:
            print("Вас устраивают отфильтрвоанные рекомендации?")
            print("1. Да :)")
            print("2. Нет :(")
            while not check:
                checkSelect = int(input())
                if checkSelect == 1:
                    filtrationFlag = True
                    check = True
                elif checkSelect == 2:
                    print(
                        "Очень жаль, что вам не понравились рекомендации, попробуйте выбрать другие фильтры или убрать их")
                    check = True
                else:
                    print(";(")
                    print("Некорректный ввод, выберите пункт еще раз!")

    # Рекомендации
    recomendationsFlag = False
    countryAdjaMatr = createCountryAdjaMatr(resultMass, AsiaMass, EuropeMass, AfricaMass, NorthAmericaMass,
                                            MiddleAmericaMass, SouthAmericaMass, OceanMass)
    priceAdjaMatr = createPriceAdjaMatr(resultMass)
    treeAdjaMatr = createTreeAdjaMatr(resultMass)
    mainAdjaMatr = createMainAdjaMatr(resultMass, treeAdjaMatr, priceAdjaMatr, countryAdjaMatr)
    # КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ
    if len(resultMass) == 1:
        print("Так как после фильтрации подошла только 1 достопримечательность, то мы можем вам порекомендовать только её :)")
        finalResultMass = [resultMass[0]]
        recomendationsFlag = True
        printSightsInfo(resultMass)
    elif len(resultMass) == 2:
        print("Так как отфильтрованных достопримечательностей только 2, их мы вам и рекомендуем :)")
        finalResultMass = [resultMass[0], resultMass[1]]
        printSightsInfo(resultMass)
        recomendationsFlag = True
    elif len(resultMass) == 3:
        print("Так как отфильтрованных достопримечательностей только 3, их мы вам и рекомендуем :)")
        finalResultMass = [resultMass[0], resultMass[1], resultMass[2]]
        printSightsInfo(resultMass)
        recomendationsFlag = True
    elif len(resultMass) == 4:
        print("Так как отфильтрованных достопримечательностей только 4, их мы вам и рекомендуем :)")
        finalResultMass = [resultMass[0], resultMass[1], resultMass[2], resultMass[3]]
        printSightsInfo(resultMass)
        recomendationsFlag = True
    elif len(resultMass) == 5:
        print("Так как отфильтрованных достопримечательностей только 5, их мы вам и рекомендуем :)")
        finalResultMass = [resultMass[0], resultMass[1], resultMass[2], resultMass[3], resultMass[4]]
        printSightsInfo(resultMass)
        recomendationsFlag = True
    # КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ КОСТЫЛЬ
    while not recomendationsFlag:
        print("Выберите вариант составления рекомендаций:")
        print("1. Выбор 1 лайка")
        print("2. Выбор 1 дизлайка")
        print("3. Выбор N лайков и M дизлайков")
        print("0. Пропустить")
        skipFlag = True
        check = False
        menuSelect = 1
        finalResultMass = list()
        while menuSelect != 0:
            menuSelect = int(input())
            if menuSelect == 1:
                skipFlag = False
                resultMatr, resultPosMatr = singleLikeAfter(resultMass, mainAdjaMatr)
                for i in range(len(resultMass)):
                    if i in resultPosMatr:
                        finalResultMass.append(resultMass[i])
                menuSelect = 0
            elif menuSelect == 2:
                skipFlag = False
                resultMatr, resultPosMatr = singleDislikeAfter(resultMass, mainAdjaMatr)
                for i in range(len(resultMass)):
                    if i in resultPosMatr:
                        finalResultMass.append(resultMass[i])
                menuSelect = 0
            elif menuSelect == 3:
                skipFlag = False
                resultMatr = multipleLikesDislikesAfter(resultMass, mainAdjaMatr)
                for i in range(len(resultMass)):
                    if i in resultMatr:
                        finalResultMass.append(resultMass[i])
                menuSelect = 0
            elif menuSelect == 0:
                print("Этап составления рекомендаций пропущен")
                check = True
            else:
                print(";(")
                print("Некорректный ввод, выберите пункт еще раз!")

        if len(finalResultMass) == 0 and not skipFlag:
            print("По заданным понравившимся/непонравившимся достопримечательностям не удалось подобрать рекомендации :(")
            print("Попробуйте выбрать другие пункты меню или понравившиеся/непонравившиеся достопримечательности")
        elif not check and len(finalResultMass) != 0:
            print("Вас устраивают составленные рекомендации?")
            print("1. Да :)")
            print("2. Нет :(")
            while not check:
                checkSelect = int(input())
                if checkSelect == 1:
                    recomendationsFlag = True
                    check = True
                elif checkSelect == 2:
                    print("Очень жаль, что вам не понравились рекомендации, попробуйте выбрать другие пункты меню или "
                          "понравившиеся/непонравившиеся достопримечательности")
                    check = True
                else:
                    print(";(")
                    print("Некорректный ввод, выберите пункт еще раз!")
        elif skipFlag:
            recomendationsFlag = True
            finalResultMass = resultMass

    return finalResultMass
