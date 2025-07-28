import time
import psutil
import os # Import the 'os' module for random data

# --- Configuration ---
TARGET_PERCENTAGE = 95.0 # Target 95% of total RAM
# -------------------

# Get total system memory for display purposes
total_memory_gb = psutil.virtual_memory().total / (1024**3)
print(f"Total System RAM: {total_memory_gb:.2f} GB")
print(f"Actively maintaining RAM usage at {TARGET_PERCENTAGE}%...")
print("Press Ctrl+C to stop.")

memory_hog = []
chunk_size = 100 * 1024 * 1024 # Allocate in smaller 100MB chunks for finer control

try:
    # This is the main monitoring and filling loop
    while True:
        # Get the current system-wide RAM usage percentage
        current_percent = psutil.virtual_memory().percent

        # If current usage is below our target, add more memory
        if current_percent < TARGET_PERCENTAGE:
            allocated_gb = (len(memory_hog) * chunk_size) / (1024**3)
            print(f"Usage at {current_percent:.1f}%. Below target. Allocating more... (Total held: {allocated_gb:.2f} GB)")
            try:
                # Add another chunk of non-compressible random data
                chunk = os.urandom(chunk_size)
                memory_hog.append(chunk)
            except MemoryError:
                print("MemoryError: OS refused to allocate more memory. Holding current amount.")
                # Wait longer if we hit a memory error before trying again
                time.sleep(5)
        else:
            # If we are at or above the target, just wait and hold
            print(f"Usage at {current_percent:.1f}%. Holding at target. Checking again soon...")

        # Wait for a second before checking again to avoid using too much CPU
        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopping the script and releasing all allocated memory.")