import os

def check_existance():
    exists = os.path.exists("template.txt")
    if not exists:
        create_template()
    exists2 = os.path.exists('txt_report_modeling_template.txt')
    if not exists2:
        create_template_modeling()

def create_template():
    file = open('template.txt', 'w', encoding='utf-8')

    file.write(f'{"ОТЧЕТ ПО РАСЧЕТУ НОМЕР [ID_RASCH]":^90}\n')
    file.write('Тип расчета: [TYPE_RASCH]\n')
    file.write('Дата расчета: [DATE]\n')
    file.write('Время расчета: [TIME]\n')
    file.write('Общая длительность проекта: [TOTAL_DURATION]\n')
    file.write('Критический путь: [CRITICAL]\n\n')

    file.write('Введенные значения длительности работ:\n[B_VALUES]\n\n')
    file.write('Отчет по каждому событию:\n[TABLE_COUNT]\n\n')
    file.write('Отчет по каждой работе:\n[TABLE_COUNT_WORKS]\n')

    file.close()

def upload_txt(calc_id, butt, date, time, tot_dur, crit, work, events_rep, works_rep):
    file = open('template.txt', 'r', encoding='utf-8')
    text = file.read()

    work_text = ', '.join(f'b{i+1}: {value}' for i, value in enumerate(work))
    critical_path_text = ", ".join(crit)

    text = text.replace('[ID_RASCH]', str(calc_id))
    text = text.replace('[TYPE_RASCH]', str(butt))
    text = text.replace('[DATE]', str(date))
    text = text.replace('[TIME]', str(time))
    text = text.replace('[TOTAL_DURATION]', str(tot_dur))
    text = text.replace('[CRITICAL]', str(critical_path_text))
    text = text.replace('[B_VALUES]', str(work_text))
    text = text.replace('[TABLE_COUNT]', str(events_rep))
    text = text.replace('[TABLE_COUNT_WORKS]', str(works_rep))

    file2 = open('report.txt', 'a', encoding='utf-8')
    file2.write(f'\n {text} \n')

    file.close()
    file2.close()


def create_template_modeling():
    file = open('txt_report_modeling_template.txt', 'w', encoding='utf-8')

    file.write(f'{"ОТЧЕТ ПО МОДЕЛИРОВАНИЮ РАСЧЕТОВ":^90}\n')
    file.write(f'Было проведено 1000 расчетов по каждому типу моделирования.\n\n')
    file.write(f'Моделирование 1: отклонение в пределах 1-3\n\n')
    file.write(f'Работа и кол-во раз, когда была критической:\n[crit_count1]\n')
    file.write(f'Работа и кол-во раз, когда была предкритической:\n[precrit_count1]\n\n')
    file.write(f'Моделирование 2: отклонение в пределах 4-7\n\n')
    file.write(f'Работа и кол-во раз, когда была критической:\n[crit_count2]\n')
    file.write(f'Работа и кол-во раз, когда была предкритической:\n[precrit_count2]\n\n')
    file.write(f'Моделирование 3: отклонение в пределах 8-15\n\n')
    file.write(f'Работа и кол-во раз, когда была критической:\n[crit_count3]\n')
    file.write(f'Работа и кол-во раз, когда была предкритической:\n[precrit_count3]\n\n')

    file.close()

def upload_model_rep(crit_count1, precrit_count1, crit_count2, precrit_count2, crit_count3, precrit_count3):
    file = open('txt_report_modeling_template.txt', 'r', encoding='utf-8')
    text = file.read()

    def dict_to_text(d):
        res = ''
        for key in d:
            percent = d[key]/1000 * 100
            res += f'{key:<10} {d[key]:<20} Процент: {percent:.2f}\n'
        return res


    text = text.replace('[crit_count1]', dict_to_text(crit_count1))
    text = text.replace('[precrit_count1]', dict_to_text(precrit_count1))
    text = text.replace('[crit_count2]', dict_to_text(crit_count2))
    text = text.replace('[precrit_count2]', dict_to_text(precrit_count2))
    text = text.replace('[crit_count3]', dict_to_text(crit_count3))
    text = text.replace('[precrit_count3]', dict_to_text(precrit_count3))

    file2 = open('txt_report_modeling.txt', 'a', encoding='utf-8')
    file2.write(f'\n {text} \n')

    file.close()
    file2.close()

def clear_txt():
    file1 = open('report.txt', 'w', encoding='utf-8')
    file2 = open('txt_report_modeling.txt', 'w', encoding='utf-8')
    file1.close()
    file2.close()




