import os
from PIL import Image
from pyzbar.pyzbar import decode

def scan_qr_bomb(directory_path):
    """
    Automated script to iterate through 3,000 QR codes and filter for 
    strings containing the 'Gdg' flag prefix.
    """
    
    # Check if directory exists
    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' not found.")
        return

    print(f"Starting scan in: {directory_path}...")
    found_count = 0

    # Loop through every file in the folder
    for filename in sorted(os.listdir(directory_path)):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            file_path = os.path.join(directory_path, filename)
            
            try:
                # Load the image
                img = Image.open(file_path)
                
                # Use pyzbar to decode the QR content
                # Note: This is where the 'libzbar' dependency is required
                decoded_objects = decode(img)
                
                for obj in decoded_objects:
                    qr_content = obj.data.decode('utf-8')
                    
                    # Filter for the flag format
                    if "Gdg" in qr_content:
                        print(f"\n[!] FLAG FRAGMENT FOUND in {filename}: {qr_content}")
                        found_count += 1
                        
            except Exception as e:
                # Log the error (Matches the 'Roadblock' in the writeup)
                print(f"Could not process {filename}: {e}")
                continue

    print(f"\nScan complete. Fragments found: {found_count}")

if __name__ == "__main__":
    # Point this to the extracted folder from Task 1 Level 3
    target_folder = "./qr_codes" 
    scan_qr_bomb(target_folder)
