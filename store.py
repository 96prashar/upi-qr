import os # To check if store.txt exists or not

STORE = "store.txt"

def load_store(): # Reading store data
    if os.path.exists(STORE):
        with open(STORE) as f: # Using with so no need to close file
            content = f.read().strip()
            if "|" in content:
                return content.split("|")
    return None

def save_store(vpa, name): # Writing store data
    with open(STORE, "w") as f:
        f.write(vpa + "|" + name)