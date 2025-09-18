
# Travel Express 🚀

A simple, console-based Python mini-project for booking travel tickets (bus, train, or flight) with an automated e-ticket sent to WhatsApp.

## Features ✨

  * **User Authentication**: A basic login system where users can set up and use a username and password.
  * **Ticket Booking**: Choose from three travel types (Bus, Train, or Flight).
  * **Dynamic Pricing**: Ticket prices are randomly generated for each booking.
  * **Seat Assignment**: Randomly assigns seat numbers based on the number of tickets booked.
  * **Coupon System**: Users can apply a coupon code for a discount on their total bill.
  * **Automated WhatsApp Bill**: Automatically sends an e-ticket containing all booking details to the user's WhatsApp number using the `pywhatkit` library.
  * **Payment Options**: Offers two payment methods: GPay (simulated) and Cash on Delivery.
  * **Image Display**: Uses the `pygame` library to display a relevant image (bus, train, or flight) during the booking process.

-----

## How to Run 🏃

### Prerequisites

You'll need to have Python installed on your system. This project also requires several Python libraries. You can install them by running the following command in your terminal:

```bash
pip install pygame pywhatkit pyautogui
```

### Execution

1.  Make sure you have the required images (`bus.jpg`, `train.jpg`, `flight.jpg`) in the specified path or update the path in the code.
2.  Run the Python script from your terminal:

<!-- end list -->

```bash
python your_project_name.py
```

3.  Follow the on-screen prompts to log in and book your ticket.

-----

## Code Structure 🏗️

The code is organized into several functions for clarity and modularity:

  * `login()`: Handles user registration and login.
  * `im_p(image)`: Displays an image using `pygame`.
  * `apply_coupon(total)`: Applies a discount based on a coupon code.
  * `payment(...)`: Manages the payment process and triggers the WhatsApp bill sending.
  * `book_ticket(name)`: The main booking logic, including travel type selection and seat calculation.
  * `main()`: The primary function that orchestrates the flow of the program.

-----

## Notes 📝

  * **WhatsApp Functionality**: For the WhatsApp message to be sent, your system must have WhatsApp Web logged in. The `pywhatkit` and `pyautogui` libraries work together to automate this process.
  * **Path Dependency**: The image paths (`C:\\Users\\Admin\\Desktop\\...`) are hardcoded. You should change these paths to where you store your images.
  * **Security**: The login system is very basic and not secure. It's intended for a mini-project and does not hash passwords or use a database.

-----

## Possible Improvements 💡

  * **Improved UI**: Replace the console-based interface with a graphical user interface (GUI) using a library like Tkinter, PyQt, or Kivy.
  * **Database Integration**: Store user data and booking information in a database (e.g., SQLite, PostgreSQL) for persistent storage.
  * **Real-time Availability**: Implement a system to track available seats and prevent overbooking.
  * **SMS/Email Integration**: Instead of just WhatsApp, send the e-ticket via SMS or email for more options.
  * **Error Handling**: Add more robust error handling for user inputs to prevent crashes.

Enjoy your travel bookings\! ✈️
