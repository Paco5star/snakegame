from turtle import Turtle




class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as self.data:
            self.highscore = self.data.read()
            int(self.highscore)
        self.high_score = self.highscore
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score} ", align="center", font=("Arial" , 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.high_score):
            with open("data.txt", mode="w") as self.data:
                self.data.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()



    # def game_over(self):
    #     self.color("white")
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER! Final score {self.score}", align="center", font=("Arial", 20, "normal"))