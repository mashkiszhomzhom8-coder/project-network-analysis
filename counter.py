from tkinter import *
from tkinter import messagebox
from math import sqrt
import random
import datetime
from matplotlib import pyplot as plt
from report import rasch_basetab, table_count, table_count_works, table_events, table_works, clear_result_files, table_modeling, table_summary, clear_modeling
from txt_report import upload_txt, check_existance, upload_model_rep, clear_txt


table_events()
table_works()

check_existance()

clear_result_files()
clear_modeling()
clear_txt()




root = Tk()
root.attributes("-fullscreen", True)
root.title("Расчет работ")
r = 0

base_values = [4, 6, 5, 6, 3, 8, 8, 7, 10, 5, 12, 9, 0]
work_names = [f"b{i+1}" for i in range(13)]
all_vars = []

def create_cells():
    global r
    for i in range(13):
        var = StringVar()
        var.set(str(base_values[i]))
        Label(root, text=f"b{i+1}:").grid(row=r, column=0, sticky=W)

        if i == 12:
            Entry(root, width=30, textvariable=var, state="disabled", disabledbackground="gray").grid(row=r, column=1, columnspan=2, sticky=W)
        else:
            Entry(root, width=30, textvariable=var).grid(row=r, column=1, columnspan=2, sticky=W)
        r = r + 1
        all_vars.append(var)

    return all_vars
create_cells()


c = Canvas(root, width=1370, height=1400, bg='#fff7ed')
c.grid(row=0, column=20, columnspan=20, rowspan=30, sticky=N+W)


e1 = c.create_oval(
    50, 680, 100, 730,
    width=2,
    fill='#9A3412',
    outline='black'
)

e2 = c.create_oval(
    150, 580, 200, 630,
    width=2,
    fill='#9A3412',
    outline='black'
)

e3 = c.create_oval(
    250, 480, 300, 530,
    width=2,
    fill='#9A3412',
    outline='black'
)

e4 = c.create_oval(
    450, 530, 500, 580,
    width=2,
    fill='#9A3412',
    outline='black'
)

e5 = c.create_oval(
    150, 330, 200, 380,
    width=2,
    fill='#9A3412',
    outline='black'
)

e6 = c.create_oval(
    350, 380, 400, 430,
    width=2,
    fill='#9A3412',
    outline='black'
)

e7 = c.create_oval(
    450, 280, 500, 330,
    width=2,
    fill='#9A3412',
    outline='black'
)

e_lst = [e1, e2, e3, e4, e5, e6, e7]


t1 = c.create_text(75, 705, text="1", font="Verdana 14 bold")
t2 = c.create_text(175, 605, text="2", font="Verdana 14 bold")
t3 = c.create_text(275, 505, text="3", font="Verdana 14 bold")
t4 = c.create_text(475, 555, text="4", font="Verdana 14 bold")
t5 = c.create_text(175, 355, text="5", font="Verdana 14 bold")
t6 = c.create_text(375, 405, text="6", font="Verdana 14 bold")
t7 = c.create_text(475, 305, text="7", font="Verdana 14 bold")

t_lst = [t1, t2, t3, t4, t5, t6, t7]


x1, y1 = 75, 705
x2, y2 = 175, 605
x3, y3 = 275, 505
x4, y4 = 475, 555
x5, y5 = 175, 355
x6, y6 = 375, 405
x7, y7 = 475, 305

R = 25



def create_arrow(x_start, y_start, x_end, y_end, text, text_x, text_y, width=2, dash=None):
    dx = x_end - x_start
    dy = y_end - y_start

    length = sqrt(dx ** 2 + dy ** 2)

    if length == 0:
        return

    ux = dx / length
    uy = dy / length

    new_x_start = x_start + ux * R
    new_y_start = y_start + uy * R

    new_x_end = x_end - ux * R
    new_y_end = y_end - uy * R

    line = c.create_line(
        new_x_start, new_y_start,
        new_x_end, new_y_end,
        arrow=LAST,
        width=width,
        dash=dash,
        fill="#431407"
    )

    text_on = c.create_text(
        text_x, text_y,
        text=text,
        fill='#FB923C',
        font="Verdana 10 bold",
    )
    return line



l1 = create_arrow(
    x1, y1, x2, y2,
    "b1",
    110, 655,
    width=2
)

l2 = create_arrow(
    x2, y2, x3, y3,
    "b2",
    215, 550,
    width=2
)

l3 = create_arrow(
    x2, y2, x4, y4,
    "b3",
    325, 570,
    width=2
)

l4 =create_arrow(
    x2, y2, x5, y5,
    "b4",
    160, 485,
    width=2
)

l5 = create_arrow(
    x3, y3, x4, y4,
    "b5",
    370, 520,
    width=2
)

l6 = create_arrow(
    x3, y3, x5, y5,
    "b6",
    237, 430,
    width=2
)

l7 = create_arrow(
    x4, y4, x6, y6,
    "b7",
    430, 470,
    width=2
)

