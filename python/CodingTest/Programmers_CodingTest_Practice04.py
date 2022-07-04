# [문제] Lv.1 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301


# 제출 답안
def solution(s):
    number = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    find =[]

    for key in number.keys():
        if key in s:
            find.append(key)

    for x in find:
        s = s.replace(x, number[x])
    return int(s)


# 풀이 과정
import pandas as pd
import numpy as np

number = {'zero':'0',
'one':'1',
'two':'2',
'three':'3',
'four':'4',
'five':'5',
'six':'6',
'seven':'7',
'eight':'8',
'nine':'9'}

for key in number.keys():
    print(key)
    print(number[key])

s = "one4seveneight"
find =[]

for key in number.keys():
    #s에 있는 key 만 우선 프린트
    if key in s:
        find.append(key)
print(find)

for x in find:
    s = s.replace(x, number[x])
print(s)


# 다른사람의 풀이
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
