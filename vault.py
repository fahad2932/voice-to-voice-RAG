# vault.py

from config import VAULT_PATH
import os

def insert_info(text: str):
    with open(VAULT_PATH, "a", encoding="utf-8") as f:
        f.write(text.strip() + "\n")

def read_info() -> str:
    if not os.path.exists(VAULT_PATH):
        return ""
    return open(VAULT_PATH, "r", encoding="utf-8").read()

def delete_info():
    open(VAULT_PATH, "w").close()
