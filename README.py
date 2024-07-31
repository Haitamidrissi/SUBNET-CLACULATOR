
# # VLSM and FLSM IP Address Calculator

# This Python script provides a graphical user interface (GUI) to calculate Variable Length Subnet Masking (VLSM) and Fixed Length Subnet Masking (FLSM) subnets. The tool is designed to assist network engineers and students in creating subnets based on specific IP address requirements.

# ## Features

# - **VLSM Calculator:** Calculate subnets based on variable length subnet masks for different hosts.
# - **FLSM Calculator:** Calculate fixed-length subnets from a given base IP address and prefix length.
# - **User-friendly GUI:** Easy-to-use interface built with Tkinter.
# - **Detailed Output:** Displays network address, prefix length, first and last usable IP addresses, subnet mask, and broadcast address.

# ## Prerequisites

# - Python 3.x
# - Tkinter (usually included with Python standard libraries)
# - `ipaddress` library (included with Python standard libraries)

# ## Usage

# 1. **Run the Script:** Open a terminal or command prompt and execute the script:
#    ```bash
#    python vlsm_flsm_calculator.py
#    ```

# 2. **VLSM Calculation:**
#    - Enter the base IP address and prefix length (CIDR notation).
#    - Click "Add Host" to add host requirements. Enter the host name and the number of hosts required.
#    - Click "Calculate" to perform the VLSM calculation. The results will be displayed in the table below.

# 3. **FLSM Calculation:**
#    - Enter the base IP address and prefix length (CIDR notation).
#    - Enter the number of subnets required.
#    - Click "Calculate" to perform the FLSM calculation. The results will be displayed in the table below.

# ## Interface Description

# - **Tabs:** The interface has three tabs:
#   - **VLSM Calculator:** For calculating subnets with variable lengths.
#   - **FLSM Calculator:** For calculating subnets with fixed lengths.
#   - **Info:** Provides information about the script and credits.

# - **Input Fields:**
#   - **Base IP Address:** The starting IP address for subnetting.
#   - **Network Prefix Length:** The prefix length in CIDR notation.
#   - **Number of Hosts (VLSM):** Number of required hosts for each subnet (entered dynamically).
#   - **Number of Subnets (FLSM):** Total number of required subnets.

# - **Buttons:**
#   - **Add Host (VLSM):** Add host entry fields.
#   - **Calculate:** Perform the subnet calculation.

# - **Output Table:**
#   - Displays the calculated subnets with details like network address, prefix length, usable IP range, subnet mask, and broadcast address.

# ## Example

# **VLSM Calculation Example:**

# 1. Enter Base IP Address: `192.168.1.0`
# 2. Enter Network Prefix Length: `24`
# 3. Add Host Entries:
#    - Host 1: Name: `HostA`, Count: `10`
#    - Host 2: Name: `HostB`, Count: `20`
# 4. Click "Calculate"

# **FLSM Calculation Example:**

# 1. Enter Base IP Address: `192.168.1.0`
# 2. Enter Network Prefix Length: `24`
# 3. Enter Number of Subnets: `4`
# 4. Click "Calculate"

# ## Credits

# Created by Haitam BEN DAHMANE IDRISSI.

# Special thanks to professors Lahcen Soussi and Mohamed Aamraoui for their guidance and support.

