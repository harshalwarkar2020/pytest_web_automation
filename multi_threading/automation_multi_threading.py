import time
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def selenium_task(thread_num):
    service = Service(executable_path=r'C:\Users\harshalashok_warkar\study_codes\bdd_demo\drivers\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.example.com")
    time.sleep(8)
    print(f"Thread {thread_num}: {driver.title}")
    driver.quit()


num_threads = 4

# Create a list to hold thread objects
threads = []

# Create and start the threads
for i in range(num_threads):
    thread = threading.Thread(target=selenium_task, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads have finished.")
