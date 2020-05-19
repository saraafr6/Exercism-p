def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    if len(scores) >= 3:
        scores.sort(reverse=True)
        return scores[0:3]
    else:
        scores.sort(reverse=True)
        return scores