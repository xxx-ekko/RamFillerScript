# Smart RAM Filler 🧠

A Python script designed to test system performance under high memory load. Unlike simple allocation scripts, this tool actively monitors real-time system RAM usage and works to maintain it at a specific target percentage.

## Features

-   **Targeted Filling**: Fills your system's RAM to a specific percentage (e.g., 95%).
-   **Active Monitoring**: Continuously checks the actual system-wide memory usage using `psutil`.
-   **Dynamic Allocation**: If the OS frees up memory (e.g., by swapping to disk), the script detects this and allocates more RAM to get back to the target.
-   **Non-Compressible Data**: Uses random bytes (`os.urandom`) to ensure that physical RAM is being used, bypassing OS-level memory compression.

---

## How to Use

### Prerequisites

-   Python 3
-   Git

### Installation & Setup

1.  **Clone the repository:**

2.  **Install the required Python package:**
    ```bash
    pip3 install psutil
    ```

### Running the Script

To start the memory test, simply run the script from your terminal:

```bash
python3 RamFiller.py
