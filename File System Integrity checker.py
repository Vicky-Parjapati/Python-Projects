import hashlib
import json
import os

# Calculate SHA-256 hash of a file
def calculate_file_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

# Create or update baseline of files in a directory
def create_baseline(directory, baseline_file="baseline.json"):
    baseline = {}
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = calculate_file_hash(file_path)
            baseline[file_path] = file_hash
    with open(baseline_file, "w") as f:
        json.dump(baseline, f, indent=4)
    print(f"[+] Baseline created and saved to {baseline_file}")

# Check for changes by comparing current state to baseline
def check_integrity(directory, baseline_file="baseline.json"):
    if not os.path.exists(baseline_file):
        print("[-] Baseline file not found. Create a baseline first.")
        return

    # Load baseline
    with open(baseline_file, "r") as f:
        baseline = json.load(f)

    # Check current state
    current_state = {}
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = calculate_file_hash(file_path)
            current_state[file_path] = file_hash

    # Compare baseline and current state
    print("[*] Checking for changes...")
    # Check for modified or missing files
    for file_path, baseline_hash in baseline.items():
        if file_path not in current_state:
            print(f"[-] File deleted: {file_path}")
        elif current_state[file_path] != baseline_hash:
            print(f"[-] File modified: {file_path}")
    # Check for new files
    for file_path in current_state:
        if file_path not in baseline:
            print(f"[-] New file added: {file_path}")

# Main menu with error handling
if __name__ == "__main__":
    try:
        directory = input("Enter directory to monitor (e.g., ./test_folder): ")
        # Validate directory
        if not os.path.isdir(directory):
            print(f"[-] Error: '{directory}' is not a valid directory.")
            exit(1)
        
        print("1. Create baseline")
        print("2. Check integrity")
        choice = input("Enter 1 or 2: ")
        
        # Validate choice
        if choice not in ["1", "2"]:
            print("[-] Error: Invalid choice. Please enter 1 or 2.")
            exit(1)
        
        if choice == "1":
            create_baseline(directory)
        elif choice == "2":
            check_integrity(directory)
            
    except EOFError:
        print("[-] Error: No input provided (EOF). Please run the program in an interactive environment.")
        exit(1)
    except KeyboardInterrupt:
        print("\n[-] Program terminated by user (Ctrl+C).")
        exit(1)
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")
        exit(1)
