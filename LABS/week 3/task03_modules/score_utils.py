def calculate_average(scores):
    if len(scores) == 0:
        return None
    return sum(scores) / len(scores)

def is_passing(score, passing_score=50):
    return score >= passing_score

def count_above_threshold(scores, threshold):
    return sum(1 for s in scores if s >= threshold)

if __name__ == "__main__":
    print("Running score_utils directly")