l8 = create_arrow(
    x5, y5, x6, y6,
    "b8",
    275, 370,
    width=2
)

l9 = create_arrow(
    x5, y5, x7, y7,
    "b9",
    305, 320,
    width=2
)

l10 = create_arrow(
    x6, y6, x7, y7,
    "b10",
    412, 352,
    width=2
)

l11 = create_arrow(
    x4, y4, x7, y7,
    "b11",
    490, 430,
    width=2
)

l12 = create_arrow(
    x3, y3, x6, y6,
    "b12",
    330, 435,
    width=2
)

l13 = create_arrow(
    x4, y4, x5, y5,
    "b13",
    373, 475,
    width=2,
    dash=(5, 3)
)

l_lst = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13]



def count_graph(b):
    tp_1 = 0
    tp_2 = b[0]
    tp_3 = tp_2 + b[1]
    tp_4 = max(tp_2 + b[2], tp_3 + b[4])
    tp_5 = max(tp_2 + b[3], tp_3 + b[5], tp_4 + b[12])
    tp_6 = max(tp_5 + b[7], tp_3 + b[11], tp_4 + b[6])
    tp_7 = max(tp_6 + b[9], tp_5 + b[8], tp_4 + b[10])

    all_tp = [tp_1, tp_2, tp_3, tp_4, tp_5, tp_6, tp_7]

    tn_7 = tp_7
    tn_6 = tn_7 - b[9]  # b10: 6 -> 7
    tn_5 = min(tn_7 - b[8], tn_6 - b[7])
    tn_4 = min(tn_7 - b[10], tn_6 - b[6], tn_5 - b[12])
    tn_3 = min(tn_4 - b[4], tn_5 - b[5], tn_6 - b[11])
    tn_2 = min(tn_3 - b[1], tn_4 - b[2], tn_5 - b[3])
    tn_1 = tn_2 - b[0]

    all_tn = [tn_1, tn_2, tn_3, tn_4, tn_5, tn_6, tn_7]

    R_list = []
    for i in range(len(all_tp)):
        R_list.append(all_tn[i]-all_tp[i])

    r1 = tn_2 - tp_1 - b[0]
    r2 = tn_3 - tp_2 - b[1]
    r3 = tn_4 - tp_2 - b[2]
    r4 = tn_5 - tp_2 - b[3]
    r5 = tn_4 - tp_3 - b[4]
    r6 = tn_5 - tp_3 - b[5]
    r7 = tn_6 - tp_4 - b[6]
    r8 = tn_6 - tp_5 - b[7]
    r9 = tn_7 - tp_5 - b[8]
    r10 = tn_7 - tp_6 - b[9]
    r11 = tn_7 - tp_4 - b[10]
    r12 = tn_6 - tp_3 - b[11]
    r13 = tn_5 - tp_4 - b[12]

    r_list = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13]

    return all_tp, all_tn, r_list, R_list



def reset_graph():
    for l in l_lst:
        c.itemconfig(l, fill="#431407", width=2)
    for i in range(len(t_lst)):
        c.itemconfig(t_lst[i], text=f'{i+1}', font="Verdana 14 bold")



calc_id = 0
def count_path():
    global calc_id
    calc_id += 1

    reset_graph()

    b = [int(var.get()) for var in all_vars]

    all_tp, all_tn, r_list, R_list = count_graph(b)

    critical_path_nums = []
    for i in range(len(r_list)):
        if r_list[i] == 0:
            c.itemconfig(l_lst[i], fill="#fb623c", width=4)
            critical_path_nums.append(work_names[i])
    for i in range(len(t_lst)):
        c.itemconfig(t_lst[i], text = f'{i + 1}:\n{all_tp[i]}/{all_tn[i]}\nR={R_list[i]}', font="Verdana 9 bold", justify=CENTER)


    button_name = 'definited'
    data_load(r_list, all_tp, all_tn, b, button_name, critical_path_nums, R_list)

def count_rand():
    global calc_id
    calc_id += 1

    for i, var in enumerate(all_vars):
        var.set(str(base_values[i]))
    all_vars[12].set("0")
    reset_graph()

    b = []
    for var in all_vars:
        int_var = int(var.get())
        var.set(random.randint(int_var-round(0.3*int_var), int_var+round(0.3*int_var)))
        b.append(int(var.get()))

    all_tp, all_tn, r_list, R_list = count_graph(b)

    critical_path_nums = []
    for i in range(len(r_list)):
        if r_list[i] == 0:
            c.itemconfig(l_lst[i], fill="#fb623c", width=4)
            critical_path_nums.append(work_names[i])
    for i in range(len(t_lst)):
        c.itemconfig(t_lst[i], text=f'{i + 1}:\n{all_tp[i]}/{all_tn[i]}\nr={R_list[i]}',
                     font="Verdana 9 bold", justify=CENTER)

    button_name = 'random'
    data_load(r_list, all_tp, all_tn, b, button_name, critical_path_nums, R_list)



