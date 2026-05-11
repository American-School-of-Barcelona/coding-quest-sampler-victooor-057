"""
CodingQuest Problem 29: Broken firewall

Your input data is in input.txt.
The data has been loaded into a list called `data` for you.
Each item in the list is one line from the file, as a string.

Write your solution below the comment line.
"""

# --- Load the data (don't change this) ---
with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

# Take a look at the first few lines
print(f"Loaded {len(data)} lines.")
print("First 5 lines:")
for line in data[:5]:
    print("  ", line)
print()

# --- Your code here ---
internal_total = 0
wifi_total = 0

for line in data:
    # Length (bytes 3-4)
    length_hex = line[4:8]
    length = int(length_hex, 16)

    # Source IP (bytes 13-16)
    src_hex = line[24:32]
    src_ip = ".".join(str(int(src_hex[i:i+2], 16)) for i in range(0, 8, 2))

    # Destination IP (bytes 17-20)
    dst_hex = line[32:40]
    dst_ip = ".".join(str(int(dst_hex[i:i+2], 16)) for i in range(0, 8, 2))

    def is_internal(ip):
        parts = list(map(int, ip.split(".")))
        return parts[0] == 192 and parts[1] == 168 and 0 <= parts[2] <= 254 and 0 <= parts[3] <= 254

    def is_wifi(ip):
        parts = list(map(int, ip.split(".")))
        return parts[0] == 10 and parts[1] == 0 and 0 <= parts[2] <= 254 and 0 <= parts[3] <= 254

    if is_internal(src_ip) or is_internal(dst_ip):
        internal_total += length
    elif is_wifi(src_ip) or is_wifi(dst_ip):
        wifi_total += length

print(f"{internal_total}/{wifi_total}")
