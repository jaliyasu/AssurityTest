# API Test Automation - Pytest

This project contains an automated test script using **pytest** to validate API responses from `https://api.tmsandbox.co.nz`.

## 📌 Prerequisites

Ensure you have the following installed before running the tests:

1. **Python** (>=3.7 recommended)
2. **pip** (Python package manager)

## 📌 Setup Instructions

### 🔹 Step 1: Clone or Download the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 🔹 Step 2: Install Required Dependencies

Navigate to the directory where `api_test_catagory.py` is located and install the required libraries:

```bash
pip install -r requirements.txt
```
If `requirements.txt` is not available, install manually:
```bash
pip install pytest requests pytest-html
```

## 📌 Running the Tests

### 🔹 Run the Test Script
Navigate to the folder containing `api_test_catagory.py` and execute:
```bash
pytest api_test_catagory.py
```

### 🔹 Run with Detailed Output
For more details on test execution:
```bash
pytest -v api_test_catagory.py
```

### 🔹 Run and Generate HTML Report
To generate an **HTML test report**, use:
```bash
pytest api_test_catagory.py --html=report.html --self-contained-html
```
After execution, open **`report.html`** in a browser to view the results.

### 🔹 Run with Logging Enabled
To log test output into a file:
```bash
pytest api_test_catagory.py > test_results.log
```

## 📌 Understanding Test Assertions
The test script validates:
1. **API Response Status** - Ensures the API call returns a **200 OK** status.
2. **Category Name Validation** - Checks if `"Name"` is `"Carbon credits"`.
3. **CanRelist Attribute** - Ensures `"CanRelist"` is `True`.
4. **Promotion Validation** - Checks if the `"Gallery"` promotion **exists** and its `"Description"` contains `"Good position in category"`.

## 📌 Troubleshooting

### ❌ Issue: `pytest command not found`
🔹 Ensure pytest is installed:
```bash
pip install pytest
```
🔹 Try running with:
```bash
python -m pytest api_test_catagory.py
```

### ❌ Issue: `ModuleNotFoundError: No module named 'requests'`
🔹 Install requests library:
```bash
pip install requests
```

## 📌 Contact
For issues, please reach out via **GitHub Issues** or contact **[Your Name]** at **[Your Email]**.


