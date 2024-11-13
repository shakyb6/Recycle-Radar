# Web Based Application for Recycle Waste Management

A web-based platform developed using Django for efficient scrap collection management. The platform allows users to book scrap collection services, track their requests in real-time, and securely pay for the services. It also includes an admin dashboard to manage bookings and process requests. The project promotes environmental awareness through its content.

## Features

- **User Registration & Authentication**: Secure login/signup system for users.
- **Booking System**: Allows users to schedule scrap collection services.
- **Real-Time Tracking**: Users can track the status of their scrap collection in real-time.
- **Payment Gateway Integration**: Secure payment integration using Razorpay for smooth transactions.
- **Admin Dashboard**: Admins can manage user bookings, view requests, and process them accordingly.
- **Responsive UI**: Mobile-friendly interface built with HTML, CSS, and JavaScript.

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Payment Gateway**: Razorpay
- **Version Control**: Git

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- Git

### Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/scrap-collection-platform.git
    cd scrap-collection-platform
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser for the admin dashboard:
    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```bash
    python manage.py runserver
    ```

8. Access the platform on your browser at `http://127.0.0.1:8000/`.

### Razorpay Integration

To set up Razorpay payment integration, follow these steps:

1. Sign up on [Razorpay](https://razorpay.com/) and get your API keys.
2. Add your `RAZORPAY_KEY_ID` and `RAZORPAY_SECRET_KEY` in the project's `settings.py` file.

## Admin Dashboard

Access the admin panel at `http://127.0.0.1:8000/admin/` after logging in with the superuser credentials. From here, you can manage user bookings and process requests.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request. Please follow the code style and ensure that all tests pass before submitting.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Environmental Awareness

We are committed to promoting environmental sustainability through this platform by helping reduce waste and promoting recycling. Let's make a difference together!

## Contact

If you have any questions or suggestions, feel free to open an issue or contact me at your-email@example.com.

