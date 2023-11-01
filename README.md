# Recursive DNS IP Scanner Tool for Subnets

Welcome to the **Recursive DNS IP Scanner Tool for Subnets** project! This tool is designed to find IP addresses that respond to recursive DNS queries. You can use it to scan multiple subnets and identify the IP addresses that provide DNS resolution.

## Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Results](#results)
- [License](#license)

## Overview

The **Recursive DNS IP Scanner Tool for Subnets** is a Python-based project that allows you to scan multiple subnets and identify IP addresses that respond to recursive DNS queries. It is a useful tool for network administrators and security professionals to discover DNS resolvers within a network.

## How It Works

This tool works by scanning a list of specified subnets, probing each IP address within those subnets with recursive DNS queries. If an IP address responds to the queries, it is considered a valid result. You will be provided with a list of these IP addresses.

## Requirements

Before using this script, ensure you have the following requirements in place:

- Python 3.x
- Required Python packages: `ipaddress`, `subprocess`, `smtplib`, `email.mime`
- Internet access for conducting DNS queries

## Getting Started

To get started with this tool, follow these steps:

1. Clone this repository to your local machine.
2. Update the configuration in the script to include your email account information, email server details, and the list of subnets to scan.
3. Run the script to start the scanning process.

If valid IP addresses are found, you will receive an email with the list of results. If no valid IP addresses are found, you will receive an email with a specific message.

## Configuration

You can configure the tool by editing the following variables in the script:

- `email_user`: Your email account username.
- `email_password`: Your email account password.
- `email_to`: The recipient email address.
- `email_server`: The email server for sending emails.
- `email_port`: The port for the email server (e.g., 25 or 587 for plain text. SSL and TLS not support yet).
- `send_email_while_empty`: Set to `True` to always send an email, even if no valid IPs are found.
- `subnets`: The list of subnets to scan.

## Results

If the tool finds valid IP addresses, you will receive an email with a list of those IP addresses. If no valid IPs are found, you will receive an email with the message "Good news! No IP addresses responding to recursive DNS queries were found."

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute to this project or report any issues you encounter.

**This project has been written with the assistance of ChatGPT 3.5.**
