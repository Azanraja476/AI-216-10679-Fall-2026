class ScoreAnalyzer:
    def __init__(self, scores):
        self.scores = scores

    def average(self):
        if len(self.scores) == 0:
            return None
        return sum(self.scores) / len(self.scores)

    def count_above(self, threshold):
        return sum(1 for s in self.scores if s >= threshold)

    def highest(self):
        if len(self.scores) == 0:
            return None
        return max(self.scores)

    def lowest(self):
        if len(self.scores) == 0:
            return None
        return min(self.scores)