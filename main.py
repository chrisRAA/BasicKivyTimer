from kivy.app import App

# Grafiske komponenter
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

# Properties til interaktion mellem python og kv
from kivy.properties import StringProperty

# Kivys interne clock til timing og framerate
from kivy.clock import Clock

import random


class ClickLayout(GridLayout):
    # Tekst paa knappen. Bundet via .kv. Bliver aendret i update.
    timerText = StringProperty('Set time')
    scoreText = StringProperty('0')
    score = 0
    clicktime = 20
    timeLeft = clicktime
    nextButton = 1
    pressed = []

    def update(self, dt):
        self.timeLeft -= dt
        self.timerText = str(round(self.timeLeft))
        self.scoreText = str(self.score)
        if self.timeLeft <= 0:
            self.reset()
            self.timeLeft = self.clicktime

    def buttonClicked(self, source):
        print(source.text)
        self.pressed.append(source.text)
        self.checkCorrect()

    def randomize(self):
        knapliste = ['knap1', 'knap2', 'knap3', 'knap4']
        knaptekster = ['1', '2', '3', '4']
        # Fordel 1-4 tilfældigt på knapperne
        random.shuffle(knaptekster)
        for knap in knapliste:
            self.ids[knap].text = knaptekster.pop()

    def reset(self):
        self.pressed = []

        self.randomize()

    def checkCorrect(self):
        if len(self.pressed) > 3:
            if self.pressed == ["1", "2", "3", "4"]:
                print("You are not a dumb piece of shit")
                self.score +=1
                self.reset()
            else:
                print("You are a dumb piece of shit")
                self.score -=1
                self.reset()



class ClickerApp(App):

    def build(self):
        # Initialiser knappen
        layout = ClickLayout()
        layout.randomize()
        # Bed Kivy om at kalde update() 30 gange pr. sekund
        Clock.schedule_interval(layout.update, 1.0 / 30.0)

        return layout


if __name__ in ('__main__', '__android__'):
    ClickerApp().run()
