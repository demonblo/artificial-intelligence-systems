```mermaid
flowchart TD
Достопримечательность ---> Культурная

Культурная ---> Country_of_residence_cultural[Страна где находится]
Культурная ---> Cost_of_visit_cultural[Стоимость посещения]
Культурная ---> Founding_date_cultural[Время строительства/основания]
Культурная ---> Count_of_visitors_cultural[Среднее количество посетителей в день]
Культурная ---> Guide_cultural[Лучше с гидом или без]
Культурная ---> Wild_animals_cultural[Наличие диких зверей]
Культурная ---> Needed_time_cultural[Время необходимое для посещения и осмотра]
Культурная ---> Relief_features_cultural[Наличие рельефных особенностей]
Культурная ---> Best_season_for_visit_cultural[Лучший сезон для посещения]

Country_of_residence_cultural ---> Countries_cultural[Одна или более из 194 стран]

Cost_of_visit_cultural ---> low_cost_cultural[0$ - 10$]
Cost_of_visit_cultural ---> upper_low_cost_cultural[11$ - 25$]
Cost_of_visit_cultural ---> medium_cost_cultural[26$ - 50$]
Cost_of_visit_cultural ---> upper_medium_cost_cultural[51$ - 100$]
Cost_of_visit_cultural ---> high_cost_cultural[100$ +]

Count_of_visitors_cultural ---> super_low_count_cultural[0 - 100]
Count_of_visitors_cultural ---> low_count_cultural[101 - 500]
Count_of_visitors_cultural ---> upper_low_count_cultural[501 - 1500]
Count_of_visitors_cultural ---> medium_count_cultural[1501 - 5000]
Count_of_visitors_cultural ---> upper_medium_count_cultural[5001 - 25000]
Count_of_visitors_cultural ---> high_count_cultural[25001 - 50000]
Count_of_visitors_cultural ---> mega_high_count_cultural[50001 +]

Guide_cultural ---> Better_with_guide_cultural[Лучше с гидом]
Guide_cultural ---> Better_without_guide_cultural[Лучше без гида]

Better_with_guide_cultural ---> Guide_dependecy_cultural[Зависимость от квалификации гида]

Guide_dependecy_cultural ---> Low_guide_dependecy_cultural[Низкая]
Guide_dependecy_cultural ---> High_guide_dependecy_cultural[Высокая]

Wild_animals_cultural ---> Presence_of_unique_animals_cultural[Наличие уникальных зверей]
Wild_animals_cultural ---> No_wild_animals_cultural[Нет]

Presence_of_unique_animals_cultural ---> Presence_of_unique_animals_yes_cultural[Есть]
Presence_of_unique_animals_cultural ---> Presence_of_unique_animals_no_cultural[Нет]

Relief_features_cultural ---> No_rilief_fetures_cultural[Нет]
Relief_features_cultural ---> Yes_rilief_fetures_cultural[Есть]

Best_season_for_visit_cultural ---> Period_cultural[Период из одного или нескольких месяцев]
```