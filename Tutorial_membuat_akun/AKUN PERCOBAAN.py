accounts = {
    "alpha": "5122", "beta": "2531", "charlie": "1245"
}

login_status = False

def login(username, pin):
    if username.lower() in accounts:
        if accounts[username.lower()] == pin:
            print(f"Selamat datang {username}")
            return True
        else:
            print("Pin tidak sesuai")
    else:
        print(f"User {username} tidak dikenali")
    return False

def is_pin_valid(pin):
    if not(len(pin) == 4 and pin.isdigit()):
        print("Pin harus terdiri dari 4 digit angka")
        return False
    return True

def display_accounts():
    censored_values = (map(lambda x: x.replace("1", "*").replace("2", "*").replace("3", "*"), accounts.values()))
    censored_accounts = dict(zip(accounts.keys(), censored_values))
    for i, (name, password) in enumerate(censored_accounts.items()):
        print(f"{i+1}. {name}: {password}")

while True:
    username = input("Masukkan username: ")
    pwd = input("Masukkan 4 digit pin: ")
    if is_pin_valid(pwd):
        login_status = login(username, pwd)
        if login_status:
            display_accounts()
            break 
    