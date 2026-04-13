import datetime

EMERGENCY_CONTACT = "rishavkumar221188@gmail.com"
YOUR_NAME = "Rishav Singh"

def log_alert():
    with open("alert_log.txt", "a") as f:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{time}] SOS triggered by {YOUR_NAME}\n")
    print("Alert saved to log file!")

def sos_alert():
    print("\n*** SOS ALERT TRIGGERED ***")
    print(f"Name: {YOUR_NAME}")
    print(f"Emergency Contact: {EMERGENCY_CONTACT}")
    print("Please call emergency services: 112")
    log_alert()

def show_tips():
    print("\n--- Safety Tips ---")
    print("1. Stay in well-lit areas")
    print("2. Share your location with trusted contacts")
    print("3. Keep emergency numbers saved")
    print("4. Trust your instincts")

def main():
    print("==========================")
    print(" WOMEN SAFETY ALERT SYSTEM")
    print("==========================")
    
    while True:
        print("\n1. Trigger SOS Alert")
        print("2. View Safety Tips")
        print("3. Exit")
        
        choice = input("\nEnter choice (1/2/3): ").strip()
        
        if choice == "1":
            sos_alert()
        elif choice == "2":
            show_tips()
        elif choice == "3":
            print("Stay safe!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
