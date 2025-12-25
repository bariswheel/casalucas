from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List

from flask import Flask, jsonify, render_template

DATA_FILE = Path("data/items.txt")

app = Flask(__name__)


@dataclass(frozen=True)
class ItemPrice:
    name: str
    price: float


def load_items(path: Path) -> List[ItemPrice]:
    items: List[ItemPrice] = []
    if not path.exists():
        return items

    for line in path.read_text(encoding="utf-8").splitlines():
        raw = line.strip()
        if not raw or raw.startswith("#"):
            continue
        if ":" not in raw:
            continue
        name, price_text = raw.split(":", 1)
        name = name.strip()
        try:
            price = float(price_text.strip())
        except ValueError:
            continue
        items.append(ItemPrice(name=name, price=price))
    return items


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/items")
def api_items():
    items = load_items(DATA_FILE)
    return jsonify(
        {
            "items": [
                {
                    "name": item.name,
                    "price": item.price,
                }
                for item in items
            ]
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
