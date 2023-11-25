#!/usr/bin/python3
import sys
import math
import time

def factorize_number(n):
    fact = []
    div = 2

    while n > 1:
        if n % div == 0:
            factors.append(str(div))
            n //= div

        else:
            div += 1

    return '*'.join(factors)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 factors.py <filename>")
        return

    filen = sys.argv[1]

    try:
        with open(filen, 'r') as f:
            for l in f:
                ner = int(l.strip())
                factorization = factorize_number(ner)
                print(f"{ner}={factorization}")

    except FileNotFoundError:
        print(f"File '{filen}' not found.")
    except ValueError:
        print("Invalid format. file must contains only natural numbers.")
    except Exception as ex:
        print("An error occurred:", str(ex))


if __name__ == "__main__":
    main()
