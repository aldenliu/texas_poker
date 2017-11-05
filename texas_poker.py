import numpy as np
import time
empty_array = np.array([])

UNKNOWN = 0
HIGH_CARD = 1
ONE_PAIR = 2
TWO_PAIR = 3
SET = 4 #done
FLUSH = 5
SAME_COLOR = 6 #done
HULU = 7 #done
SITIAO = 8 # done

def shuffle_poker():
    np.random.shuffle(poker)
    return poker

def get_same_color(poker):
    colors = np.floor_divide(poker, 13)
    color_cnt = np.bincount(colors)
    max_field = np.argmax(color_cnt)
    if color_cnt[max_field] >= 5:
        cond = colors == max_field
        return np.sort(np.extract(cond, poker))[0:5] % 13
    else:
        return empty_array

def get_sitiao(numbers, number_cnt):
    fours = np.where(number_cnt == 4)
    if len(fours[0]) > 0:
        max_type = SITIAO
        four_number = fours[0][0]
        if four_number != numbers[-1]:
            best_numbers = np.array([four_number] * 4 + [numbers[-1]])
            return best_numbers
        else:
            best_numbers = np.array([four_number] * 4 + [numbers[-5]])
            return best_numbers
    return empty_array

def get_hulu(number_cnt):
    threes = np.where(number_cnt == 3)
    if len(threes[0]) == 2:
        max_three = threes[0][1]
        low_pair = threes[0][0]
        best_number = [max_three] * 3 + [low_pair] * 2
        return np.array(best_number)
    if len(threes[0]) == 1:
        three = threes[0][0]
        twos = np.where(number_cnt == 2)
        if len(twos[0]) == 0:
            return empty_array
        high_two = twos[0][-1]
        best_numbers = [three] * 3 + [high_two] * 2
        return np.array(best_numbers)
    return empty_array

def get_three(number_cnt):
    threes = np.where(number_cnt == 3)
    if len(threes[0]) == 1:
        three = threes[0][0]
        ones = np.where(number_cnt == 1)[0]
        ones[::-1].sort()
        high_two = ones[0:2]
        best_number = np.append(np.array([three] * 3), high_two)
        return best_number
    return empty_array

def get_pairs(number_cnt):
    twos = np.where(number_cnt == 2)
    if len(twos[0]) == 0:
        return empty_array
    if len(twos[0]) == 1:
        two = twos[0][0]
        ones = np.where(number_cnt == 1)[0]
        ones[::-1].sort()
        high_ones = ones[0:3]
        best_number = np.append(np.array([two] * 2), high_ones)
        return best_number
    twos[0][::-1].sort()
    if len(twos[0]) == 2:
        high_two = twos[0][0]
        low_two = twos[0][1]
        high_one = np.where(number_cnt == 1)[0].max()
        best_number = [high_two] * 2 + [low_two] * 2 + [high_one]
        return np.array(best_number)
    if len(twos[0]) == 3:
        high_two = twos[0][0]
        middle_two = twos[0][1]
        low_two = twos[0][2]
        one = np.where(number_cnt == 1)[0][0]
        high_one = max(low_two, one)
        best_number = [high_two] * 2 + [middle_two]* 2 + [high_one]
        return np.array(best_number)
    return empty_array

def get_flush(poker_number):
    numbers = np.unique(poker_number)
    start = 0
    end = len(numbers) - 1
    cur = end
    while end - cur != 4 and cur >= 0:
        if numbers[cur] == numbers[cur - 1] + 1:
            cur -= 1
        else:
            end = cur - 1
            cur -= 1
    if end - cur == 4:
        best_number = numbers[end:cur-1:-1]
        return np.array(best_number)
    return empty_array

    
def get_max_number(poker):
    number_type = UNKNOWN
    max_numbers = empty_array
    numbers = np.sort(np.mod(poker, 13))
    number_cnt = np.bincount(numbers)
    sitiao = get_sitiao(numbers, number_cnt)
    if len(sitiao) > 0:
        return (SITIAO, sitiao)
    hulu = get_hulu(number_cnt)
    if len(hulu) > 0:
        return (HULU, hulu)
    flush = get_flush(numbers)
    if len(flush) > 0:
        return(FLUSH, flush)
    three = get_three(number_cnt)
    if len(three) > 0:
        return (SET, three)
    pairs = get_pairs(number_cnt)
    if len(pairs) > 0:
        if len(pairs) < 3:
            print(poker)
            print(number_cnt)
            print(pairs)
        if pairs[2] == pairs[3]:
            return (TWO_PAIR, pairs)
        return (ONE_PAIR, pairs)
    high_five = numbers[2:]  
    print(numbers)
    return (HIGH_CARD, high_five[::-1])

def compare_poker(suite_a, suite_b):
    (type_a, field_a) = suite_a
    (type_b, field_b) = suite_b
    if type_a > type_b:
        return 1
    if type_a < type_b:
        return -1
    for i in range(0,5):
        if field_a[i] != field_b[i]:
            return 1 if field_a[i] > field_b[i] else -1
    return 0

def main():
    start = time.time()
    for i in range(0,1000000):
        shuffled_poker = shuffle_poker()
        selected = shuffled_poker[0:7]
        data = get_max_number(selected)
        if len(data) > 0 and data[0] == HIGH_CARD:
            print(data, selected)
    end = time.time()
    print('time cost {0}'.format(end - start))

def main1():
    a = (FLUSH, np.array([12,5,5,5,12]))
    b = (SITIAO, np.array([10,9,8,7,6]))
    print(compare_poker(a,b))

if __name__ == '__main__':
    main1()
