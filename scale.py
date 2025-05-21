import hid
import time

VENDOR_ID = 0x0922
PRODUCT_ID = 0x8009  # S250 model

device = hid.device()
device.open(VENDOR_ID, PRODUCT_ID)
device.set_nonblocking(True)

print("Reading from DYMO S250 scale...")

try:
    while True:
        data = device.read(6)
        if data:
            # Weight is usually in grams, little endian
            weight_raw = data[4] + (data[5] << 8)

            # Byte 1 may indicate unit (e.g., 0x02 for grams, 0x11 for ounces)
            unit_code = data[2]
            if unit_code == 0x02:
                unit = "g"
            elif unit_code == 0x0b:
                unit = "oz"
                weight = weight_raw / 10.0  # Convert to decimal ounces
            else:
                unit = "unknown"
                weight = weight_raw

            print(f"Weight: {weight_raw} {unit}")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    device.close()

