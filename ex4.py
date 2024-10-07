def solve(price: float) -> list[int]:
    cents = int(price * 100)
    coins = [100, 50, 20, 10, 5, 2, 1]
    result = []

    for coin in coins:
        count = cents // coin
        if count > 0:
            if coin == 100:
                result.append(f'{count} x {int(coin/100)} euro')
            else:
                result.append(f'{count} x {coin} cents')
        cents -= count * coin

    return result