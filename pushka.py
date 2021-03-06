from random import randrange as rnd, choice
import tkinter as tk #graphic library
import math
import time


root = tk.Tk() #created window
fr = tk.Frame(root)
root.geometry('800x600') #set the size of the window
canv = tk.Canvas(root, bg='white') #creates a white background surface
canv.pack(fill=tk.BOTH, expand=1) #object packing method, 'expand=1' makes label in the center of frame


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 10
        self.vy = 10
        self.g = 2.5
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x + self.r >= 800:
            self.vx = -0.7 * self.vx
            self.x =  799 - self.r
        if self.y + self.r >= 600:
            self.vy = -self.vy
            self.vx = 0.8 * self.vx
            self.y = 599 - self.r
        if abs(self.vy) < 2 and self.y > 599 - self.r:
            self.vx = 0
            self.vy = 0
            self.g = 0
        self.x += self.vx
        self.y -= self.vy
        self.vy -= self.g

    def draw_ball(self):
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )

    def del_ball(self):
        canv.delete(self.id)

    def ball_stop(self):
        if self.vx == 0 and self.vy == 0:
            if self.live == 0:
                return True
            else:
                self.live -= 1
                return False
        else:
            return False



    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if math.sqrt(abs(self.x - obj.pos_x()) **2 + abs(self.y - obj.pos_y())**2) < self.r + obj.radius():
            return True
        else:
            return False


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 1
        self.an = 0
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
            """Выстрел мячом.

            Происходит при отпускании кнопки мыши.
            Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
            """
            global balls, bullet
            bullet += 1
            new_ball = ball()
            new_ball.r += 5
            self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = - self.f2_power * math.sin(self.an)
            balls += [new_ball]
            self.f2_on = 0
            self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.points = 0
        self.live = 1
        self.vy = rnd(-5, 5)
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30,30,text ='' ,font = '28')
        self.new_target()

    def move(self):
        if self.y - self.r < 20:
            self.vy = -self.vy
        if self.y + self.r >= 550:
            self.vy = -self.vy
        self.y -= self.vy

    def draw_target(self):
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
    def del_target(self):
        canv.delete(self.id)

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def pos_x(self):
        return self.x
    def pos_y(self):
        return self.y
    def radius(self):
        return self.r

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points

    def score(self):
        return self.points

    def id_points_1(self):
        return self.id_points


t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []


def new_game(event=''):
    global gun, t1, screen1, balls, bullet
    t1.new_target()
    t2.new_target()
    t1.del_target()
    t2.del_target()
    bullet = 0
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    z = 0.0003
    t1.live = 1
    t2.live = 1
    while t1.live or t2.live or balls != []:
        delete = []
        t1.move()
        t2.move()
        if t1.live != 0:
            t1.draw_target()
        if t2.live != 0:
            t2.draw_target()

        for i in range(len(balls)):
            balls[i].move()
            if balls[i].hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
            if balls[i].hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
            if t1.live == 0 and t2.live == 0:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                canv.itemconfig(t1.id_points_1(), text=t1.score())
            balls[i].draw_ball()
            if balls[i].ball_stop() == True:
                balls[i].delete_ball()
                delete.append(i)
        for i in delete:
            del balls[i]


        canv.update()
        time.sleep(0.03)
        for b in balls:
            b.del_ball()
        t1.del_target()
        t2.del_target()
        g1.targetting()
        g1.power_up()


    canv.delete(gun)
    canv.itemconfig(screen1, text='')



while True:
    new_game()

