import random

NUM_OF_ROUNDS = 67
NUM_VOTED_YES_QUESTION_ONE = 5
NUM_VOTED_YES_QUESTION_TWO = 22
NUM_VOTED_YES_QUESTION_THREE = 8
NUM_VOTED_YES_QUESTION_FOUR = 54



def players_play():
    players_money_list = [1000000] * NUM_OF_ROUNDS
    randomlistq1 = random.sample(range(0, NUM_OF_ROUNDS), NUM_VOTED_YES_QUESTION_ONE)
    randomlistq2 = random.sample(range(0, NUM_OF_ROUNDS), NUM_VOTED_YES_QUESTION_TWO)
    randomlistq3 = random.sample(range(0, NUM_OF_ROUNDS), NUM_VOTED_YES_QUESTION_THREE)
    randomlistq4 = random.sample(range(0, NUM_OF_ROUNDS), NUM_VOTED_YES_QUESTION_FOUR)

    for i in range(0, NUM_OF_ROUNDS):
        # Q1
        if i not in randomlistq1:
            flip = random.randint(0, 1)
            if flip == 1:
                players_money_list[i] += 150000
            else:
                players_money_list[i] -= 150000

        #Q2
        if i in randomlistq2:
            players_money_list[i] -= 900
        else:
            res = random.randint(1, 10)
            if res != 10:
                players_money_list[i] -= 1000
        #Q3
        if i in randomlistq3:
            flip = random.randint(0, 1)
            if flip == 1:
                players_money_list[i] += 100000
            else:
                players_money_list[i] -= 99980

        #Q4
        if i in randomlistq4:
            players_money_list[i] += 900
        else:
             res = random.randint(1, 10)
             if res != 10:
                players_money_list[i] += 1000

    print(players_money_list)
    return players_money_list


def machines_play():
    computers_money_list = [1000000] * NUM_OF_ROUNDS
    for i in range(0,NUM_OF_ROUNDS):
        #Q1 - no right answer. 50% will and 50% wont
        if int(i) % 2 == 0:
            flip = random.randint(0, 1)
            if flip == 1:
                computers_money_list[i] += 150000
            else:
                computers_money_list[i] -= 150000

        #Q2
        flip = random.randint(0, 1)
        if flip == 1:
            computers_money_list[i] -= 900
        else:
            res = random.randint(1, 10)
            if res != 10:
                computers_money_list[i] -= 1000

        #Q3
        flip = random.randint(0, 1)
        if flip == 1:
            computers_money_list[i] += 100000
        else:
            computers_money_list[i] -= 99980

        #Q4
        flip = random.randint(0, 1)
        if flip == 1:
            computers_money_list[i] += 900
        else:
            res = random.randint(1, 10)
            if res != 10:
                computers_money_list[i] += 1000

    print(computers_money_list)
    return computers_money_list


def compare_lists(machines_list, players_list):
    counter1 = 0
    counter2 = 0

    for i in range(0, len(players_list)):
        if machines_list[i] > players_list[i]:
            counter1 += 1
        elif machines_list[i] < players_list[i]:
            counter2 += 1

    print(f"machines have {counter1} wins. players have {counter2} wins.")

if __name__ == '__main__':
    r1 = machines_play()
    r2 = players_play()
    compare_lists(r1,r2)


