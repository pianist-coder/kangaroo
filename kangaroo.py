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
from math import log2

sp = """
-----------------------------------------------------
{0:x}
-----------------------------------------------------"""
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
Z = (0, 0)

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
    print(f"[+] Key range:       {rng - 1} bit")
    print("-"*87)

def speedup_prob(st, counter):
    elapsed_time = time.time() - start
    speed = counter / elapsed_time
    print(f"[2^{p_2(counter)}] [{scan_str(speed)}keys] [{display_time(elapsed_time)}]    ", end="\r")

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

def add(P, Q):
    if P == Z:
        return Q
    if Q == Z:
        return P
    if P[0] == Q[0]:
        if P[1] == Q[1]:
            inv_2P1 = invert(2 * P[1], modulo)
            m = (3 * P[0] * P[0] * inv_2P1) % modulo
        else:
            return Z
    else:
        m = ((Q[1] - P[1]) * invert(Q[0] - P[0], modulo)) % modulo
    x = (m * m - P[0] - Q[0]) % modulo
    y = (m * (P[0] - x) - P[1]) % modulo
    return (x, y)

def mul(k, P=PG):
    R = Z
    Q = P
    while k:
        if k & 1:
            R = add(R, Q)
        Q = add(Q, Q)
        k >>= 1
    return R

def check(P, k, DP_rarity, A, Ak, B, Bk):
    if not P[0] % DP_rarity:
        A.append(P[0])
        Ak.append(k)
        if set(A) & set(B):
            kA = Ak[A.index(next(iter(set(A) & set(B))))]
            kB = Bk[B.index(next(iter(set(A) & set(B))))]
            print(sp.format(abs(kA-kB)))
            printc(color.BOLD, f"[+] Complete in {time.time() - start:.2f} sec")
            return True
    return False

def search(P, W0, DP_rarity, Nw, Nt, hop_modulo, upper, lower):
    t = [lower + random.randint(0, upper - lower) for _ in range(Nt)]
    T = [mul(ti) for ti in t]
    dt = [0] * Nt
    w = [random.randint(0, upper - lower) for _ in range(Nw)]
    W = [add(W0, mul(wi)) for wi in w]
    dw = [0] * Nw
    memo = {i: 1 << i for i in range(hop_modulo)}
    jumps, jumps_old, t0 = 0, 0, time.time()
    while True:
        for k in range(Nt):
            jumps += 1
            pw = T[k][0] % hop_modulo
            dt[k] = memo[pw]
            if check(T[k], t[k], DP_rarity, T, t, W, w):
                return
            t[k] += dt[k]
            T[k] = add(P[pw], T[k])
        for k in range(Nw):
            jumps += 1
            pw = W[k][0] % hop_modulo
            dw[k] = memo[pw]
            if check(W[k], w[k], DP_rarity, W, w, T, t):
                return
            w[k] += dw[k]
            W[k] = add(P[pw], W[k])
        t1 = time.time()
        if t1 - t0 > 1:
            speedup_prob(start, jumps)
            t0, jumps_old = t1, jumps


compressed = k
puzzle = rng
kangaroo_power = 4
lower = 2 ** (puzzle - 1)
upper = 2 ** puzzle - 1
DP_rarity = 1 << ((puzzle - 2 * kangaroo_power) // 2 - 2)
hop_modulo = (puzzle - 1) // 2 + kangaroo_power
Nt = Nw = 2 ** kangaroo_power
pub = to_cpub(compressed)
X = int(pub[2:], 16)
Y = X2Y(X, pub[:2] == '03')[1]
W0 = (X, Y)

P = [PG]
for _ in range(255):
    P.append(add(P[-1], P[-1]))

pr()
start = time.time()
search(P, W0, DP_rarity, Nw, Nt, hop_modulo, upper, lower)