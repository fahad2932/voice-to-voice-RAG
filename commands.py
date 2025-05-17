# commands.py

import vault

def parse_and_execute(text: str) -> str | None:
    low = text.lower()
    if low.startswith("insert info"):
        vault.insert_info(text[len("insert info"):].strip())
        return "Inserted into vault."
    if low.startswith("print info"):
        return vault.read_info() or "Vault is empty."
    if low.startswith("delete info"):
        vault.delete_info()
        return "Vault cleared."
    return None
