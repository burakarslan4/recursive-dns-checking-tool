# bulk-recursive-dns
**Script Purpose:**

This script is designed to perform the following tasks:

1-) It reads a list of IP subnets.

2-) For each IP subnet, it tries to resolve DNS queries using the dig command to check if any valid IP addresses can be reached.

3-) If a valid IP is found, it compiles a list of these IPs.

4-) It sends an email containing the list of valid IP addresses to a specified recipient.

**How to Use the Script:**

**1-) Set up Email Configuration:**

- Replace email_user with your email address.
- Replace email_password with your email account password or an app-specific password if applicable.
- Replace email_to with the recipient's email address.
- Configure the email_server and email_port to match your email service provider's settings.

**2-) Define IP Subnets:**

- Edit the subnets list to include the IP subnets you want to scan.

**3-) Run the Script:**

- Execute the script using a Python interpreter.

**4-) Check the Output:**

- The script will attempt to resolve DNS queries for each IP address in the specified subnets.
- If a valid IP address is found, it will be added to the list of valid IPs.
- An email containing the list of valid IP addresses will be sent to the specified recipient.

**5-) Error Handling:**

- If there are any errors during the email sending process, the script will display an error message.

**Important Notes:**

- Make sure you have the dig command available on your system.
- Ensure that the necessary email configuration details are accurate and allowed by your email service provider.

In summary, this script is a tool for checking and notifying you of valid IP addresses within specific subnets, and it can be customized to suit your needs by adjusting the email configuration and the list of subnets to scan.
