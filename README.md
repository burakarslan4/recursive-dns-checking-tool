# Recursive DNS IP Scanner Tool for Subnets

The **Recursive DNS IP Scanner Tool for Subnets** is a Python script designed to scan a list of IP subnets, perform recursive DNS queries on each IP address within those subnets, and send an email with the results. The tool is especially useful for identifying IP addresses that respond to recursive DNS queries.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Description

The **Recursive DNS IP Scanner Tool for Subnets** performs the following tasks:

- Scans specified IP subnets for potential DNS resolvers.
- Conducts recursive DNS queries on each IP address within the subnets.
- Compiles a list of IP addresses that respond to recursive DNS queries.
- Sends an email notification with the list of valid IP addresses.

The tool allows you to configure email settings, choose whether to use SSL for email communication, and decide whether to send an email even if no valid IP addresses are found.

## Requirements

Before using this script, ensure you have the following requirements in place:

- Python 3.x
- Required Python packages: `ipaddress`, `subprocess`, `smtplib`, `email.mime`
- Internet access for conducting DNS queries

## Usage

### Configuration

1. Clone the repository to your local machine.
2. Open the script in a text editor.
3. Configure the following variables at the top of the script:
   - `email_user`: Your email username.
   - `email_password`: Your email password.
   - `email_to`: The recipient's email address.
   - `email_server`: Your SMTP server address (e.g., 'smtp.example.com').
   - `email_port`: Your SMTP server port (e.g., 587 for TLS or 465 for SSL).
   - `use_ssl`: Set to `True` to use SSL for email communication, or `False` for non-SSL.
   - `send_email_while_empty`: Set to `True` to send an email even if no valid IP addresses are found, or `False` to send only when valid IPs are found.
   - `subnets`: List of IP subnets you want to scan.
   - `subject`: The email subject.
   
4. Save the script.

### Running the Script

To run the script, follow these steps:

1. Open your terminal and navigate to the project directory.
2. Run the script with the command: `python recursive_dns_ip_scanner.py`

The script will scan the specified subnets, perform recursive DNS queries, and print the valid IP addresses that respond to recursive DNS queries. If configured to do so, it will also send an email with the results.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**This project has been written with the assistance of ChatGPT 3.5.**
