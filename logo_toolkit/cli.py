import argparse
import sys
import os
from .fetcher import fetch_logo_clearbit, scrape_logo_web
from .utils import create_folder
from .resizer import resize_image

def main():
    print(sys.path)  # For debugging; remove if not needed

    parser = argparse.ArgumentParser(description="Fetch and resize logos.")
    parser.add_argument('--input', type=str, required=True, help='Path to the input file with tool names.')
    parser.add_argument('--output', type=str, required=True, help='Path to the output folder for logos.')

    args = parser.parse_args()
    create_folder(args.output)

    with open(args.input, 'r') as file:
        tool_names = [line.strip() for line in file.readlines()]

    for tool in tool_names:
        print(f"Fetching logo for '{tool}'...")

        logo_path = os.path.join(args.output, f"{tool}.png")
        resized_logo_path = os.path.join(args.output, f"{tool}_resized.png")

        # Attempt to fetch logo using Clearbit first
        if fetch_logo_clearbit(tool, args.output):
            try:
                if os.path.exists(logo_path):
                    resize_image(logo_path, resized_logo_path)
                    print(f"Logo for '{tool}' fetched and resized successfully via Clearbit.")
                else:
                    print(f"Logo for '{tool}' not found at '{logo_path}'. Skipping resizing.")
                continue
            except Exception as e:
                print(f"Error resizing image for '{tool}': {e}")

        # Fallback to web scraping if Clearbit fails
        if scrape_logo_web(tool, args.output):
            try:
                if os.path.exists(logo_path):
                    resize_image(logo_path, resized_logo_path)
                    print(f"Logo for '{tool}' fetched and resized successfully from web scraping.")
                else:
                    print(f"Logo for '{tool}' not found at '{logo_path}'. Skipping resizing.")
                continue
            except Exception as e:
                print(f"Error resizing image for '{tool}': {e}")

        print(f"Failed to fetch logo for '{tool}' after all methods.")

if __name__ == "__main__":
    main()

