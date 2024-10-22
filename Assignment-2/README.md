## Running The Project 
### Steps modified from example [repository](https://github.com/anwardr/Cisc327-F24/blob/343c0f056c658d28d902f44da12618a731def3ce/how-to-run.md).

1. Make sure you are in the root directory of the project.
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
5. Run the following command to start the server:

    ```bash
    python app.py
    ```
6. Follow the link from the output (or copy-paste into your browser).
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

## Notes
Some smaller screens have trouble displaying a few of the web pages. If that is happening, please try to zoom out or in, in an attempt to fix the visual issues.

As of now, we have no backend functionality and all data has been mock-implemented to provide a full frontend look.
