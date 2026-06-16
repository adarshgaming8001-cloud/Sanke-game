from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Rectangle, Color
from random import randint

class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.label = Label(text="Score: 0", pos=(10, 450))
        self.add_widget(self.label)

        self.reset()

        Clock.schedule_interval(self.update, 0.15)

    def reset(self):
        self.snake = [[200, 200]]
        self.dir = [20, 0]
        self.food = [randint(0, 24)*20, randint(0, 24)*20]
        self.score = 0

    def update(self, dt):
        head = self.snake[0].copy()
        head[0] += self.dir[0]
        head[1] += self.dir[1]

        # game over reset
        if head[0] < 0 or head[0] >= 500 or head[1] < 0 or head[1] >= 500:
            self.reset()
            return

        if head in self.snake:
            self.reset()
            return

        self.snake.insert(0, head)

        if head == self.food:
            self.score += 1
            self.food = [randint(0, 24)*20, randint(0, 24)*20]
        else:
            self.snake.pop()

        self.label.text = "Score: " + str(self.score)

        self.draw()

    def draw(self):
        self.canvas.clear()
        with self.canvas:
            # snake
            Color(0, 1, 0)
            for s in self.snake:
                Rectangle(pos=s, size=(20, 20))

            # food
            Color(1, 0, 0)
            Rectangle(pos=self.food, size=(20, 20))

    def on_touch_down(self, touch):
        x, y = touch.pos
        hx, hy = self.snake[0]

        if abs(x - hx) > abs(y - hy):
            if x > hx:
                self.dir = [20, 0]
            else:
                self.dir = [-20, 0]
        else:
            if y > hy:
                self.dir = [0, 20]
            else:
                self.dir = [0, -20]

class SnakeApp(App):
    def build(self):
        return SnakeGame()

SnakeApp().run()