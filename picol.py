import matplotlib.pyplot as plt
import numpy as np

action = 'Рисовать' # 'Экспорт' 'Вывод' 'Рисовать'

PI = open('c:\PI\pi_wout3.pi ', 'r')
output = open('c:\PI\output_hex_100K_woutP.pi ', 'a')
CLRS = open('c:\PI\output_hex_100K_woutP.pi ', 'r')
colors = CLRS.read()
text = PI.read()

quantity = 10000 # Количество цветов для вывода


def do_hex(pi):
    mass_pi = []
    b = quantity
    key = 0
    i = 1
    step1 = 0
    step2 = 3
    s = ''
    s1 = ''
    s2 = ''
    s3 = ''
    while b > 0:
        while i < 4:
            s = pi[step1:step2]
            if s == '000':
                s = '00'  # уже в hex
            else:
                s = hex(int(s))[2:]

            if int(len(s)) > 2:
                step2 -= 1
                key += 1
                continue
            else:
                if int(len(s)) == 1: s = '0' + str(s)
                if i == 1: s1 = s
                if i == 2: s2 = s
                if i == 3: s3 = s
                step1 += 3 - key
                step2 += 3
                i += 1
                key = 0

        i = 1
        s = '#' + s1 + s2 + s3
        mass_pi.append(s)
        b -= 1
    return mass_pi


def color_list(lst, q):
    string = lst.split(' ')
    mass = []
    mass.extend(string)
    return mass[0:q]


def draw():
    fig = plt.figure()
    ax = fig.add_subplot(111)  # добавление области рисования ax
    y = 1.0
    num = quantity
    n = 1
    k = 10
    while num > 0:
        x = np.arange(n, n + 1, 1)
        # my_hex = hex_mass(defined_color)[n - 1]

        ax.bar(x, y, color=color_list(colors, quantity + 1)[n - 1], alpha=1.00, align='center', \
               width=1)
        n += 1
        num -= 1
    plt.show()


def main():
    # print(color_list(colors))
    if action == 'Вывод':
        print(do_hex(text))
    if action == 'Рисовать':
        draw()
    # Выгрузка массива цветов в файл
    if action == 'Экспорт':
        output.write(str(do_hex(text)))

    PI.close()
    output.close()


if __name__ == '__main__':
    main()
