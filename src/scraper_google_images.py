from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import requests
from urllib.parse import quote

# -------- CONFIG --------
search_keywords = ["wearing helmet in road india traffic", "bike without helmet india", "traffic red lights in indian roads from cctv"]
num_images_per_class = 100
save_dir = "data/raw"
scrolls_per_keyword = 6
wait_time = 2
# ------------------------

def create_folders(keywords):
    """
    Create folders for saving images.
    Example: data/raw/bike_with_helmet/
    """
    for keyword in keywords:
        folder_path = os.path.join(save_dir, keyword.replace(" ", "_"))
        os.makedirs(folder_path, exist_ok=True)

def download_images(images, folder_path, keyword, engine_name, limit):
    """
    Download image URLs and save them into the respective folder.
    """
    count = 0
    for img in images:
        if count >= limit:
            break
        try:
            img_url = img.get_attribute("src")
            if img_url is None or not img_url.startswith("http"):
                continue
            img_data = requests.get(img_url, timeout=5).content
            file_path = os.path.join(folder_path, f"{engine_name}_{keyword.replace(' ','_')}_{count+1}.jpg")
            with open(file_path, "wb") as f:
                f.write(img_data)
            count += 1
        except Exception as e:
            print(f"⚠️ Error downloading image: {e}")
    print(f"✅ Saved {count} images from {engine_name} into {folder_path}")


def scrape_google(driver, keywords):
    print("\n=== Starting Google Scraping ===")

    for keyword in keywords:
        print(f"\n🔍 [Google] Scraping for: {keyword}")
        url = f"https://www.google.com/search?tbm=isch&q={quote(keyword)}"
        driver.get(url)
        time.sleep(wait_time)

        # Scroll to load more
        body = driver.find_element(By.TAG_NAME, "body")
        for _ in range(scrolls_per_keyword):
            body.send_keys(Keys.END)
            time.sleep(wait_time)

        images = driver.find_elements(By.TAG_NAME, "img")
        print(f"Found {len(images)} img tags for '{keyword}'")

        folder_path = os.path.join(save_dir, keyword.replace(" ", "_"))
        download_images(images, folder_path, keyword, "google", num_images_per_class)


def scrape_bing(driver, keywords):
    print("\n=== Starting Bing Scraping ===")

    for keyword in keywords:
        print(f"\n🔍 [Bing] Scraping for: {keyword}")
        url = f"https://www.bing.com/images/search?q={quote(keyword)}"
        driver.get(url)
        time.sleep(wait_time)

        # Scroll to load more
        body = driver.find_element(By.TAG_NAME, "body")
        for _ in range(scrolls_per_keyword):
            body.send_keys(Keys.END)
            time.sleep(wait_time)

        images = driver.find_elements(By.CSS_SELECTOR, "img.mimg")
        print(f"Found {len(images)} images for '{keyword}'")

        folder_path = os.path.join(save_dir, keyword.replace(" ", "_"))
        download_images(images, folder_path, keyword, "bing", num_images_per_class)


# 1️⃣ Start Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Uncomment for headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 2️⃣ Create class folders once
create_folders(search_keywords)

# 3️⃣ Run both scrapers (both save into the same folder)
scrape_google(driver, search_keywords)
scrape_bing(driver, search_keywords)

driver.quit()
print("\nScraping completed! Google + Bing images are saved together in 'data/raw/'")
