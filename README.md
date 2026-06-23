# FUCKINSTA

A powerful tool designed to mass-report Instagram accounts using rotating proxies to trigger bans or suspensions. Built for maximum impact with multi-threading and anti-detection features.

## Features

- Mass reporting with rotating proxies to simulate reports from different IPs.
- Randomized user agents to mimic different devices and browsers.
- Multi-threaded execution for speed and efficiency.
- Detailed logging of all actions for monitoring success and failures.
- Fully customizable report reasons and attack intensity.

## Setup Instructions

1. **Install Python**:
   - Download and install Python (3.8 or higher) from [python.org](https://www.python.org/downloads/).

2. **Clone this Repository**:
   - Clone or download this repo to your local machine.
   ```bash
   git clone https://github.com/yourusername/FUCKINSTA.git
   cd deathtrend-
   ```

3. **Install Dependencies**:
   - Install the required libraries using pip.
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare Proxies**:
   - Add a list of proxies to `proxies/proxies.txt` in the format `ip:port` (one per line).
   - You can scrape free proxies from sites like `free-proxy-list.net` or purchase premium proxies for better reliability.

5. **Customize the Tool**:
   - Open `src/fuckinsta.py` and replace `target_username_here` with the Instagram username of your target.
   - Adjust `REPORT_REASON`, `REPORT_COUNT_PER_PROXY`, and `DELAY_BETWEEN_REPORTS` as needed for your attack strategy.

6. **Find Target User ID (Optional but Recommended)**:
   - Instagram often requires a user ID for reporting. Use tools like `lookup-id.com` to find the user ID of the target account.
   - Replace the placeholder `user_id` in the script with the real ID for better results.

## Usage

Run the tool from the command line:

```bash
cd src
python fuckinsta.py
```

Or from the project root:

```bash
python src/fuckinsta.py
```

- Monitor the console output and check `logs/report_logs.txt` for detailed logs of the attack.

## Tips for Maximum Impact

- Use a large number of fresh, working proxies to make reports appear from different locations.
- Spread reports over time by increasing `DELAY_BETWEEN_REPORTS` if you get rate-limited.
- Test with a small number of reports first to ensure everything works before scaling up.

## Disclaimer

This tool is for educational purposes and testing on accounts you own or have permission to target. Use at your own risk.

## Contributing

Feel free to fork this repo, make improvements, and submit pull requests. Let's make this tool even more brutal together!

## Contact

Got questions or need tweaks? Open an issue or hit me up on GitHub.
