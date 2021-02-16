def main(coins):
    coins.sort()
    currentPossibleChange = 0
    for coin in coins:
        if coin > currentPossibleChange + 1:
            return currentPossibleChange + 1
        currentPossibleChange += coin
    return currentPossibleChange + 1
