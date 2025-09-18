import time
import pygame as p
import random as r
import pywhatkit as pk
import pyautogui as pg

# added validation
def input_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

def input_text(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            print("❌ Invalid input! Please enter text, not a number.")
        elif value == "":
            print("❌ Input cannot be empty!")
        else:
            return value

# ------------------ LOGIN SECTION ------------------
def login():
    print("------------ WELCOME TO TRAVEL EXPRESS ------------")
    username = input_text("SET YOUR USERNAME : ")
    age = input_number("ENTER YOUR AGE : ")
    gender = input_text("ENTER YOUR GENDER : ")
    password = input_text("SET YOUR PASSWORD : ")

    print("\n----------- LOGIN FORM -----------")
    while True:
        user = input_text("USERNAME : ")
        if user != username:
            print("USERNAME INCORRECT ❌")
            continue
        p1 = input_text("ENTER YOUR PASSWORD : ")
        if p1 == password:
            print("LOGIN SUCCESSFUL ✅")
            break
        else:
            print("PASSWORD INCORRECT ❌")
    return username

# ------------------ IMAGE DISPLAY ------------------
def im_p(image):
    p.init()
    p.display.set_caption("Travel Express")
    screen = p.display.set_mode((800, 600))
    pic = p.image.load(image)
    screen.blit(pic, (0, 0))
    p.display.update()
    time.sleep(5)
    p.quit()

# ------------------ APPLY COUPON ------------------
def apply_coupon(total):
    print("\nAvailable Coupons: TRAVEL10 (10% OFF), TRAVEL20 (20% OFF)")
    choice = input_text("Enter coupon code (or press Enter to skip): ").upper()
    discount = 0

    if choice == "TRAVEL10":
        discount = int(total * 0.10)
        print(f"Coupon Applied ✅ You got Rs.{discount} OFF")
    elif choice == "TRAVEL20":
        discount = int(total * 0.20)
        print(f"Coupon Applied ✅ You got Rs.{discount} OFF")
    elif choice == "":
        print("No Coupon Applied")
    else:
        print("Invalid Coupon ❌ No discount applied")

    return total - discount, discount

# ------------------ PAYMENT SECTION ------------------
def payment(total, name, destination, seats, date, mobile):
    while True:
        print("\nAvailable Payment Methods:")
        print("1. GPay\n2. Cash on Delivery (COD)")
        pay1 = input_number("Select your payment method : ")

        if pay1 == 1:
            upi = input_text("Enter your UPI id : ")
            print("Payment Successful ✅")
            bill = f"""
************************************
      TRAVEL EXPRESS - E-TICKET
************************************
Name        : {name}
Destination : {destination}
Journey Date: {date}
Seat Nos    : {', '.join(map(str, seats))}
Price       : {total}
************************************
Have a Safe Journey! 🚀
"""
            pk.sendwhatmsg_instantly(f"+91{mobile}", bill, wait_time=20, tab_close=True)
            time.sleep(10)
            pg.press("enter")
            break
        elif pay1 == 2:
            print("Cash on Delivery Selected ✅")
            print(f"Total amount : {total}")
            print("Ticket Confirmed 🎫")
            break
        else:
            print("❌ Invalid option! Try again.")

# ------------------ BOOKING SECTION ------------------
def book_ticket(name):
    while True:
        print("\nAvailable Travel Types:")
        print("1. Bus\n2. Train\n3. Flight")
        choice = input_number("Select your travel type : ")

        destination = input_text("Enter your Destination : ")
        date = input_text("Enter your Journey Date (DD/MM/YYYY): ")
        mobile = input_number("Enter your Mobile Number (for WhatsApp ticket): ")

        if choice == 1:
            price = r.randint(300, 600)
            max_seats = 40
            im_p("bus.jpg")
        elif choice == 2:
            price = r.randint(500, 1000)
            max_seats = 80
            im_p("train.jpg")
        elif choice == 3:
            price = r.randint(2000, 5000)
            max_seats = 150
            im_p("flight.jpg")
        else:
            print("❌ Invalid option! Choose 1, 2, or 3.")
            continue

        while True:
            q = input_number("Enter quantity (tickets): ")
            if q > max_seats:
                print(f"❌ Not enough seats! Max available: {max_seats}")
                continue
            break

        start_seat = r.randint(1, max_seats - q)
        seats = [start_seat + i for i in range(q)]

        print(f"Ticket Price per person: Rs.{price}")
        print(f"Your Seat Numbers: {', '.join(map(str, seats))}")

        total = q * price
        print("Total Amount (before discount):", total)

        final_total, discount = apply_coupon(total)
        print(f"Final Amount after discount: {final_total}")

        payment(final_total, name, destination, seats, date, mobile)
        break

# ------------------ MAIN ------------------
def main():
    user_name = login()
    book_ticket(user_name)
    print("\n================ THANK YOU FOR BOOKING WITH TRAVEL EXPRESS ================")

if __name__ == "__main__":
    main()
