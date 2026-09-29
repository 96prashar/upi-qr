from store import load_store, save_store # To load & save store details
from qr_gen import generate # To generate QR codes
from history import view_history # To see history
from validator import valid_vpa, valid_amount # To check if VPA and amount are valid or not

store = load_store()

while True: # Showing menu with four choices
    print("\n[1] Generate QR")
    print("[2] View history")
    print("[3] Update store (VPA/Name)")
    print("[4] Exit")
    choice = input("> ")

    if choice == "1":
        if not store: # If store details are not saved
            vpa = input("VPA: ")
            while not valid_vpa(vpa):
                print("Invalid VPA")
                vpa = input("VPA: ")
            name = input("Store name: ")
            save_store(vpa, name)
            store = [vpa, name]

        amount = input("Amount: ") # If store details are saved
        while amount and not valid_amount(amount):
            print("Invalid amount")
            amount = input("Amount: ")
        note = input("Note: ")
        ref = input("Order ID: ")
        generate(store[0], store[1], amount, note, ref) # Generating QR code

    elif choice == "2":
        show_history() # Showing history

    elif choice == "3":
        if store:
            print("Current data: " + store[0] + " | " + store[1])
        vpa = input("VPA: ")
        while not valid_vpa(vpa):
            print("Invalid VPA")
            vpa = input("VPA: ")
        name = input("Store name: ")
        save_store(vpa, name)
        store = [vpa, name]
        print("Updated data.")

    elif choice == "4":
        break # If user exits