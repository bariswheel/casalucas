# Casa Lucas

Casa Lucas is a lightweight Flask web app that reads grocery prices from a simple
key-value text file and renders them as 2D charts.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Then visit `http://localhost:5000` in your browser.

## Data format

Edit `data/items.txt` using `Item Name: price` per line, for example:

```
Apples: 1.49
```
