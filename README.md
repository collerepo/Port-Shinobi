
Stealthy Port Sentinel: A Port Scanner specialized in Covert & Advanced Evasion Techniques
============================================================================================

**Description:**
Stealthy Port Sentinel is a Python-based port scanner designed to evade detection by modern security systems. It employs advanced techniques such as polymorphism, metamorphism, and anti-debugging to remain stealthy while scanning for open ports on a target system.

**Features:**

* Scans for open ports on a target system
* Employs persistence to reconnect to open ports
* Escalates to privileged mode using a custom payload
* Utilizes polymorphic and metamorphic techniques to evade detection
* Includes anti-debugging measures to detect and respond to debugging attempts

**Usage (when executing through CLI/Terminal):**
$ python3 PortSentinel.py <target_ip>

**Requirements:**

* `Python 3.9 or later` Version 
* `socket` library
* `sys` library
* `random` library
* `time` library
* `os` library

**License:**
This project is licensed under the MIT License. See `LICENSE` for details.

**Warning:**
This tool is for educational purposes only and should not be used for malicious activities. By proceeding, you are agreeing to the ethical considerations of this publication at your own risk. All simulated runs were conducted by a Security Researcher in a controlled and isolated environment which targeted a live dummy system for realistic results.