def data_load(r_list, all_tp, all_tn, b, button_name, critical_path_nums, R_list):
    now = datetime.datetime.now()

    fix_date = datetime.date.today()
    fix_time = now.strftime("%H:%M:%S")
    rasch_basetab(calc_id, fix_date, fix_time, button_name)

    table_count(calc_id, all_tp, all_tn)

    table_count_works(calc_id, b, r_list)

    tot_dur = all_tp[-1]

    events_report = ''
    for i in range(len(all_tp)):
        id_event = i + 1
        t1 = all_tp[i]
        t2 = all_tn[i]
        reserv = R_list[i]
        events_report += f'Событие {id_event:<5} Ранний срок - {t1:<5} поздний - {t2:<5} резерв - {reserv:<5}\n'

    works_report = ''
    for i in range(len(b)):
        id_work = i + 1
        tn = b[i]
        reserv = r_list[i]
        if reserv == 0:
            critical = "да"
        else:
            critical = "нет"
        works_report += f"Работа b{id_work:<5} Длительность - {tn:<5} резерв - {reserv:<5} критическая ли - {critical:<5}\n"

    upload_txt(calc_id, button_name, fix_date, fix_time, tot_dur, critical_path_nums, b, events_report, works_report)


def generate_random_b(deviation:int):
    def g(alpha, betta):
        b = []
        for value in base_values:
            if value == 0:
                new_value = 0
            else:
                new_value = (random.randint(alpha, betta) + value)
            b.append(new_value)
        return b
    if deviation == 1:
        return g(1, 3)
    elif deviation == 2:
        return g(4, 7)
    elif deviation == 3:
        return g(8, 15)


def modeling_one_deviation(deviation):
    crit_count = {f'b{x + 1}': 0 for x in range(13)}
    precrit_count = {f'b{x + 1}': 0 for x in range(13)}

    for id_raschet in range(1, 1001):
        b = generate_random_b(deviation)
        all_tp, all_tn, r_list, R_list = count_graph(b)

        for ind, r in enumerate(r_list):
            index_plus1 = ind + 1
            work_name = f"b{index_plus1}"
            if r == 0:
                crit_count[work_name] += 1
                zone = 'критическая'
            elif 0 < r <= 3:
                precrit_count[work_name] += 1
                zone = 'предкритическая'
            elif r > 3:
                zone = 'не критическая'
            table_modeling(id_raschet, deviation, index_plus1, b[ind], r, zone)
    for x in range(13):
        index_plus1 = x + 1
        work_name = f"b{index_plus1}"
        table_summary(deviation, index_plus1, crit_count[work_name], precrit_count[work_name])



    return crit_count, precrit_count

def modeling():
    crit_count1, precrit_count1 = modeling_one_deviation(1)
    crit_count2, precrit_count2 = modeling_one_deviation(2)
    crit_count3, precrit_count3 = modeling_one_deviation(3)

    messagebox.showinfo("Готово", "Моделирование завершено")
    upload_model_rep(crit_count1, precrit_count1, crit_count2, precrit_count2, crit_count3, precrit_count3)
    plot(crit_count1, precrit_count1, crit_count2, precrit_count2, crit_count3, precrit_count3)


def plot(crit_count1, precrit_count1, crit_count2, precrit_count2, crit_count3, precrit_count3):
    list_of_dicts = [[crit_count1, precrit_count1], [crit_count2, precrit_count2], [crit_count3, precrit_count3]]
    fig, ax = plt.subplots(3, 2, figsize=(18, 12))
    diapason = ['в рамках отклонений 1-3', 'в рамках отклонений 4-7', 'в рамках отклонений 8-15']
    for i in range(13):
        for x in range(3):
            ax[x, 0].bar(i+1, list_of_dicts[x][0][f'b{i + 1}'])
            ax[x, 1].bar(i+1, list_of_dicts[x][1][f'b{i + 1}'])
            ax[x, 0].set_title(f"Критическая {diapason[x]}", fontsize=10)
            ax[x, 1].set_title(f"Предкритическая {diapason[x]}", fontsize=10)
    for a in ax.flat:
        a.grid(True)
        a.set_xlabel('Работа', fontsize=8, labelpad=0)
        a.set_ylabel("Кол-во раз", fontsize=8, labelpad=0)
        a.set_xticks(range(1, 14))

    plt.tight_layout()
    fig.subplots_adjust(hspace=0.4, wspace=0.25)
    fig.savefig("modeling_plot.pdf")
    plt.show()




Button(root, text="Расчет", command=count_path).grid(row=14, column=0, padx=(0, 0), pady=(0,0), sticky='w')

Button(root, text="Рандомый расчет +-30%", command=count_rand).grid(row=14, column=1, padx=(0, 0), pady=(0,0))

Button(root, text='Моделирование', command=modeling).grid(row=14, column=2, padx=(0, 0), pady=(0,0), sticky='e')




root.mainloop()