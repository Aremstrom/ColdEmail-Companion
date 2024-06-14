# ColdEmail-Companion

A sleek Python script to streamline job application emails with résumé attachments.

## Overview

This script is your trusty companion in the job hunt, automating the process of sending job application emails with your résumé attached. It reads email addresses from a CSV file, crafts a professional email message, and dispatches it to each recipient seamlessly.

## Prerequisites

- If your Gmail account does not have 2-Factor Authentication enabled, you can use your email address and password in the `.env` file.
- If your Gmail account has 2-Factor Authentication enabled, follow these steps:
  1. Go to your Google Account's [App Passwords](https://myaccount.google.com/apppasswords) page.
  2. Select `Other (Custom name)` as the app and enter a name (e.g., "Resume Delivery").
  3. Click `Generate` to get an app-specific password.
  4. Use your email address and the generated app-specific password in the `.env` file.

## Features

- Reads email addresses from a CSV file
- Composes an email with your résumé attached
- Sends the email to each recipient via SMTP
- Updates the CSV file with email delivery status

## Setup

1. Install Python 3.
2. Install required libraries by running `pip install -r requirements.txt`.
3. Prepare a `email.csv` file with an `email` column containing recipient addresses.
4. Have your résumé file (e.g., `resume.pdf`) in the same directory.
5. Create a `.env` file in the project directory and add the following lines:

`EMAIL_ADDRESS=your_email@example.com`

`EMAIL_PASSWORD=your_email_password_or_app_password`

Replace `your_email@example.com` and `your_email_password_or_app_password` with your actual email credentials (see Prerequisites section for details).

## Usage

1. Navigate to the project directory.
2. Run `python resume_delivery_automator.py`.
3. A new `data_updated.csv` file will be created with an `Email_Sent` column indicating delivery status.

## Contributing

Contributions are welcome! Open an issue or submit a pull request.

## License

[MIT License](LICENSE)
