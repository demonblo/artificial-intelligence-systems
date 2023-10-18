```mermaid
flowchart TD
Достопримечательность ---> Архитектурная
Достопримечательность ---> Культурная
Достопримечательность ---> Природная
Достопримечательность ---> Гастрономическая
Достопримечательность ---> World_miracle[Чудо света]

Гастрономическая ---> Country_of_residence[Страна где находится]
Гастрономическая ---> Cost_of_visit[Стоимость посещения]
Гастрономическая ---> Founding_date[Needed_timeемя строительства/основания]
Гастрономическая ---> Count_of_visitors[Среднее количество посетителей в день]

Country_of_residence ---> Countries[Одна или более из 194 стран]

Cost_of_visit ---> low_cost[0$ - 10$]
Cost_of_visit ---> upper_low_cost[11$ - 25$]
Cost_of_visit ---> medium_cost[26$ - 50$]
Cost_of_visit ---> upper_medium_cost[51$ - 100$]
Cost_of_visit ---> high_cost[100$ +]

Count_of_visitors ---> super_low_count[0 - 100]
Count_of_visitors ---> low_count[101 - 500]
Count_of_visitors ---> upper_low_count[501 - 1500]
Count_of_visitors ---> medium_count[1501 - 5000]
Count_of_visitors ---> upper_medium_count[5001 - 25000]
Count_of_visitors ---> high_count[25001 - 50000]
Count_of_visitors ---> mega_high_count[50001 +]

World_miracle ---> Country_of_residence_world_miracle[Страна где находится]
World_miracle ---> Cost_of_visit_world_miracle[Стоимость посещения]
World_miracle ---> Founding_date_world_miracle[Время строительства/основания]
World_miracle ---> Count_of_visitors_world_miracle[Среднее количество посетителей в день]
World_miracle ---> Guide_world_miracle[Лучше с гидом или без]
World_miracle ---> Wild_animals_world_miracle[Наличие диких зверей]
World_miracle ---> Needed_time_world_miracle[Время необходимое для посещения и осмотра]
World_miracle ---> Relief_features_world_miracle[Наличие рельефных особенностей]

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















```