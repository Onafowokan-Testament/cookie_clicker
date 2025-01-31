# Automated Web Interactions with Selenium 🤖

Welcome to the **Automated Web Interactions** project! This project demonstrates how to automate web interactions using **Selenium**, a powerful tool for browser automation. The scripts provided automate tasks such as clicking buttons, navigating websites, and extracting data. These examples can be adapted for various use cases, including web scraping, testing, and repetitive task automation.

---

## Features

- **Cookie Clicker Automation**: Automates clicking the "big cookie" and purchasing upgrades in the popular game [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/).
- **Wikipedia Search**: Automates searching for a term on Wikipedia.
- **Python.org Event Extraction**: Extracts event details (date and name) from the [Python.org events page](https://www.python.org/).

---

## How It Works

1. **Cookie Clicker Automation**:
   - Opens the Cookie Clicker game.
   - Continuously clicks the "big cookie" using a separate thread.
   - Purchases upgrades and products automatically.

2. **Wikipedia Search**:
   - Opens Wikipedia's main page.
   - Searches for a specified term (e.g., "python") and navigates to the search results.

3. **Python.org Event Extraction**:
   - Opens the Python.org events page.
   - Extracts the date and name of the first 5 upcoming events and stores them in a dictionary.

---

## Installation

To run these scripts locally, follow these steps:

### Prerequisites

- Python 3.8 or higher
- Selenium
- ChromeDriver (matching your Chrome browser version)

### Steps

1. **Install Selenium**:
   ```bash
   pip install selenium
   ```

2. **Download ChromeDriver**:
   - Download the appropriate version of ChromeDriver from [here](https://sites.google.com/chromium.org/driver/).
   - Ensure the ChromeDriver executable is in your system's PATH or specify its location in the script.

3. **Run the Scripts**:
   - Save the scripts to `.py` files and run them using Python:
     ```bash
     python script_name.py
     ```

---

## Scripts

### 1. Cookie Clicker Automation
Automates the Cookie Clicker game by clicking the "big cookie" and purchasing upgrades.

### 2. Wikipedia Search
Automates searching for a term on Wikipedia and navigating to the search results.

### 3. Python.org Event Extraction
Extracts event details (date and name) from the Python.org events page.

---

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Selenium](https://www.selenium.dev/) for browser automation.
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) for enabling Chrome automation.

---

Automate web interactions with ease using this project! 🚀🤖
