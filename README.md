# Behave_Excel_Integration

**Behave BDD with Excel Data-Driven Testing (DDTF)** project using `openpyxl`, targeting [https://www.saucedemo.com](https://www.saucedemo.com):

```markdown
# 🧪 Python BDD Excel DDTF - SauceDemo Login Automation

This project demonstrates a **Data-Driven Testing Framework (DDTF)** using **Python Behave (BDD)** and **Excel integration via openpyxl**. It automates the login functionality on [SauceDemo](https://www.saucedemo.com/) with multiple sets of credentials and writes the test results back into the Excel sheet.

---

## 🚀 Features

- 📊 **Data-Driven Testing (DDT)** via Excel
- ✅ **Behave** for BDD-style test execution
- 🧪 **Selenium WebDriver** for browser automation
- 💾 Results written back to Excel after test execution
- 🔁 Reusable page object structure

---

## 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/behave-excel-saucedemo.git
cd behave-excel-saucedemo
````

2. Set up a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Ensure Google Chrome is installed and compatible with the ChromeDriver.

---

## 📊 Test Data Format (`data/test_data.xlsx`)

| Username          | Password      | Result |
| ----------------- | ------------- | ------ |
| standard\_user    | secret\_sauce |        |
| locked\_out\_user | secret\_sauce |        |
| wrong\_user       | wrong\_pass   |        |

> ✅ Result will be auto-updated after execution.

---

## 🧪 Run the Test

```bash
behave
```

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgments

* [Behave](https://github.com/behave/behave)
* [OpenPyXL](https://openpyxl.readthedocs.io/)
* [SauceDemo](https://www.saucedemo.com/)

---
