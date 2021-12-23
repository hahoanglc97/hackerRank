def climbingLeaderboard(scores, alice):
    currentrank = len(set(scores))
    score_index = 0
    highscore_index = len(scores) - 1
    out = []
    while score_index != len(alice):
        while alice[score_index] > scores[highscore_index] and highscore_index > -1:
            highscore_index -= 1
            if scores[highscore_index] != scores[highscore_index + 1]:
                currentrank -= 1
        if alice[score_index] == scores[highscore_index]:
            out.append(currentrank)
        else:
            out.append(currentrank + 1)
        score_index += 1
    print(out)


ranked = [100, 90, 90, 80, 75, 60]
player = [50, 65, 77, 90, 102]
climbingLeaderboard(ranked, player)
