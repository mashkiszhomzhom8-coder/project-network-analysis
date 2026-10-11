def table_events():
    file = open("events.csv", "w", encoding="utf-8")
    file.write("ID_EVENT;NAME\n")

    file.write("1;Начало проекта\n")
    file.write("2;Техническое задание разработано и согласовано\n")
    file.write("3;Анализ API образовательной платформы завершен\n")
    file.write("4;Модули сбора данных и правила информационной безопасности готовы\n")
    file.write("5;База данных и серверная инфраструктура развернуты\n")
    file.write("6;Программные компоненты нейрокуратора разработаны\n")
    file.write("7;Нейрокуратор внедрен в онлайн-школу\n")

    file.close()


def table_works():
    file = open("works.csv", "w", encoding="utf-8")
    file.write("ID_WORK;NAME;TN;ID_EVB;ID_EVE;TREB\n")

    file.write("1;Разработка ТЗ и согласование требований;4;1;2;ТЗ согласовано с заказчиком\n")
    file.write("2;Анализ API образовательной платформы;6;2;3;Определены доступные данные и методы интеграции\n")
    file.write("3;Утверждение политик безопасности по ФЗ-152;5;2;4;Установлены правила обработки персональных данных\n")
    file.write("4;Настройка облачной инфраструктуры сервера;6;2;5;Серверная среда подготовлена к размещению системы\n")
    file.write("5;Настройка парсинга данных успеваемости;3;3;4;Данные об успеваемости корректно собираются без потерь\n")
    file.write("6;Проектирование БД и конвейера данных ETL;8;3;5;Структура БД и поток обработки данных спроектированы\n")
    file.write("7;Программирование визуальных отчетов;8;4;6;Отчеты по прогрессу учащихся формируются корректно\n")
    file.write("8;Настройка LLM и интеграция Telegram API;7;5;6;Бот отвечает через Telegram и использует языковую модель. Длительность ответа бота не более 3 секунд\n")
    file.write("9;Подготовка документации для сотрудников;10;5;7;Инструкция для кураторов и преподавателей подготовлена\n")
    file.write("10;Тестирование бота и деплой;5;6;7;Система протестирована и размещена в рабочей среде\n")
    file.write("11;Нагрузочное тестирование парсеров;12;4;7;Парсинг выдерживает заданную нагрузку\n")
    file.write("12;Настройка алгоритма индивидуальных планов;9;3;6;Индивидуальные планы формируются на основе данных учащихся\n")
    file.write("13;Фиктивная работа(ожидание парсеров);0;4;5;Обеспечивает логическую зависимость между событиями\n")

    file.close()


def rasch_basetab(id_rasch, date, time, type_rasch):
    file = open("basetab_rasch.csv", "a", encoding="utf-8")

    file.write(f"{id_rasch};{date};{time};{type_rasch}\n")

    file.close()

def table_count(id_rasch, all_tp, all_tn):
    file = open("table_count.csv", "a", encoding="utf-8")

    for i in range(len(all_tp)):
        id_event = i + 1
        t1 = all_tp[i]
        t2 = all_tn[i]
        reserv = all_tn[i] - all_tp[i]

        file.write(f"{id_rasch};{id_event};{t1};{t2};{reserv}\n")
    file.write("\n")

    file.close()

def table_count_works(id_rasch, b, r_list):
    file = open("table_count_works.csv", "a", encoding="utf-8") # tn - то что ввел пользователь в ячейку

    for i in range(len(b)):
        id_work = i + 1
        tn = b[i]
        reserv = r_list[i]

        if reserv == 0:
            critical = "да"
        else:
            critical = "нет"

        file.write(f"{id_rasch};{id_work};{tn};{reserv};{critical}\n")
    file.write("\n")

    file.close()

def table_modeling(id_rasch, type_rasch, id_work, tn, reserv, zone):
    file = open("modeling.csv", 'a', encoding='utf-8')

    file.write(f'{id_rasch};{type_rasch};{id_work};{tn};{reserv};{zone}\n')

    file.close()

def table_summary(type_rasch, id_work, quant_crit, quant_precrit):
    file = open('table_summary.csv', 'a', encoding='utf-8')

    file.write(f'{type_rasch};{id_work};{quant_crit};{quant_precrit}\n')

    file.close()


def clear_result_files():
    files = [
        "basetab_rasch.csv",
        "table_count.csv",
        "table_count_works.csv"
    ]

    headers = [
        "ID_RASCH;DAT;TIM;TYPE_RASCH\n",
        "ID_RASCH;ID_EVENT;T1;T2;R\n",
        "ID_RASCH;ID_WORK;TN;R;CRITICAL\n"
    ]

    for i, filename in enumerate(files):
        file = open(filename, "w", encoding="utf-8")
        file.write(headers[i])
        file.close()

def clear_modeling():
    files = [
        "modeling.csv",
        'table_summary.csv'
    ]
    headers = [
        "ID_RASCH_M;TYPE_RASCH_M;ID_WORK;TN;RESERV;ZONE\n",
        "TYPE_RASCH_M;ID_WORK;CRITICAL_COUNT;PRECRITICAL_COUNT\n"
    ]
    for i, filename in enumerate(files):
        file = open(filename, "w", encoding="utf-8")
        file.write(headers[i])
        file.close()






