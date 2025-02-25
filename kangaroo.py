#-------------------------------------------------------------------------
# Name:        kangaroo
# Author:      pianist (Telegram: @pianist_coder)
# Credit:      iceland
# Created:     24.05.2024
# Copyright:   (c) pianist 2022-2024
#-------------------------------------------------------------------------

import time
import random
import sys
import os
from gmpy2 import mpz, powmod, invert
from math import log2, sqrt, log
from collections import defaultdict

sp = """
-------------------------------------------------------
{0:x}
-------------------------------------------------------"""
splash = """
. . .-. . . .-. .-. .-. .-. .-. 
|<  |-| |\| |.. |-| |(  | | | | 
' ` ` ' ' ` `-' ` ' ' ' `-' `-' 
"""
#=========================================================================
class color:
    GREEN = "\033[32m"
    RED = "\033[31m"
    X = "\033[5m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"
#=========================================================================

k, rng = sys.argv[1:]
rng = int(rng)

Gx, Gy = (mpz(55066263022277343669578718895168534326250603453777594175500187360389116729240),
          mpz(32670510020758816978083085130507043184471273380659243275938904335757337482424))
modulo =  mpz(115792089237316195423570985008687907853269984665640564039457584007908834671663)
PG = (Gx, Gy)

#=========================================================================

def printc(colors, message):
    print(colors + message + color.END)

def to_cpub(pub_hex):
    P = pub_hex
    if len(pub_hex) > 70:
        P = '02' + pub_hex[2:66] if int(pub_hex[66:], 16) % 2 == 0 else '03' + pub_hex[2:66]
    return P

def X2Y(X, parity):
    Y2 = (X * X * X + 7) % modulo
    Y = powmod(Y2, (modulo + 1) // 4, modulo)
    return (X, -Y % modulo if parity else Y)

def p_2(num):
    return f'{log2(num):.2f}'

def pr():
    os.system("cls||clear")
    printc(color.GREEN, splash)
    printc(color.RED, "by pianist (Telegram: @pianist_coder | btc: bc1q0jth0rjaj2vqtqgw45n39fg4qrjc37hcw4frcz)")
    printc(color.BOLD, "\n[+] Program started")
    print("-"*87)
    print(f"[+] Pubkey:          {pub.upper()}")
    print(f"[+] Key range:       2^{rng-1}({2**(rng - 1)})")
    print(f"[+] DP:              2^{int(log2(DP_rarity))}({DP_rarity:x})")
    print(f"[+] Expected op.:    2^{p_2(2.13 * sqrt(1 << (rng-1)))}")    
    print("-"*87)

def speedup_prob(st, counter, Nt):
    elapsed_time = time.time() - start
    speed = counter / elapsed_time
    prob = float(counter / (2.13 * sqrt(1 << (rng-1))) * 100)
    print(f"[{Nt}] [2^{p_2(counter)}] [{scan_str(speed)}keys] [{display_time(elapsed_time)}] [{prob:.2f}%]   ", end="\r")

def scan_str(num):
    suffixes = ["", "K", "M", "B", "T"]
    exponent = 0
    while abs(num) >= 1000 and exponent < 4:
        num /= 1000
        exponent += 1
    return f"{num:.2f} {suffixes[exponent]}"

def display_time(seconds):
    hours, rem = divmod(seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{int(hours):02d}:{int(minutes):02d}:{seconds:05.2f}"

#speedup this please

def add(P, Q):
    Z = (0, 0)
    if P == Z:
        return Q
    if Q == Z:
        return P
    
    Px, Py = P
    Qx, Qy = Q

    if Px == Qx:
        if Py == Qy:
            # Use double formula
            inv_2Py = invert((Py << 1) % modulo, modulo)
            m = (3 * Px * Px * inv_2Py) % modulo
        else:
            return Z
    else:
        inv_diff_x = invert(Qx - Px, modulo)
        m = ((Qy - Py) * inv_diff_x) % modulo

    x = (m * m - Px - Qx) % modulo
    y = (m * (Px - x) - Py) % modulo
    
    return (x, y)

def mul(k, P=PG):
    R = (0, 0)
    while k:
        if k & 1:
            R = add(R, P)
        P = add(P, P)
        k >>= 1
    return R

def kangs(lower, upper, size):
    odd_numbers = set()
    while len(odd_numbers) < size:
        number = random.SystemRandom().randint(lower, upper)
        #if number % 2 == 1:
        odd_numbers.add(number)
    return list(odd_numbers)

def check(P, k, DP_rarity, A_dict, B_dict):
    if not P[0] % DP_rarity:
        if P[0] in B_dict:
            kA = k
            kB = B_dict[P[0]]
            print(sp.format(abs(kA - kB)))
            printc(color.BOLD, f"[+] Complete in {time.time() - start:.2f} sec")
            with open('FOUND.txt', 'a') as f:
                f.write(f'{pub.lower()};{abs(kA - kB):x}\n')
            return True
        A_dict[P[0]] = k
    return False

def search(P, W0, DP_rarity, Nw, Nt, hop_modulo, upper, lower):
    t = kangs(lower, upper, Nt)
    T = [mul(ti) for ti in t]
    w = kangs(0, upper, Nw)
    W = [add(W0, mul(wi)) for wi in w]
    
    T_dict = defaultdict(int)
    W_dict = defaultdict(int)
    
    jumps, t0 = 0, time.time()
    while True:
        for k in range(Nt):
            jumps += 1
            pw = T[k][0] % hop_modulo
            if check(T[k], t[k], DP_rarity, T_dict, W_dict):
                return
            t[k] += 1 << pw
            T[k] = add(P[pw], T[k])
        for k in range(Nw):
            jumps += 1
            pw = W[k][0] % hop_modulo
            if check(W[k], w[k], DP_rarity, W_dict, T_dict):
                return
            w[k] += 1 << pw
            W[k] = add(P[pw], W[k])
        t1 = time.time()
        if t1 - t0 > 1:
            speedup_prob(start, jumps, Nt)
            t0 = t1

#optimal params
KANG = rng // 5
lower = 2 ** (rng - 1)
upper = 2 ** rng - 1
DP_rarity = 1 << ((rng - 1) // 2 - 2) // 2 + 2
hop_modulo = round(log(2**rng)+5)

Nt = Nw = 1 << KANG

pub = to_cpub(k)
X = int(pub[2:], 16)
Y = X2Y(X, pub[:2] == '03')[1]
W0 = (mpz(X), mpz(Y))
P = [PG]
for _ in range(KANG ** 2):
    P.append(add(P[-1], P[-1]))

pr()
start = time.time()
search(P, W0, DP_rarity, Nw, Nt, hop_modulo, upper, lower)
