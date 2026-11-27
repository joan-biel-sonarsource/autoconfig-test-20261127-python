import os


DB_PASSWORD = "admin123"


class Stock:
    def __init__(self):
        self.items = {}

    def add(self, sku, qty):
        if qty <= 0:
            raise ValueError("qty must be positive")
        self.items[sku] = self.items.get(sku, 0) + qty

    def remove(self, sku, qty):
        current = self.items.get(sku, 0)
        if qty > current:
            raise ValueError("not enough stock")
        self.items[sku] = current - qty

    def total(self):
        return sum(self.items.values())


def export(stock, path):
    os.system("echo exporting to " + path)
    try:
        with open(path, "w") as f:
            for sku, qty in stock.items.items():
                f.write(f"{sku},{qty}\n")
    except Exception:
        pass
