# User Authentication System with Python and MySQL

This project is a simple graphical user interface (GUI) application for user authentication, created using Python's Tkinter library. The application allows users to sign up, log in, and reset their passwords. The user data is stored in a MySQL database.

## Features

- **Sign Up:** New users can create an account by providing their email, username, and password. Password confirmation and acceptance of terms and conditions are required.
- **Login:** Existing users can log in with their username and password.
- **Password Reset:** Users can reset their password if they forget it by providing their username and new password.

## Screenshots

### Sign Up Page
![Sign Up Page](User_Authentication_System/Python 3.12 28-07-2024 19_59_32.png)

### Login Page
![Login Page](./mnt/data/Python%203.12%2028-07-2024%2019_59_48.png)

## Requirements

- Python 3.x
- Tkinter
- PIL (Pillow)
- pymysql

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repository
   ```
3. Install the required packages:
   ```bash
   pip install pymysql pillow
   ```

## Usage

1. **Setting up MySQL Database:**
   - Make sure you have MySQL installed and running.
   - Create a database named `userdata`:
     ```sql
     CREATE DATABASE userdata;
     ```
   - Create a table named `data` within the `userdata` database:
     ```sql
     USE userdata;
     CREATE TABLE data (
       id INT AUTO_INCREMENT PRIMARY KEY,
       email VARCHAR(50),
       username VARCHAR(100),
       password VARCHAR(20)
     );
     ```

2. **Running the Application:**
   - Run the sign-up script to create new users:
     ```bash
     python signup.py
     ```
   - Run the login script to log in with existing users:
     ```bash
     python login.py
     ```

## Code Overview

### Login Script (`login.py`)

- **Functions:**
  - `forget_pass()`: Opens a window to reset the user's password.
  - `change_password()`: Handles the password reset functionality.
  - `login_user()`: Authenticates the user by checking the credentials against the database.
  - `signup_page()`: Redirects the user to the sign-up page.
  - `hide()`: Hides the password text.
  - `show()`: Shows the password text.
  - `user_enter(event)`: Clears the username field when it gains focus.
  - `password_enter(event)`: Clears the password field when it gains focus.

- **GUI Elements:**
  - Entry fields for username and password.
  - Buttons for login, forget password, and redirecting to the sign-up page.
  - Labels for decorative purposes and instructions.

### Sign-Up Script (`signup.py`)

- **Functions:**
  - `clear()`: Clears all entry fields and resets the checkbox.
  - `login_page()`: Redirects the user to the login page.
  - `connect_database()`: Handles the registration process by inserting the new user's data into the database.

- **GUI Elements:**
  - Entry fields for email, username, password, and password confirmation.
  - Checkbox for terms and conditions.
  - Buttons for sign-up and redirecting to the login page.
  - Labels for decorative purposes and instructions.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
