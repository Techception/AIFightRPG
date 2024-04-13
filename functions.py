
def status(countdown:int, p1:object, p2:object) -> None:
    print("---")
    #print(f'Start Cycle Continue: {PLAY}')
    print(f'Time: {countdown}')
    print(f'p1_health: {p1.health}')
    print(f'p2_health: {p2.health}')


def who_won(p1:object, p2:object):
    if p1.KO and p2.KO:
        print('draw game')
    elif p2.KO:
        print('Player 1 wins')
    elif p1.KO:
        print('player 2 wins')