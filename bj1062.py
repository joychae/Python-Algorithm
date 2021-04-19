# 가르침 (브루트포스 연습)

import sys
from collections import Counter

N, K = map(int,sys.stdin.readline().strip().split())
words = [list(sys.stdin.readline().strip()) for _ in range(N)]
real_words = []

if K < 5:
    print(0)

elif K > 5:
    for word in words:
        real_words.extend(word[4:-4])

    real_words_cnt = Counter(real_words)
    real_words_cnt_keys = list(real_words_cnt.keys())
    learned = ['a', 'n', 't', 'c', 'i']
    learned.extend(real_words_cnt_keys[:K-5])
    print(real_words_cnt)
    print(real_words_cnt_keys)
    print(learned)
        
