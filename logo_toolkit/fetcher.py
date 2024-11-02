import requests
from bs4 import BeautifulSoup
import re
from .resizer import resize_image

def fetch_logo_clearbit(tool_name, output_folder):
    base_url = "https://logo.clearbit.com/"
    try:
        response = requests.get(f"{base_url}{tool_name}.com", stream=True)
        if response.status_code == 200:
            input_path = f"{output_folder}/{tool_name}.png"
            output_path = f"{output_folder}/{tool_name}_resized.png"
            with open(input_path, 'wb') as logo_file:
                for chunk in response.iter_content(1024):
                    logo_file.write(chunk)
            resize_image(input_path=input_path, output_path=output_path)
            return True
    except Exception as e:
        print(f"Error fetching logo from Clearbit for '{tool_name}': {e}")
    return False

def scrape_logo_web(tool_name, output_folder):
    search_url = f"https://www.google.com/search?q={tool_name}+logo&tbm=isch"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        img_tag = next((img for img in soup.find_all('img') if 'src' in img.attrs and re.match(r'^https?://', img['src'])), None)
        if img_tag:
            img_url = img_tag['src']
            img_data = requests.get(img_url).content
            input_path = f"{output_folder}/{tool_name}.png"
            output_path = f"{output_folder}/{tool_name}_resized.png"
            with open(input_path, 'wb') as file:
                file.write(img_data)
            resize_image(input_path=input_path, output_path=output_path)
            return True
        else:
            print(f"No valid image URL found for '{tool_name}'.")
    except Exception as e:
        print(f"Error scraping logo for '{tool_name}': {e}")
    return False

