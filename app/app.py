import os
import time
import subprocess
import json

# Path helper: points to the data folder relative to this script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(BASE_DIR, "data", "autosanp_logs.json")
INVENTORY = os.path.join(BASE_DIR, "data", "hosts.ini")
PASS_FILE = os.path.join(BASE_DIR, "secrets", "pass.txt")

def log_action(policy_name, status, message):
    log_entry = {
        "timestamp": time.ctime(),
        "host": "Managed Nodes",
        "policy": policy_name,
        "status": status,
                "details": message
    }
    # Using the absolute path to ensure logs save in the 'data' folder
    with open(LOG_FILE, 'a') as f:
        f.write(json.dumps(log_entry) + "\n")

def enforce_policy(policy_file):
    policy_path = os.path.join(BASE_DIR, "policies", policy_file)
    inventory_path = os.path.join(BASE_DIR, "data", "hosts.ini")
    pass_path = os.path.join(BASE_DIR, "secrets", "pass.txt")
    
    print(f"[{time.ctime()}] AutoSANP: Enforcing {policy_file}...")
    
    # The command MUST include the password file
    command = f"ansible-playbook -i {inventory_path} {policy_path} --become-password-file {pass_path}"

    try:

        # Change this line inside enforce_policy function:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # ADD THESE TWO LINES IMMEDIATELY AFTER:
        print("--- RAW ANSIBLE OUTPUT START ---")
        print(result.stdout)
        print(result.stderr)
        print("--- RAW ANSIBLE OUTPUT END ---")
        
        # DEBUG: Print the raw output to Terminal 2 so you can see wh>
        if result.returncode != 0:
            print(f"DEBUG ERROR: {result.stderr}")

        # LOGIC: Check for real success or failure
        if "fatal" in result.stdout.lower() or "failed=1" in result.stdout:
            msg = "Policy execution failed. Check sudo password or connection."
            log_action(policy_file, "FAILED", msg)

        elif "changed=1" in result.stdout or "changed=2" in result.stdout:
            msg = "Policy enforced! Apache was successfully restarted."
            log_action(policy_file, "REMEDIATED", msg)
        else:
            msg = "Policy healthy. No changes needed."
            log_action(policy_file, "SUCCESS", msg)
            
    except Exception as e:
        log_action(policy_file, "ERROR", str(e))

# Example: Running specific policies in a loop
# Path to the shared state file
STATES_FILE = os.path.join(BASE_DIR, "data", "policy_states.json")

if __name__ == "__main__":
    while True:
        try:
            # 1. Read what the Admin has toggled on the Dashboard
            with open(STATES_FILE, 'r') as f:
                active_states = json.load(f)

            print(f"\n--- [{time.ctime()}] Policy Scan Starting ---")

            # 2. Iterate through the policies
            for policy_name, is_active in active_states.items():
                if is_active:
                    # Only run Ansible if the Dashboard button is GRE>
                    print(f"[ACTIVE] Enforcing: {policy_name}")
                    enforce_policy(policy_name)
                else:
                    # Skip if the Dashboard button is RED (False)
                    print(f"[DISABLED] Skipping: {policy_name}")

            print("--- Scan Complete. Waiting 60 seconds... ---")
        except Exception as e:
            print(f"Error reading states: {e}")

        time.sleep(60)

