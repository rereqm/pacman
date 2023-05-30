from objects.texts import RecalculableText
from logic.score import ScoreCounter
class ScoreDrawer(RecalculableText):
    def __init__(self, x, y, size, color):
        self.counter = ScoreCounter()
        super().__init__(x, y, 'Scores: {}', size, color)
        self.text_format = self.text
        self.recreate_text(self.counter.get())

    def add_scores(self,scores):
        self.counter.add(scores)
        self.recreate_text(self.counter.get())
