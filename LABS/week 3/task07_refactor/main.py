from preprocessing import clean_scores
from analyzer import ScoreAnalyzer

raw_data = [78, -5, 92, 110, 67, 88]
cleaned_data = clean_scores(raw_data)
analyzer = ScoreAnalyzer(cleaned_data)

print("Cleaned:", cleaned_data)
print("Average:", analyzer.average())
print("Highest:", analyzer.highest())
print("Lowest:", analyzer.lowest())
print("Count above 70:", analyzer.count_above(70))