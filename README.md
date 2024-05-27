# kangaroo
Find PrivateKey of corresponding Pubkey using Pollard Kangaroo algo

kahgaroo is a tool for solving private keys in the Bitcoin ecosystem. It is designed to efficiently search for private keys that correspond to a given public key.

## Usage

To use kangaroo, you'll need to have the following dependencies installed:

- `gmpy2`

You can install these dependencies using pip:

```
pip install gmpy2
```

Once the dependencies are installed, you can run the kangaroo script with the following command-line arguments:

```
python3 kangaroo.py <public_key> <range>
```

- `<public_key>`: The public key you want to find the corresponding private key for.
- `<range>`: The bit range to search for the private key.

For example, to run the script with the following parameters:

```
python3 kangaroo.py 038AF9439C38F9AA692E03E789DF533C9207F57B961E30CC67E08E4521B5579FC9 40
```

This will search for the private key corresponding to the given public key in a key range of 39-40 bits.

## Run
```
. . .-. . . .-. .-. .-. .-. .-.
|<  |-| |\| |.. |-| |(  | | | |
' ` ` ' ' ` `-' ` ' ' ' `-' `-'

by pianist (Telegram: @pianist_coder | btc: bc1q0jth0rjaj2vqtqgw45n39fg4qrjc37hcw4frcz)

[+] Program started
---------------------------------------------------------------------------------------
[+] Pubkey:          038AF9439C38F9AA692E03E789DF533C9207F57B961E30CC67E08E4521B5579FC9
[+] Key range:       39 bit
---------------------------------------------------------------------------------------
[2^18.84] [467.01 Kkeys] [00:00:01.00]
-----------------------------------------------------
94711b9219
-----------------------------------------------------
[+] Complete in 1.73 sec

. . .-. . . .-. .-. .-. .-. .-.
|<  |-| |\| |.. |-| |(  | | | |
' ` ` ' ' ` `-' ` ' ' ' `-' `-'

by pianist (Telegram: @pianist_coder | btc: bc1q0jth0rjaj2vqtqgw45n39fg4qrjc37hcw4frcz)

[+] Program started
---------------------------------------------------------------------------------------
[+] Pubkey:          038D139CECD9BEB270DD222C54CD25628D379FEEFBC39F02626168EFA39B308143
[+] Key range:       59 bit
---------------------------------------------------------------------------------------
[2^31.10] [417.83 Kkeys] [01:31:32.15]
-----------------------------------------------------
ce2018efcfc1819
-----------------------------------------------------
```

## Donations
If you find this project useful, please consider donating to the author's Bitcoin address:

`bc1q0jth0rjaj2vqtqgw45n39fg4qrjc37hcw4frcz`
