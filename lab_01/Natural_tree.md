```mermaid
flowchart TD
Достопримечательность ---> Природная

Природная ---> Country_of_residence_natural[Страна где находится]
Природная ---> Cost_of_visit_natural[Стоимость посещения]
Природная ---> Founding_date_natural[Время строительства/основания]
Природная ---> Count_of_visitors_natural[Среднее количество посетителей в день]
Природная ---> Guide_natural[Лучше с гидом или без]
Природная ---> Wild_animals_natural[Наличие диких зверей]
Природная ---> Needed_time_natural[Время необходимое для посещения и осмотра]
Природная ---> Relief_features_natural[Наличие рельефных особенностей]
Природная ---> Best_season_for_visit_natural[Лучший сезон для посещения]

Country_of_residence_natural ---> Countries_natural[Одна или более из 194 стран]

Cost_of_visit_natural ---> low_cost_natural[0$ - 10$]
Cost_of_visit_natural ---> upper_low_cost_natural[11$ - 25$]
Cost_of_visit_natural ---> medium_cost_natural[26$ - 50$]
Cost_of_visit_natural ---> upper_medium_cost_natural[51$ - 100$]
Cost_of_visit_natural ---> high_cost_natural[100$ +]

Count_of_visitors_natural ---> super_low_count_natural[0 - 100]
Count_of_visitors_natural ---> low_count_natural[101 - 500]
Count_of_visitors_natural ---> upper_low_count_natural[501 - 1500]
Count_of_visitors_natural ---> medium_count_natural[1501 - 5000]
Count_of_visitors_natural ---> upper_medium_count_natural[5001 - 25000]
Count_of_visitors_natural ---> high_count_natural[25001 - 50000]
Count_of_visitors_natural ---> mega_high_count_natural[50001 +]

Guide_natural ---> Better_with_guide_natural[Лучше с гидом]
Guide_natural ---> Better_without_guide_natural[Лучше без гида]

Better_with_guide_natural ---> Guide_dependecy_natural[Зависимость от квалификации гида]

Guide_dependecy_natural ---> Low_guide_dependecy_natural[Низкая]
Guide_dependecy_natural ---> High_guide_dependecy_natural[Высокая]

Wild_animals_natural ---> Presence_of_unique_animals_natural[Наличие уникальных зверей]
Wild_animals_natural ---> No_wild_animals_natural[Нет]

Presence_of_unique_animals_natural ---> Presence_of_unique_animals_yes_natural[Есть]
Presence_of_unique_animals_natural ---> Presence_of_unique_animals_no_natural[Нет]

Relief_features_natural ---> No_rilief_fetures_natural[Нет]
Relief_features_natural ---> Yes_rilief_fetures_natural[Есть]

Best_season_for_visit_natural ---> Period_natural[Период из одного или нескольких месяцев]
```