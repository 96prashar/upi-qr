import qrcode
import csv
import os
import datetime # To get current time
from history import HISTORY

def generate(vpa, name, amount, note, ref):
    safe_name = name.replace(" ", "%20") # In URL spaces are %20
    url = "upi://pay?pa=" + vpa + "&pn=" + safe_name
    if amount:
        url += "&am=" + amount + "&cu=INR"
    if note:
        url += "&tn=" + note.replace(" ", "%20")
    if ref:
        url += "&tr=" + ref.replace(" ", "%20")

    qr = qrcode.QRCode() # Creating the QR
    qr.add_data(url)
    qr.make()
    qr.print_ascii()

    row = [datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), vpa, name, amount, note, ref]
    write_header = not os.path.exists(HISTORY)
    
    with open(HISTORY, "a", newline="", encoding="utf-8") as f: # Appending history
        w = csv.writer(f)
        if write_header:
            w.writerow(["time", "vpa", "name", "amount", "note", "ref"])
        w.writerow(row)