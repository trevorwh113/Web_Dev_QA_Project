## Disclaimers
Some smaller screens have trouble displaying a few of the web pages. If that is happening, please try to zoom out or in, in an attempt to fix the visual issues.

Backend functionality is now implemented and as such, there may be longer load times for the pages as it is fetching that data from the cloud.


## Running The Project 

1. Make sure you are in the root directory of the project (Web_Dev_QA_Project).
2. In the root directory, create a virtual environment by running the following command:
    ```bash
    python3 -m venv venv
    ```
    Here the second `venv` is the name of the virtual environment. You can use any name you want.
3. Activate the virtual environment by running the following command:
    ```bash
    source venv/bin/activate 
    ```
    If you are using Windows, you can activate the virtual environment by running the following command:
    ```bash
    venv\Scripts\activate
    ```
4. Install the required packages for the project by running the following command:
    ```bash
    pip install -r requirements.txt
    ```
5. Change your directory to Web_Dev_QA_Project/app using cd.
6. Run the following command to start the server:
    ```bash
    python app.py
    ```
7. This hosts the webpage in the localhost. Follow the link from the output (or copy-paste into your browser).

## Running The Tests 
1. Follow the instructions listed in **Running The Project**, but stop before launching the app (steps 1-5).
2. Run the following command to run **all** tests:
     ```bash
    pytest 
    ```
3. To choose specific test files, run the following command:
     ```bash
    pytest test_name.py
    ```
   where test_name is the name of the test file. Or, use one of the three following commands to target our sub-directories of tests:
     ```bash
    pytest tests/unit
    pytest tests/integration
    pytest tests/end-to-end
    ```
**For End-To-End Tests:** These tests use the Playwright tool and require the app to be running in the
localhost.
1. Ensure Playwright is installed:    
    ```bash
    pip install -r requirements.txt 
    ```
2. Run the following command to complete installation of the browsers:
    ```bash
    playwright install
    ```
3. Make sure `app.py` is running so that Playwright can simulate user interactions. If it is not, run this command once again:
     ```bash
    python app.py
    ```
    Then, in a second terminal (with an activated venv), execute the following to run just the End-To-End Tests
     ```bash
    pytest tests/end-to-end
    ```
    or, now that app.py is running, you can run all tests together with:
     ```bash
    pytest
    ```

## Generating Code Coverage Reports
1. Make sure to have updated your venv using the requirements.txt file
     ```bash
    pip install -r requirements.txt
    ```
2. Run the tests again through this command:
     ```bash
    coverage run -m pytest
    ```
3. Then, to generate a coverage report, run the following command:
     ```bash
    coverage report
    ```
    OR, if you wish to view the report in the browser, and with more detail, run
     ```bash
    coverage html
    ```
   and open `./htmlcov/index.html` in your browser.
   
4. To view the reports that we ran, and that are referenced in `Assignment-4.pdf` open `Assignment-4/initial_coverage/index.hmtl` and `Assignment-4/updated_coverage/index.html` within our github directory.

## Test Suite Breakdown
### Unit Tests
`test_client_by_name.py`    `test_client_filter.py` `test_drug_filter.py`

`test_valid_input.py`   `test_get_set_prescriptions.py` `test_valid_drug.py`

`test_save_new_prescription.py` `test_update_list.py`   `test_misc_pages.py`

### Integration Tests
`test_client_lookup.py` `test_drug_lookup.py`   `test_view_prescriptions.py`

`test_prescription_creation.py` `test_prescription_num.py`  `test_submit_num.py`

### End-To-End Tests
`test_user_change_status.py`    `test_user_create_prescription.py`

`test_user_drug_client_search.py`   `test_user_navigation.py`
