# Automated Login Testing for Multiple Websites

This project is designed to automate the process of testing login functionality for multiple websites. The main goal is to ensure that the login feature works as expected across different platforms.

## Project Structure

```
.
├── tests
│   ├── __init__.py
│   ├── test_login.py
├── config
│   ├── __init__.py
│   ├── settings.py
├── utils
│   ├── __init__.py
│   ├── browser.py
│   ├── logger.py
├── requirements.txt
├── README.md
```

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/automated-login-testing.git
    cd automated-login-testing
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Update the `config/settings.py` file with the necessary configuration details for the websites you want to test.

## Running Tests

To run the tests, use the following command:
```sh
pytest
```

### Using Pytest

`pytest` is a framework that makes building simple and scalable test cases easy. It is used to run the tests in this project.

1. **Install Pytest**:
   Ensure `pytest` is listed in your `requirements.txt` and has been installed via `pip install -r requirements.txt`.

2. **Run Tests**:
   To run all tests in the `tests` directory, simply execute:
   ```sh
   pytest
   ```

3. **Test Report**:
   Pytest provides detailed information about which tests passed or failed, along with error tracebacks.

4. **Running Specific Tests**:
   You can run specific tests by specifying the file or test name:
   ```sh
   pytest tests/test_login.py
   ```

5. **Verbose Output**:
   For more detailed output, use the `-v` option:
   ```sh
   pytest -v
   ```

6. **Generate HTML Report**:
   To generate an HTML report of the test results, you can use the `pytest-html` plugin:
   ```sh
   pip install pytest-html
   pytest --html=report.html
   ```

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

This project is licensed under the MIT License.