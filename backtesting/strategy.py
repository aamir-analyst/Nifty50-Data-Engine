BUY_THRESHOLD = 0.5

SELL_THRESHOLD = -0.5


def get_signal(expected_return):

    if expected_return >= BUY_THRESHOLD:
        return "BUY"

    elif expected_return <= SELL_THRESHOLD:
        return "SELL"

    else:
        return "HOLD"