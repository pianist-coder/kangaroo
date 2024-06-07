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
python3 kangaroo.py <public_key> <range> <cores>
```

- `<public_key>`: The public key you want to find the corresponding private key for.
- `<range>`: The bit range to search for the private key.
- `<cores>`: The numbers of your CPU cores

For example, to run the script with the following parameters:

```
python3 kangaroo.py 038AF9439C38F9AA692E03E789DF533C9207F57B961E30CC67E08E4521B5579FC9 40 10
```

This will search for the private key corresponding to the given public key in a key range of 39-40 bits with 10 CPU cores.

## Run
```
. . .-. . . .-. .-. .-. .-. .-.
|<  |-| |\| |.. |-| |(  | | | |
' ` ` ' ' ` `-' ` ' ' ' `-' `-'

by pianist (Telegram: @pianist_coder | btc: bc1q0jth0rjaj2vqtqgw45n39fg4qrjc37hcw4frcz)

[+] Program started
---------------------------------------------------------------------------------------
[+] Pubkey:          02A8C20AD5753A3029E19058743D109B72213C6E2CFA95AFAEB66722B44E99A5C6
[+] Key range:       2^49 (562949953421312)
[+] DP:              2^13 (8192)
[+] Expected op.:    2^25.64 (52198446)
---------------------------------------------------------------------------------------
[2048] [2^24.43] [475.95 Kkeys] [00:00:47.35] [44.60%]
-------------------------------------------------------
39c5ede67fdb1
-------------------------------------------------------
[+] Complete in 47.48 sec
```

## Donations
If you find this project useful, please consider donating to the author's Bitcoin address:

`bc1q0jth0rjaj2vqtqgw45n39fg4qrjc37hcw4frcz`
