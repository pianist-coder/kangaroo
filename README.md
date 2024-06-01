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
[+] Pubkey:          022ADBCBC6950EFF62FDE9CF4499E7AE7ADEA0A8B8D57AEF8498C0B421E7A3BD1B
[+] Key range:       2^49(562949953421312)
[+] DP:              2^12(1000)
[+] Expected op.:    2^25.59
---------------------------------------------------------------------------------------
[1024] [2^24.08] [491.15 Kkeys] [00:00:36.22] [35.20%]
-------------------------------------------------------
22c9cb9174b4f
-------------------------------------------------------
[+] Complete in 36.89 sec
```

## Donations
If you find this project useful, please consider donating to the author's Bitcoin address:

`bc1q0jth0rjaj2vqtqgw45n39fg4qrjc37hcw4frcz`
