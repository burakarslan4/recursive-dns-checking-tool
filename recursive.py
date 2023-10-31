import ipaddress
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Add your email account information here
email_user = 'email_username'
email_password = 'email_password'
email_to = 'recipient_email'

# Add your email server and port information here
email_server = 'smtphost'
email_port = 587

# List of subnets
subnets = ["XX.XX.XX.XX/XX","YY.YY.YY.YY/YY"] 

# Email subject and body
subject = 'Recursive IP Addresses'
body = 'Below are the IP addresses:\n\n'

# Read IP addresses from the valid_ips.txt file
valid_ips = []
for subnet in subnets:
    network = ipaddress.IPv4Network(subnet, strict=False)
    for ip in network.hosts():
        ip_str = str(ip)
        dig_command = f"dig +short +timeout=2 google.com @{ip_str}"

        try:
            result_bytes = subprocess.check_output(dig_command, shell=True, stderr=subprocess.STDOUT)
            result = result_bytes.decode("utf-8")

            if result.strip():  # If the result is not empty (if an IP is returned)
                valid_ips.append(ip_str)

        except subprocess.CalledProcessError:
            pass

# Create the email message
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_to
msg['Subject'] = subject
msg.attach(MIMEText(body + '\n'.join(valid_ips), 'plain'))

# Connect to the email server and send the email
try:
    server = smtplib.SMTP(email_server, email_port)
    server.starttls()
    server.login(email_user, email_password)
    text = msg.as_string()
    server.sendmail(email_user, email_to, text)
    server.quit()
    print('Email sent!')
except Exception as e:
    print(f'An error occurred while sending the email: {str(e)}')
