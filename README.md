# API Test Automation - Pytest

This project contains an automated test script using **pytest** to validate API responses from `https://api.tmsandbox.co.nz`.

## 📌 Prerequisites

Ensure you have the following installed before running the tests:

1. **Python** (>=3.7 recommended)
2. **pip** (Python package manager)

## 📌 Setup Instructions

### 🔹 Step 1: Clone or Download the Repository and switch to main branch

```bash
git clone https://github.com/jaliyasu/AssurityTest.git
git checkout main
cd AssurityTest
```

### 🔹 Step 2: Install Required Dependencies
```bash
pip install -r requirements.txt
```


# 📌 Running the Tests

### 🔹 Run the Test Script
Navigate to the **test_script** folder containing `api_test_catagory.py` and execute:

```bash
cd test_script
pytest api_test_category.py
```

### 🔹 Run with Detailed Output
For more details on test execution:
```bash
pytest -v api_test_category.py
```

### 🔹 Run and Generate HTML Report
To generate an **HTML test report**, use:
```bash
pytest api_test_category.py --html=report.html --self-contained-html
```
After execution, open **`report.html`** in a browser to view the results.


## 📌 Understanding Test Assertions
The test script validates:
1. **API Response Status** - Ensures the API call returns a **200 OK** status.
2. **Category Name Validation** - Checks if `"Name"` is `"Carbon credits"`.
3. **CanRelist Attribute** - Ensures `"CanRelist"` is `True`.
4. **Promotion Validation** - Checks if the `"Gallery"` promotion **exists** and its `"Description"` contains `"Good position in category"`.




