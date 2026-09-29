# Validator file checks validity of VPA & Amount
def valid_vpa(vpa):
    if "@" not in vpa:
        return False
    parts = vpa.split("@")
    return len(parts) == 2 and len(parts[0]) > 0 and len(parts[1]) > 0

def valid_amount(amount):
    try:
        float(amount)
        return True
    except ValueError:
        return False