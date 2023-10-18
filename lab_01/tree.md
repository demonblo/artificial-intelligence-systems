```mermaid
flowchart TD
Достопримечательность ---> Архитектурная
Достопримечательность ---> Культурная
Достопримечательность ---> Природная
Достопримечательность ---> Гастрономическая
Достопримечательность ---> World_miracle[Чудо света]

Гастрономическая ---> Country_of_residence_gastronomic[Страна где находится]
Гастрономическая ---> Cost_of_visit_gastronomic[Стоимость посещения]
Гастрономическая ---> Founding_date_gastronomic[Needed_timeемя строительства/основания]
Гастрономическая ---> Count_of_visitors_gastronomic[Среднее количество посетителей в день]

Country_of_residence_gastronomic ---> Countries_gastronomic[Одна или более из 194 стран]

Cost_of_visit_gastronomic ---> low_cost_gastronomic[0$ - 10$]
Cost_of_visit_gastronomic ---> upper_low_cost_gastronomic[11$ - 25$]
Cost_of_visit_gastronomic ---> medium_cost_gastronomic[26$ - 50$]
Cost_of_visit_gastronomic ---> upper_medium_cost_gastronomic[51$ - 100$]
Cost_of_visit_gastronomic ---> high_cost_gastronomic[100$ +]

Count_of_visitors_gastronomic ---> super_low_count_gastronomic[0 - 100]
Count_of_visitors_gastronomic ---> low_count_gastronomic[101 - 500]
Count_of_visitors_gastronomic ---> upper_low_count_gastronomic[501 - 1500]
Count_of_visitors_gastronomic ---> medium_count_gastronomic[1501 - 5000]
Count_of_visitors_gastronomic ---> upper_medium_count_gastronomic[5001 - 25000]
Count_of_visitors_gastronomic ---> high_count_gastronomic[25001 - 50000]
Count_of_visitors_gastronomic ---> mega_high_count_gastronomic[50001 +]

World_miracle ---> Country_of_residence_world_miracle[Страна где находится]
World_miracle ---> Cost_of_visit_world_miracle[Стоимость посещения]
World_miracle ---> Founding_date_world_miracle[Время строительства/основания]
World_miracle ---> Count_of_visitors_world_miracle[Среднее количество посетителей в день]
World_miracle ---> Guide_world_miracle[Лучше с гидом или без]
World_miracle ---> Wild_animals_world_miracle[Наличие диких зверей]
World_miracle ---> Needed_time_world_miracle[Время необходимое для посещения и осмотра]
World_miracle ---> Relief_features_world_miracle[Наличие рельефных особенностей]
World_miracle ---> Best_season_for_visit_world_miracle[Лучший сезон для посещения]

Country_of_residence_world_miracle ---> Countries_world_miracle[Одна или более из 194 стран]

Cost_of_visit_world_miracle ---> low_cost_world_miracle[0$ - 10$]
Cost_of_visit_world_miracle ---> upper_low_cost_world_miracle[11$ - 25$]
Cost_of_visit_world_miracle ---> medium_cost_world_miracle[26$ - 50$]
Cost_of_visit_world_miracle ---> upper_medium_cost_world_miracle[51$ - 100$]
Cost_of_visit_world_miracle ---> high_cost_world_miracle[100$ +]

Count_of_visitors_world_miracle ---> super_low_count_world_miracle[0 - 100]
Count_of_visitors_world_miracle ---> low_count_world_miracle[101 - 500]
Count_of_visitors_world_miracle ---> upper_low_count_world_miracle[501 - 1500]
Count_of_visitors_world_miracle ---> medium_count_world_miracle[1501 - 5000]
Count_of_visitors_world_miracle ---> upper_medium_count_world_miracle[5001 - 25000]
Count_of_visitors_world_miracle ---> high_count_world_miracle[25001 - 50000]
Count_of_visitors_world_miracle ---> mega_high_count_world_miracle[50001 +]

Guide_world_miracle ---> Better_with_guide_world_miracle[Лучше с гидом]
Guide_world_miracle ---> Better_without_guide_world_miracle[Лучше без гида]

Better_with_guide_world_miracle ---> Guide_dependecy_world_miracle[Зависимость от квалификации гида]

Guide_dependecy_world_miracle ---> Low_guide_dependecy_world_miracle[Низкая]
Guide_dependecy_world_miracle ---> High_guide_dependecy_world_miracle[Высокая]

Wild_animals_world_miracle ---> Presence_of_unique_animals_world_miracle[Наличие уникальных зверей]
Wild_animals_world_miracle ---> No_wild_animals_world_miracle[Нет]

Presence_of_unique_animals_world_miracle ---> Presence_of_unique_animals_yes_world_miracle[Есть]
Presence_of_unique_animals_world_miracle ---> Presence_of_unique_animals_no_world_miracle[Нет]

Relief_features_world_miracle ---> No_rilief_fetures_world_miracle[Нет]
Relief_features_world_miracle ---> Yes_rilief_fetures_world_miracle[Есть]

Best_season_for_visit_world_miracle ---> Period_world_miracle[Период из одного или нескольких месяцев]

Архитектурная ---> Country_of_residence_architectural[Страна где находится]
Архитектурная ---> Cost_of_visit_architectural[Стоимость посещения]
Архитектурная ---> Founding_date_architectural[Время строительства/основания]
Архитектурная ---> Count_of_visitors_architectural[Среднее количество посетителей в день]
Архитектурная ---> Guide_architectural[Лучше с гидом или без]
Архитектурная ---> Wild_animals_architectural[Наличие диких зверей]
Архитектурная ---> Needed_time_architectural[Время необходимое для посещения и осмотра]
Архитектурная ---> Relief_features_architectural[Наличие рельефных особенностей]
Архитектурная ---> Best_season_for_visit_architectural[Лучший сезон для посещения]

Country_of_residence_architectural ---> Countries_architectural[Одна или более из 194 стран]

Cost_of_visit_architectural ---> low_cost_architectural[0$ - 10$]
Cost_of_visit_architectural ---> upper_low_cost_architectural[11$ - 25$]
Cost_of_visit_architectural ---> medium_cost_architectural[26$ - 50$]
Cost_of_visit_architectural ---> upper_medium_cost_architectural[51$ - 100$]
Cost_of_visit_architectural ---> high_cost_architectural[100$ +]

Count_of_visitors_architectural ---> super_low_count_architectural[0 - 100]
Count_of_visitors_architectural ---> low_count_architectural[101 - 500]
Count_of_visitors_architectural ---> upper_low_count_architectural[501 - 1500]
Count_of_visitors_architectural ---> medium_count_architectural[1501 - 5000]
Count_of_visitors_architectural ---> upper_medium_count_architectural[5001 - 25000]
Count_of_visitors_architectural ---> high_count_architectural[25001 - 50000]
Count_of_visitors_architectural ---> mega_high_count_architectural[50001 +]

Guide_architectural ---> Better_with_guide_architectural[Лучше с гидом]
Guide_architectural ---> Better_without_guide_architectural[Лучше без гида]

Better_with_guide_architectural ---> Guide_dependecy_architectural[Зависимость от квалификации гида]

Guide_dependecy_architectural ---> Low_guide_dependecy_architectural[Низкая]
Guide_dependecy_architectural ---> High_guide_dependecy_architectural[Высокая]

Wild_animals_architectural ---> Presence_of_unique_animals_architectural[Наличие уникальных зверей]
Wild_animals_architectural ---> No_wild_animals_architectural[Нет]

Presence_of_unique_animals_architectural ---> Presence_of_unique_animals_yes_architectural[Есть]
Presence_of_unique_animals_architectural ---> Presence_of_unique_animals_no_architectural[Нет]

Relief_features_architectural ---> No_rilief_fetures_architectural[Нет]
Relief_features_architectural ---> Yes_rilief_fetures_architectural[Есть]

Best_season_for_visit_architectural ---> Period_architectural[Период из одного или нескольких месяцев]












```