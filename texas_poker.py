import numpy as np
import time
poker = np.array(range(0,54))
empty_array = np.array([])

UNKNOWN = 0
HIGH_CARD = 1
ONE_PAIR = 2
TWO_PAIR = 3
SET = 4
FLUSH = 5
SAME_COLOR = 6
HULU = 7
SITIAO = 8

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

def get_max_number(poker):
    numbers = np.sort(np.mod(poker, 13))
    number_cnt = np.bincount(numbers)
    fours = np.where(number_cnt == 4)
    if len(fours) > 0:
        four_number = fours[0]
        

def get_type_with_param(poker):
    max_poker = empty_array
    max_type = UNKNOWN
    k = get_same_color(poker)
    if len(k) > 0:
        max_poker = k
        max_type = SAME_COLOR
        
    numbers = poker % 13
    return -1
    
def compare_poker(poker1, poker2):
    type1 = p

def main():
    start = time.time()
    for i in range(0,10000):
        shuffled_poker = shuffle_poker()
        selected = shuffled_poker[0:7]
        same_color = get_same_color(selected)
        if len(same_color) > 0:
            print(same_color, selected)
    end = time.time()
    print('time cost {0}'.format(end - start))

if __name__ == '__main__':
    main()

