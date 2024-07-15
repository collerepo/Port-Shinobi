
Port Shinobi: A Port Scanner specialized in Covert & Advanced Evasion Techniques
================================================================================

**Description:**
------------------------
Port Shinobi is a Python-based port scanner designed to evade detection by modern security systems. It employs advanced techniques such as polymorphism, metamorphism, and anti-debugging to remain undetected while scanning for open ports on a target system.

**Features:**
-----------------------
* Scans for open ports on a target system
* Supports multi-port scans
* 2 Second timeout for each port scan ran
* Employs persistence to reconnect to open ports
* Escalates to privileged mode using a custom payload
* Utilizes polymorphic and metamorphic techniques to evade detection
* Includes anti-debugging measures to detect and respond to debugging attempts

**Usage (when executing through CLI/Terminal):**
------------------------
1. Clone the repository 'git clone https://github.com/collerepo/Port-Shinobi.git'
2. Navigate to the repository directory: 'cd Port-Shinobi'
3. Run the script: 'python3 port_shinobi.py <target_ip>' 

Example: 'python3 port_shinobi.py 192.168.1.1'

The script will scan the target IP address for open ports and display the results.

**Requirements:**
-------------------------
* `Python 3.9 or later` Version 
* `socket` library
* `sys` library
* `random` library
* `time` library
* `os` library

**License:**
------------------------
This project is licensed under the Apache 2.0 License. See `LICENSE.md` for details.

Copyright 2024 Rodrigo Coll

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

**Warning:**
------------------------
This tool is for educational purposes only and should not be used for malicious activities. By proceeding further, you are adhereing to your regional regulations and the ethical consideration of this publication at your own risk. All simulated trials were conducted by a Security Researcher in a controlled, isolated environment which targeted a live dummy system for best results.
