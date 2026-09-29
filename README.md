# UPI QR Generator

CLI tool to generate UPI QR codes and keep track of payment history.

## Features
- Generate UPI QR codes (terminal output)
- Store name & UPI ID is saved and can be changed
- Payment history saved using CSV file

## Setup

```bash
pip install qrcode

```

## Usage

```bash
python main.py
```
To run on linux
```bash
python3 main.py
```

Menu:
```
[1] Generate QR
[2] View history
[3] Update store (VPA + name)
[4] Exit
```

## Files

| File | Purpose |
|------|---------|
| `main.py` | Main file |
| `store.py` | Load/save store VPA & name |
| `qr_gen.py` | Build UPI URL & display QR |
| `history.py` | Read payment history from CSV |
| `validators.py` | VPA & Amount validation |

## Data

| File | Description |
|------|-------------|
| `store.txt` | `vpa\|store_name` |
| `payments.csv` | time, vpa, name, amount, note, ref |

## Author
Parth Prashar