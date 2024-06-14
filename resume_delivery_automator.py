from dotenv import load_dotenv
import os
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# Open the CSV files
with open('email.csv', 'r') as csvfile, open('data_updated.csv', 'r+', newline='') as updated_file:
    csvreader = csv.DictReader(csvfile)
    fieldnames = csvreader.fieldnames + ['Email_Sent']
    csvwriter = csv.DictWriter(updated_file, fieldnames=fieldnames)

    # Loop through each row in the CSV file
    for row in csvreader:
        recipient_email = row['email']

        # Check if the email has already been sent
        updated_file.seek(0)
        sent_emails = [row for row in csv.DictReader(updated_file) if row['email'] == recipient_email and row['Email_Sent'] == 'Yes']
        if sent_emails:
            print(f'Skipping email to {recipient_email} (already sent)')
            continue

        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = 'Job Application'

        # Attach the resume file
        with open('Jay_Resume.pdf', 'rb') as file:
            resume_part = MIMEApplication(file.read(), Name='Jay_Resume.pdf')
            resume_part['Content-Disposition'] = 'attachment; filename="Jay_Resume.pdf"'
            msg.attach(resume_part)

        # Add the body of the email
        # body = 'Dear HR,\n\nPlease find my resume attached for your consideration.\n\nBest regards,\nYour Name'
        body = """\
        <html>
        <body>
            <p>Dear HR,<br><br>
        
        Please find my resume attached for your consideration.
            
            Best regards,<br>
            Your Name
            </p>
        </body>
        </html>
        """

        msg.attach(MIMEText(body, 'html'))

        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            try:
                failed = smtp.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
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