from dotenv import load_dotenv
import os
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

load_dotenv()

email = os.getenv('EMAIL_ADDRESS')
password = os.getenv('EMAIL_PASSWORD')

# Open the CSV file
with open('email.csv', 'r') as csvfile, open('data_updated.csv', 'w', newline='') as updated_file:
    csvreader = csv.DictReader(csvfile)
    fieldnames = csvreader.fieldnames + ['Email_Sent']
    csvwriter = csv.DictWriter(updated_file, fieldnames=fieldnames)
    csvwriter.writeheader()

    # Loop through each row in the CSV file
    for row in csvreader:
        # Extract the email address from the row
        recipient_email = row['email']

        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = recipient_email
        msg['Subject'] = 'Job Application'

        # Attach the resume file
        with open('Jay_Resume.pdf', 'rb') as file:
            resume_part = MIMEApplication(file.read(), Name='Jay_Resume.pdf')
            resume_part['Content-Disposition'] = 'attachment; filename="Jay_Resume.pdf"'
            msg.attach(resume_part)

        # Add the body of the email
        body = 'Dear HR,\n\nPlease find my resume attached for your consideration.\n\nBest regards,\nYour Name'
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(email, password)
            try:
                failed = smtp.sendmail(email, recipient_email, msg.as_string())
                if failed:
                    print(f'Failed to send email to {recipient_email}')
                    row['Email_Sent'] = 'No'
                else:
                    print(f'Email sent to {recipient_email}')
                    row['Email_Sent'] = 'Yes'
            except smtplib.SMTPException as e:
                print(f'Error sending email to {recipient_email}: {e}')
                row['Email_Sent'] = 'No'

        csvwriter.writerow(row)