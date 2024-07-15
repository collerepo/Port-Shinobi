Port-Shinobi Changelog
======================

## Unreleased

* Initial release of Port-Shinobi

## 1.0.0 (2023-02-20)

* Initial commit of the port scanning script
* Supports scanning of 10 common ports (21, 22, 23, 25, 80, 139, 443, 445, 3306, 3389)
* Scans ports first, then IPs, and then by Host name
* It checks if the script is run with exactly one command-line argument (the IP address to scan). If not, it prints an error message and exits.
* It resolves the IP address using socket.gethostbyname() and stores it in the target variable.
* It creates a socket object for each port in the list and attempts to connect to the target machine on that port using connect_ex().
* If the connection is successful (i.e., connect_ex() returns 0), it prints a message indicating that the port is open.
* The script catches KeyboardInterrupt exceptions (e.g., when the user presses Ctrl+C) and exits out from execution.
* It also catches socket.gaierror exceptions (e.g., when the hostname cannot be resolved) and socket.error exceptions (e.g., when the connection cannot be established) and prints error messages.

## Future Releases

* Add support for more ports
* Improve performance and reduce timeout
* Add error handling for invalid target IPs

## Latest Release + Update 
* 1.0.1 (2024-07-14)

## Update Features for v 1.0.1
* 2 Second timeout for each port scan ran
* Employs persistence to reconnect to open ports
* Escalates to privileged mode using a custom payload
* Utilizes polymorphic and metamorphic techniques to evade detection
* Includes anti-debugging measures to detect and respond to debugging attempts
