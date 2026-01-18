import os
from PIL import Image
from pyzbar.pyzbar import decode

def scan_qr_bomb(directory_path):
    """
    Iterates through the extracted QR codes in Task 1A: Level 3 
    to filter for strings containing the 'Gdg' flag prefix.
    """
    
    # Verify the directory path exists
    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' not found.")
        return

    print(f"Starting automated scan in: {directory_path}...")
    found_count = 0

    # Iterate through every image file in the specified folder
    for filename in sorted(os.listdir(directory_path)):
        if filename.endswith(".png"):
            file_path = os.path.join(directory_path, filename)
            
            try:
                # Open the image file
                img = Image.open(file_path)
                
                # Decode the QR code content
                # Note: This requires the 'pyzbar' and 'Pillow' libraries
                decoded_objects = decode(img)
                
                for obj in decoded_objects:
                    qr_content = obj.data.decode('utf-8')
                    
                    # Filter for the known flag fragment format
                    if "Gdg" in qr_content or "_" in qr_content:
                        print(f"\n[!] MATCH FOUND in {filename}: {qr_content}")
                        found_count += 1
                        
            except Exception as e:
                # Skips files that cannot be processed due to environment errors
                continue

    print(f"\nScan complete. Total fragments located: {found_count}")

if __name__ == "__main__":
    target_folder = "./cybersec-recruitments/gdg_part3/qr_code_zipbomb/qr_code_zipbomb"
    scan_qr_bomb(target_folder)
