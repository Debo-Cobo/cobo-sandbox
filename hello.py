#!/usr/bin/env python3
"""
hello.py — Cobo's first commit 🎉
Proof that the clone → edit → commit → push pipeline works.
"""


def greet(name: str = "World") -> str:
    return f"Hello, {name}! Cobo was here. 💻"


if __name__ == "__main__":
    print(greet())
    print(greet("Vincent"))
    print(greet("Debo"))
