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
        check = False
        menuSelect = 1
        resultMass = list()
        while menuSelect != 0:
            menuSelect = int(input())
            if menuSelect == 1:
                resultMatr, resultPosMatr = singleLike(Sights, mainAdjaMatr)
                for i in range(len(Sights)):
                    if i in resultPosMatr:
                        resultMass.append(Sights[i])
                menuSelect = 0
            elif menuSelect == 2:
                resultMatr, resultPosMatr = singleDislike(Sights, mainAdjaMatr)
                for i in range(len(Sights)):
                    if i in resultPosMatr:
                        resultMass.append(Sights[i])
                menuSelect = 0
            elif menuSelect == 3:
                resultMatr = multipleLikesDislikes(Sights, mainAdjaMatr)
                for i in range(len(Sights)):
                    if i in resultMatr:
                        resultMass.append(Sights[i])
                menuSelect = 0
            elif menuSelect == 0:
                print("Этап составления рекомендаций пропущен")
                check = True
            else:
                print(";(")
                print("Некорректный ввод, выберите пункт еще раз!")

        if not check and len(resultMass) != 0:
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

    if len(resultMass) != 0:
        recMass = resultMass
    else:
        resultMass = Sights
        recMass = Sights
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
        numbEl = int(input())
        filtrationMass = Sights
        if numbEl != 0:
            selectedFiltersMass = list()
            while numbEl < 0 or numbEl > 4:
                print(";(")
                print("Некорректный ввод, введите еще раз!")
                numbEl = int(input())
            for i in range(numbEl):
                print("Введите номер " + str(i + 1) + " фильтра")
                inNumb = int(input())
                while inNumb not in range(4) or inNumb == 0:
                    print("Такого номера нет, введите еще раз!")
                    inNumb = int(input())
                if inNumb not in selectedFiltersMass:
                    selectedFiltersMass.append(inNumb)
            for i in range(len(selectedFiltersMass)):
                if selectedFiltersMass[i] == 1:
                    resultMass = typeFiltration(resultMass)
                    filtrationMass = typeFiltration(filtrationMass)
                elif selectedFiltersMass[i] == 2:
                    resultMass = countryFiltration(resultMass, AsiaMass, EuropeMass, AfricaMass, NorthAmericaMass, MiddleAmericaMass, SouthAmericaMass, OceanMass)
                    filtrationMass = countryFiltration(filtrationMass, AsiaMass, EuropeMass, AfricaMass, NorthAmericaMass, MiddleAmericaMass, SouthAmericaMass, OceanMass)
                elif selectedFiltersMass[i] == 3:
                    resultMass = priceCatFiltration(resultMass)
                    filtrationMass = priceCatFiltration(filtrationMass)
                elif selectedFiltersMass[i] == 4:
                    resultMass = monthFiltration(resultMass)
                    filtrationMass = monthFiltration(filtrationMass)



