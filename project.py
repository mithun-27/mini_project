import time
import pygame as p
import random as r
import pywhatkit as pk
import pyautogui as pg

# ------------------ LOGIN SECTION ------------------
def login():
    print("------------ WELCOME TO TRAVEL EXPRESS ------------")
    name = input("ENTER YOUR NAME : ")
    age = int(input("ENTER YOUR AGE : "))
    gender = input("ENTER YOUR GENDER : ")
    password = input("SET YOUR PASSWORD : ")

    print("\n----------- LOGIN FORM -----------")
    def check_login():
        user = input("USERNAME : ")
        if user == name:
            p1 = input("ENTER YOUR PASSWORD : ")
            if p1 == password:
                print("LOGIN SUCCESSFUL ✅")
            else:
                print("PASSWORD INCORRECT ❌")
                check_login()
        else:
            print("USERNAME INCORRECT ❌")
            check_login()

    check_login()
    return name

# ------------------ IMAGE DISPLAY ------------------
def im_p(image):
    p.init()
    p.display.set_caption("Travel Express")
    screen = p.display.set_mode((3000, 2000))
    pic = p.image.load(image)
    screen.blit(pic, (10, 10))
    p.display.update()
    time.sleep(5)
    p.quit()

# ------------------ APPLY COUPON ------------------
def apply_coupon(total):
    print("\nAvailable Coupons: TRAVEL10 (10% OFF), TRAVEL20 (20% OFF)")
    choice = input("Enter coupon code (or press Enter to skip): ").strip().upper()
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
    print("\nAvailable Payment Methods:")
    print("1. GPay\n2. Cash on Delivery (COD)")
    pay1 = int(input("Select your payment method : "))

    if pay1 == 1:
        upi = input("Enter your UPI id : ")
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

    elif pay1 == 2:
        print("Cash on Delivery Selected")
        print("Please pay at the counter. ✅")
        print("Total amount :", total)
        print("Ticket Confirmed 🎫")
    else:
        print("Invalid Payment Method ❌")
        payment(total, name, destination, seats, date, mobile)

# ------------------ BOOKING SECTION ------------------
def book_ticket(name):
    print("\nAvailable Travel Types:")
    print("1. Bus\n2. Train\n3. Flight")
    choice = int(input("Select your travel type : "))

    destination = input("Enter your Destination : ")
    date = input("Enter your Journey Date (DD/MM/YYYY): ")
    mobile = input("Enter your Mobile Number (for WhatsApp ticket): ")

    if choice == 1:
        price = r.randint(300, 600)
        max_seats = 40
        im_p("C:\\Users\\Admin\\Desktop\\pythonProject\\.venv\\Scripts\\bus.jpg")

    elif choice == 2:
        price = r.randint(500, 1000)
        max_seats = 80
        im_p("C:\\Users\\Admin\\Desktop\\pythonProject\\.venv\\Scripts\\train.jpg")

    elif choice == 3:
        price = r.randint(2000, 5000)
        max_seats = 150
        im_p("C:\\Users\\Admin\\Desktop\\pythonProject\\.venv\\Scripts\\flight.jpg")

    else:
        print("Invalid Option ❌")
        return book_ticket(name)

    q = int(input("Enter quantity (tickets): "))
    if q > max_seats:
        print("Not enough seats available ❌")
        return book_ticket(name)


    start_seat = r.randint(1, max_seats - q)
    seats = [start_seat + i for i in range(q)]

    print(f"Ticket Price per person: Rs.{price}")
    print(f"Your Seat Numbers: {', '.join(map(str, seats))}")

    total = q * price
    print("Total Amount (before discount):", total)


    final_total, discount = apply_coupon(total)
    print(f"Final Amount after discount: {final_total}")


    payment(final_total, name, destination, seats, date, mobile)

# ------------------ MAIN ------------------
def main():
    user_name = login()
    book_ticket(user_name)
    print("\n================ THANK YOU FOR BOOKING WITH TRAVEL EXPRESS ================")

main()
