## Running The Project 
### Steps modified from example [repository](https://github.com/anwardr/Cisc327-F24/blob/343c0f056c658d28d902f44da12618a731def3ce/how-to-run.md).

1. Make sure you are in the root directory of the project (Group-8-FS).
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
4. Install the required packages by running the following command. This is updated for our project (includes pytest).:

    ```bash
    pip install -r requirements.txt
    ```
5. Change your directory to Group-8-FS/app using cd.
6. Run the following command to start the server:

    ```bash
    python app.py
    ```
7. Follow the link from the output (or copy-paste into your browser).
## Running The Tests 
1. After following steps for **Running The Project**, terminate the execution of app.py but keep the virtual machine active.

2. Run the following command to run **all** tests:
     ```bash
    pytest 
    ```
3. To choose specific test files, run the following command:
     ```bash
    pytest test_name.py
    ```
   where test_name is the name of the test file.
4. PERTAINING TO ASSIGNMENT 5: In the case of `verify_navigation.py`, one of our tests uses the playwright tool, so you must also install its browsers.

    a. Install playwright with this command:    
    ```bash
    pip install -r requirements.txt 
    ```

    b. Run the following command to complete installation:
    ```bash
    playwright install
    ```

    c. Since this test works only on a unix/linux machine, it does not have the prefix of test_, and thus must be specified manually. First navigate to the `/tests`, then run  this command:
     ```bash
    pytest verify_navigation.py
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

## File Suite(s) Breakdown
### Unit Tests
`test_client_by_name.py`

`test_client_filter.py`

`test_drug_filter.py`

`test_valid_input.py`

`test_get_set_prescriptions.py`

`test_valid_drug.py`

`test_save_prescription.py`

`test_update_list.py`

`test_misc_pages.py`

### Functional Tests (related to test cases from A1)
`test_client_lookup.py`

`test_drug_lookup.py`

`test_view_prescriptions.py`

`test_prescription_creation.py`

### Integration Tests (for A5)
`test_prescription_num.py`

`test_submit_num.py`

`verify_navigation.py`

## Notes
Some smaller screens have trouble displaying a few of the web pages. If that is happening, please try to zoom out or in, in an attempt to fix the visual issues.

Backend functionality is now implemented and as such, there may be longer load times for the pages as it is fetching that data from the cloud.
