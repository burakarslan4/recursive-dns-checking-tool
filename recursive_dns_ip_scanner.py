import ipaddress
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os  # Import the os module

# Add your email account information here
email_user = 'xxxxxx'
email_password = 'xxxxxxx'
email_to = 'mail@domain.com'

# Add email server and port information here
email_server = 'sandbox.smtp.mailtrap.io'
email_port = 25  # 25,587

# Add send_email_while_empty variable (set to True to always send email)
send_email_while_empty = True

# List of subnets
subnets = ["192.168.1.0/24", "10.0.0.128/25", "192.168.10.0/25"]

# Email subject and body
subject = 'Recursive DNS IP Addresses'
body = 'The following IP addresses are found:\n\n'

# Create a list to store valid IP addresses
valid_ips = []

for subnet in subnets:
    network = ipaddress.IPv4Network(subnet, strict=False)
    print(f"Scanning in the {subnet} subnet...")  # Notify that subnet scanning has started
    for ip in network.hosts():
        ip_str = str(ip)
        dig_command = f"dig +short +timeout=2 google.com @{ip_str}"

        try:
            result_bytes = subprocess.check_output(dig_command, shell=True, stderr=subprocess.STDOUT)
            result = result_bytes.decode("utf-8")

            if result.strip():  # If the result is not empty (IP is returned)
                valid_ips.append(ip_str)
                print(f"Valid IP address found: {ip_str}")  # Print the valid IP address to the console

        except subprocess.CalledProcessError:
            pass

# Check if there are valid IPs
if send_email_while_empty or valid_ips:
    # Create an email message
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_to
    msg['Subject'] = subject

    if valid_ips:
        body_text = body + '\n'.join(valid_ips)
    else:
        body_text = "Good news! No IP addresses responding to recursive DNS queries were found."

    msg.attach(MIMEText(body_text, 'plain'))

    # Connect to the email server and send the email (without SSL)
    try:
        server = smtplib.SMTP(email_server, email_port)
        server.login(email_user, email_password)
        text = msg.as_string()
        server.sendmail(email_user, email_to, text)
        server.quit()
        print('Email sent!')
    except Exception as e:
        print(f'An error occurred while sending the email: {str(e)}')
else:
    # If no valid IPs were found, send an email with a specific message
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_to
    msg['Subject'] = subject
    msg.attach(MIMEText("Good news! No IP addresses responding to recursive DNS queries were found.", 'plain'))

    # Connect to the email server and send the email (without SSL)
    try:
        server = smtplib.SMTP(email_server, email_port)
        server.login(email_user, email_password)
        text = msg.as_string()
        server.sendmail(email_user, email_to, text)
        server.quit()
        print('Email sent!')
    except Exception as e:
        print(f'An error occurred while sending the email: {str(e)}')

# After the task is complete, delete the valid_ips.txt file
if os.path.exists('valid_ips.txt'):
    os.remove('valid_ips.txt')
