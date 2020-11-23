#
#
#ТУТ БУДУТ СОБРАНЫ РАЗНЫЕ ФУНКЦИИ И ЭЛЕМЕНТЫ КОДА,КОТОРЫЕ ВРОДЕ КАК ИНОГДА ИСПОЛЬЗУЮ Я НО ПОСТОЯННО ПИСАТЬ ИХ Я ЗАЕБАЛСЯ 
#
#


#Преобразование двумерной матрицы в одномерную(прямую или линейную я хз)
def changing(matrix):
    lst = []
    for line in matrix:
        lst += line
    return lst
    
    
    
#Функция для отрисовки графика (на всякий)
def draw(mass1):
    dpi = 100
    fig = plt.figure(dpi = dpi, figsize = (1024 / dpi, 640 / dpi) )
    mpl.rcParams.update({'font.size': 10})
    plt.axis([20, 122, -0.1,0.1])#Координатная плоскость
    plt.title(f'График')
    plt.xlabel('x')
    plt.ylabel('Y')
    xs = []
    cos_vals = []
    x = 0
    while x < 122.0:
        cos_vals += [0]
        xs += [x]
        x += 1
    plt.plot(xs, cos_vals, color = 'blue', linestyle = 'solid',label = '!!!!!!!!')
    #Точки для 1 массива пока что
    size1=len(mass1)
    for i in range(size1):
        plt.scatter(mass1[i], 0, color ='green', s = 30, marker = '*')
        plt.vlines(mass1[i], -1, 1,color = 'b',linewidth = 0.3,linestyle = '--')
     #Можно реальзовать все графики на 1 пикче с помощью этой вещи(горизонт лин)
    plt.hlines(0.05, -1, 200,
          color = 'red',
          linewidth = 10,
          linestyle = '--')
    fig.savefig(f'Популяция.png')
    
    
    
    
    
    
    
    