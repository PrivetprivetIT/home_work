# ANIMATION

## Что происходит
При запуске анимации на экране появляются синие кружки и зелёные квадраты разного размера, которые двигаются колебаниями.

## Класы
* Главный (он же родительский) класс **Shape**. От него наследуются два дочерних класса: **Circle** и **Square**.
* В классе **Shape** всего три функции: init, update_position и draw.
1. init - инициализатор и содержит в себе 6 параметров: *self*, *canvas*, *x*, *y*, *size*, *color*.
2. update_position - функция, которая обновляет координаты *x* и *y*, прибавляя к текущим значениям координат длины колебаний.
3. draw - функция, которая будет описываться в дочерних классах.
* Дочерние классы очень похожи друг на друга:
1. В функции init они при помощи функции **super()** наследуют *canvas*, *x*, *y*, *size*, *color*, при чём у кружков цвет синий, а к квадратов - зелёный (остальные параметры одинаковые).
2. Также у них описана функция draw. Она создаёт на холсте квадраты и кружки разного размера, взависимости от переменной *size*.

## Функции
В коде есть особая функция animate, которая задаёт рандомные длины колебаний и присваивает их каждому объекту на экране. Также эта функция запускает саму себя каждые 0.1 секунды, то есть обновляет колебания каждый раз по прошествии этого времени.

## Переменные
* *canvas_width* и *canvas_height* задают длину и ширину холста.
* *canvas* - сам холст.
* *x*, *y* - Кординаты объектов на холсте.
* *size* - размер объектов.
* *color* - цвет объектов.
* *dx*, *dy* - колебания объектов.

## Цикл
Завершающая часть кода - это цикл, который добавляет 20 фигур, у которых координаты, размер и сама форма рандомны.