"""
--- Part One ---
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y).
This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X).
This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?

--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway,
the second column says how the round needs to end: X means you need to lose,
Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what
shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y),
so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B),
and you choose Rock, so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column,
what would your total score be if everything goes exactly according to your strategy guide?
"""

OPPONENT_HAND_SHAPES = ["A", "B", "C"]
MY_HAND_SHAPES = ['X', 'Y', 'Z']
WIN_POINTS = 6
DRAW_POINTS = 3
LOSE_POINTS = 0


def get_my_hand_shape_points(hand_shape):
    return MY_HAND_SHAPES.index(hand_shape) + 1


def get_my_hand_shape(opponent_hand_shape, action):
    if opponent_hand_shape == OPPONENT_HAND_SHAPES[0]:
        if action == MY_HAND_SHAPES[0]:
            return MY_HAND_SHAPES[2]
        elif action == MY_HAND_SHAPES[1]:
            return MY_HAND_SHAPES[0]
        else:
            return MY_HAND_SHAPES[1]

    if opponent_hand_shape == OPPONENT_HAND_SHAPES[1]:
        if action == MY_HAND_SHAPES[0]:
            return MY_HAND_SHAPES[0]
        elif action == MY_HAND_SHAPES[1]:
            return MY_HAND_SHAPES[1]
        else:
            return MY_HAND_SHAPES[2]

    if opponent_hand_shape == OPPONENT_HAND_SHAPES[2]:
        if action == MY_HAND_SHAPES[0]:
            return MY_HAND_SHAPES[1]
        elif action == MY_HAND_SHAPES[1]:
            return MY_HAND_SHAPES[2]
        else:
            return MY_HAND_SHAPES[0]


def calculate_round_score_based_on_hand_shape(opponent_hand_shape, my_hand_shape, translate_hand_shape_to_action=False):
    if opponent_hand_shape not in OPPONENT_HAND_SHAPES or my_hand_shape not in MY_HAND_SHAPES:
        raise ValueError('invalid hand shape provided')

    if translate_hand_shape_to_action:
        action = my_hand_shape
        my_hand_shape = get_my_hand_shape(opponent_hand_shape, action)
    return get_my_hand_shape_points(my_hand_shape) + result_points(opponent_hand_shape, my_hand_shape)


def result_points(opponent_hand_shape, my_hand_shape):
    if OPPONENT_HAND_SHAPES.index(opponent_hand_shape) == MY_HAND_SHAPES.index(my_hand_shape):
        return DRAW_POINTS
    if (opponent_hand_shape == OPPONENT_HAND_SHAPES[0] and my_hand_shape == MY_HAND_SHAPES[1]) or \
            (opponent_hand_shape == OPPONENT_HAND_SHAPES[1] and my_hand_shape == MY_HAND_SHAPES[2]) or \
            (opponent_hand_shape == OPPONENT_HAND_SHAPES[2] and my_hand_shape == MY_HAND_SHAPES[0]):
        return WIN_POINTS
    return LOSE_POINTS


def total_score():
    score_based_on_hand_shape, score_based_on_action = 0, 0
    file = open("input-2day.txt", mode='r')
    line = file.readline()

    while line:
        opponent_hand_shape, my_hand_shape = line.strip().split()
        score_based_on_hand_shape += calculate_round_score_based_on_hand_shape(opponent_hand_shape, my_hand_shape)
        score_based_on_action += calculate_round_score_based_on_hand_shape(
            opponent_hand_shape, my_hand_shape, translate_hand_shape_to_action=True
        )
        line = file.readline()

    file.close()
    return score_based_on_hand_shape, score_based_on_action


if __name__ == "__main__":
    score_strategy_one, score_strategy_two = total_score()

    print(f"<<<<<--------| Strategy one score -> {score_strategy_one} | Strategy two score -> {score_strategy_two}")
