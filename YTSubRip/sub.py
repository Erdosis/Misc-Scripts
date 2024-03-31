import webbrowser
import time
import random

BATCH_SIZE = 10
FILE_PATH = 'channel_list.txt'

def open_urls_in_batches(file_path, batch_size):
    with open(file_path, 'r', encoding='utf-8') as file:
        urls = file.readlines()


    for url_index in range(0, len(urls), batch_size):
        batch = urls[url_index:url_index+batch_size]
        print(f"Opening batch {url_index//batch_size + 1}/{(len(urls) + batch_size - 1)//batch_size}...")

        for url in batch: 
            # Random sleep to avoid bot detection
            sleep_duration = random.uniform(1,3)
            time.sleep(sleep_duration/2)

            webbrowser.open(url.strip())

        input("Press Enter to continue to the next batch...")

if __name__ == "__main__": 
    open_urls_in_batches(FILE_PATH, BATCH_SIZE)