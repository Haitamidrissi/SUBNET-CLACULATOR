import tkinter as tk
from tkinter import messagebox, ttk
import ipaddress
import math

def calculate_vlsm(base_ip, prefix_length, hosts):
    subnets = []
    try:
        base_network = ipaddress.ip_network(f"{base_ip}/{prefix_length}", strict=False)
    except ValueError:
        raise ValueError("Invalid base IP address or prefix length.")
    
    current_address = base_network.network_address
    

    hosts.sort(key=lambda x: x[1], reverse=True)
    
    for host_name, host_count in hosts:
     
        required_hosts = host_count + 2 
        subnet_bits = math.ceil(math.log2(required_hosts))
        new_prefix_length = 32 - subnet_bits
        
        subnet = ipaddress.ip_network((current_address, new_prefix_length), strict=False)
        
        subnets.append((host_name, host_count, subnet))
        
        current_address = subnet.network_address + 2**(32 - new_prefix_length)
    
    return subnets

def on_vlsm_calculate():
    try:
        base_ip = entry_ip_vlsm.get()
        prefix_length = int(entry_prefix_vlsm.get())
        hosts = []
        for i in range(len(host_entries_vlsm)):
            host_name = host_entries_vlsm[i][0].get()
            host_count = int(host_entries_vlsm[i][1].get())
            hosts.append((host_name, host_count))
        
        if not base_ip:
            raise ValueError("Base IP address is required.")
        
        if not hosts:
            raise ValueError("At least one host count is required.")
        
        if not (0 <= prefix_length <= 32):
            raise ValueError("Prefix length must be between 0 and 32.")
        
        subnets = calculate_vlsm(base_ip, prefix_length, hosts)
        

        for item in tree_vlsm.get_children():
            tree_vlsm.delete(item)
        

        for host_name, host_count, subnet in subnets:
            first_usable_ip = subnet.network_address + 1
            last_usable_ip = subnet.broadcast_address - 1
            subnet_mask = subnet.netmask
            tree_vlsm.insert('', 'end', values=(
                f"{host_name} ({host_count})", 
                subnet.network_address, 
                f"/{subnet.prefixlen}",
                first_usable_ip, 
                last_usable_ip, 
                subnet_mask,
                subnet.broadcast_address
            ))
        
        messagebox.showinfo("Success", "VLSM Calculation Completed Successfully!")
        
    except Exception as e:
        messagebox.showerror("Error", str(e))

def add_host_entry_vlsm():
    host_frame = tk.Frame(hosts_frame_vlsm, bg='#f0f0f0')
    host_frame.pack(pady=2, padx=10, fill='x')
    
    host_name_label = tk.Label(host_frame, text=f"Host {len(host_entries_vlsm) + 1} Name:", bg='#f0f0f0')
    host_name_label.pack(side=tk.LEFT, padx=5)
    
    host_name_entry = tk.Entry(host_frame, width=15)
    host_name_entry.pack(side=tk.LEFT, padx=5)
    
    host_count_label = tk.Label(host_frame, text="Count:", bg='#f0f0f0')
    host_count_label.pack(side=tk.LEFT, padx=5)
    
    host_count_entry = tk.Entry(host_frame, width=10)
    host_count_entry.pack(side=tk.LEFT, padx=5)
    
    host_entries_vlsm.append((host_name_entry, host_count_entry))

def calculate_flsm(base_ip, prefix_length, num_subnets):
    subnets = []
    try:
        base_network = ipaddress.ip_network(f"{base_ip}/{prefix_length}", strict=False)
    except ValueError:
        raise ValueError("Invalid base IP address or prefix length.")
    
    subnet_prefix_length = math.ceil(math.log2(num_subnets))
    new_prefix_length = prefix_length + subnet_prefix_length
    
    if new_prefix_length > 32:
        raise ValueError("Not enough address space to create the required subnets.")
    
    current_address = base_network.network_address
    
    for i in range(num_subnets):
        subnet = ipaddress.ip_network((current_address, new_prefix_length), strict=False)
        subnets.append(subnet)
        current_address = subnet.network_address + 2**(32 - new_prefix_length)
    
    return subnets

def on_flsm_calculate():
    try:
        base_ip = entry_ip_flsm.get()
        prefix_length = int(entry_prefix_flsm.get())
        num_subnets = int(entry_num_subnets.get())
        
        if not base_ip:
            raise ValueError("Base IP address is required.")
        
        if not (0 <= prefix_length <= 32):
            raise ValueError("Prefix length must be between 0 and 32.")
        
        if num_subnets <= 0:
            raise ValueError("Number of subnets must be a positive integer.")
        
        subnets = calculate_flsm(base_ip, prefix_length, num_subnets)

        for item in tree_flsm.get_children():
            tree_flsm.delete(item)
        

        for subnet in subnets:
            first_usable_ip = subnet.network_address + 1
            last_usable_ip = subnet.broadcast_address - 1
            subnet_mask = subnet.netmask
            tree_flsm.insert('', 'end', values=(
                subnet.network_address, 
                f"/{subnet.prefixlen}",
                first_usable_ip, 
                last_usable_ip, 
                subnet_mask,
                subnet.broadcast_address
            ))
        
        messagebox.showinfo("Success", "FLSM Calculation Completed Successfully!")
        
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("DECOUPAGE CALCULATION")
root.geometry("1480x500")


notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)


style = ttk.Style()
style.configure('TNotebook.Tab', font=('Arial', 12, 'bold'))
style.configure('TButton', font=('Arial', 12), padding=5)
style.configure('Treeview.Heading', font=('Arial', 10, 'bold'))

frame_vlsm = tk.Frame(notebook, bg='#e6f7ff')
frame_vlsm.pack(fill='both', expand=True)
notebook.add(frame_vlsm, text='VLSM Calculator')


frame_flsm = tk.Frame(notebook, bg='#fff7e6')
frame_flsm.pack(fill='both', expand=True)
notebook.add(frame_flsm, text='FLSM Calculator')


frame_info = tk.Frame(notebook, bg='#e6ffe6')
frame_info.pack(fill='both', expand=True)
notebook.add(frame_info, text='Info')


tk.Label(frame_vlsm, text="Enter Base IP Address:", bg='#e6f7ff', font=('Arial', 12)).pack(pady=5)
entry_ip_vlsm = tk.Entry(frame_vlsm, width=30, font=('Arial', 12))
entry_ip_vlsm.pack(pady=5)


tk.Label(frame_vlsm, text="Enter Network Prefix Length (CIDR):", bg='#e6f7ff', font=('Arial', 12)).pack(pady=5)
entry_prefix_vlsm = tk.Entry(frame_vlsm, width=30, font=('Arial', 12))
entry_prefix_vlsm.pack(pady=5)


hosts_frame_vlsm = tk.Frame(frame_vlsm, bg='#e6f7ff')
hosts_frame_vlsm.pack(pady=5)

btn_add_host_vlsm = tk.Button(frame_vlsm, text="Add Host", command=add_host_entry_vlsm)
btn_add_host_vlsm.pack(pady=10)

host_entries_vlsm = []

btn_calculate_vlsm = tk.Button(frame_vlsm, text="Calculate", command=on_vlsm_calculate)
btn_calculate_vlsm.pack(pady=10)


columns_vlsm = ('Host (Count)', 'Network Address', 'Prefix Length', 'First Usable IP', 'Last Usable IP', 'Subnet Mask', 'Broadcast Address')
tree_vlsm = ttk.Treeview(frame_vlsm, columns=columns_vlsm, show='headings')

for col in columns_vlsm:
    tree_vlsm.heading(col, text=col)

tree_vlsm.pack(pady=10, padx=10, fill='both', expand=True)

tk.Label(frame_flsm, text="Enter Base IP Address:", bg='#fff7e6', font=('Arial', 12)).pack(pady=5)
entry_ip_flsm = tk.Entry(frame_flsm, width=30, font=('Arial', 12))
entry_ip_flsm.pack(pady=5)


tk.Label(frame_flsm, text="Enter Network Prefix Length (CIDR):", bg='#fff7e6', font=('Arial', 12)).pack(pady=5)
entry_prefix_flsm = tk.Entry(frame_flsm, width=30, font=('Arial', 12))
entry_prefix_flsm.pack(pady=5)


tk.Label(frame_flsm, text="Enter Number of Subnets:", bg='#fff7e6', font=('Arial', 12)).pack(pady=5)
entry_num_subnets = tk.Entry(frame_flsm, width=30, font=('Arial', 12))
entry_num_subnets.pack(pady=5)


btn_calculate_flsm = tk.Button(frame_flsm, text="Calculate", command=on_flsm_calculate)
btn_calculate_flsm.pack(pady=10)


columns_flsm = ('Network Address', 'Prefix Length', 'First Usable IP', 'Last Usable IP', 'Subnet Mask', 'Broadcast Address')
tree_flsm = ttk.Treeview(frame_flsm, columns=columns_flsm, show='headings')

for col in columns_flsm:
    tree_flsm.heading(col, text=col)

tree_flsm.pack(pady=10, padx=10, fill='both', expand=True)


info_label = tk.Label(frame_info, text="Created by Haitam BEN DAHMANE IDRISSI ", font=('Arial', 19, 'bold'), bg='#e6ffe6')
info_label.pack(pady=10)

vlsm_info = tk.Label(frame_info, text=(
    "MORE THANKS TO MY DEDICATED PROFESSOR LAHCEN SOUSSI AND MOHAMED AAMRAOUI FOR THEIR EFFORT"
), wraplength=400, justify="left", bg='#e6ffe6', font=('Arial', 12))
vlsm_info.pack(pady=10, padx=10)

root.mainloop()

