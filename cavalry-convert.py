import os
import sys
import json

# --- Coolors palette data
coolor_code = {"Punch Red":"e63946","Honeydew":"f1faee","Frosted Blue":"a8dadc"}

palette_name = "Summer Ocean Breeze".lower()

# --- Convert Coolor palette to Cavalry format
def convert_to_cavalry(input_colors, palette_name):
    cavalry_colors = []
    for name, hex_code in input_colors.items():
        formatted_hex = f"#{hex_code}"
        cavalry_colors.append({"color": formatted_hex, "swatchName": name})

    title_case_name = palette_name.title()

    output_data = {"colors": cavalry_colors, "designer": "Coolors", "name": title_case_name, "version": 1.0}

    filename = f"{palette_name}.pal"
    
    # --- Check if file exists
    if os.path.exists(filename):
        response = input(f"Warning: '{filename}' already exists. Overwrite? (y/N): ").strip().lower()
        if response != 'y':
            print("Operation cancelled.")
            sys.exit()
        else:
            print(f"Overwriting '{filename}'...")
    else:
        print(f"Creating new file '{filename}'...")
            
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4)
        
    print(f"Success! Saved '{filename}'!")

convert_to_cavalry(coolor_code, palette_name)