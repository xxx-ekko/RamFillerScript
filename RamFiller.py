import time
import psutil
import os # Import the 'os' module for random data

# --- Configuration ---
TARGET_PERCENTAGE = 0.95 # Target 95% of total RAM
# -------------------

# Get total system memory in bytes
total_memory = psutil.virtual_memory().total
target_memory = total_memory * TARGET_PERCENTAGE

# Convert to Gigabytes for user-friendly printing
total_memory_gb = total_memory / (1024**3)
target_memory_gb = target_memory / (1024**3)

print(f"Total System RAM: {total_memory_gb:.2f} GB")
print(f"Targeting {TARGET_PERCENTAGE:.0%} usage: {target_memory_gb:.2f} GB")
print("Starting to fill RAM with non-compressible data...")
print("Press Ctrl+C to stop.")

memory_hog = []
allocated_bytes = 0
chunk_size = 50 * 1024 * 1024 # Allocate in 50MB chunks

try:
    while allocated_bytes < target_memory:
        # Use random bytes
        chunk = os.urandom(chunk_size)
        
        memory_hog.append(chunk)
        allocated_bytes = len(memory_hog) * chunk_size
        
        # Calculate and print current progress
        allocated_gb = allocated_bytes / (1024**3)
        current_percentage = (allocated_bytes / total_memory) * 100
        print(f"Allocated: {allocated_gb:.2f} GB / {target_memory_gb:.2f} GB ({current_percentage:.1f}%)")
        
        time.sleep(0.2)

    print(f"\nTarget of {TARGET_PERCENTAGE:.0%} reached! Holding memory.")
    print("Press Ctrl+C to stop and release memory.")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopping the script and releasing memory.")
except MemoryError:
    print("\nMemoryError: Ran out of memory before reaching the target.")