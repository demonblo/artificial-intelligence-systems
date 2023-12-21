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
