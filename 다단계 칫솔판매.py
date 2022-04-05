from collections import deque
import sys
sys.getrecursionlimit()

def bfs(start,m,gr,money):
    mm=int(m*1/10)
    money[start] += m-mm
    if m > 0:
        if start in gr.keys():
            bfs(gr[start],mm,gr,money)

def solution(enroll, referral, seller, amount):
    gr={}
    money={}
    for e,r in zip(enroll,referral):
        if r != "-":
            gr[e] = r
        money[e] = 0
    for s, a in zip(seller,amount):
        bfs(s,a*100,gr,money)
    return (list(money.values()))
