### **Commands and Steps Followed**

This document provides an overview of the commands and actions taken during the setup and execution of the project.

---

#### **1. Setting Up the Python Environment**

To ensure project dependencies are isolated, the following commands were used to create and activate a virtual environment:

- **Creating a Python Environment:**
  ```
  python -m venv my_s3load_env
  ```

- **Activating the Environment:**
  ```
  my_s3load_env\Scripts\activate.bat
  ```

---

#### **2. Installing Required Dependencies**

Once the environment was activated, the following dependencies were installed using the **pip** command:

- **AWS CLI:**  
  AWS CLI was installed to interact with AWS services through the command line.
  ```
  pip install awscli
  ```

- **Boto3:**  
  Boto3 was installed to enable interaction with AWS services such as S3 directly from Python code.
  ```
  pip install boto3
  ```

- **Requests:**  
  Requests was installed to facilitate making HTTP requests to external APIs.
  ```
  pip install requests
  ```

---

#### **3. Running Test Files**

Test files were created and executed to ensure that the AWS connection was properly set up, and that the API call functioned as expected:

- **Boto3 Import Test:**
  A test file (`boto3_import_test.py`) was run to confirm that **Boto3** was imported successfully and the AWS connection was functional.
  ```
  python boto3_import_test.py
  ```

- **API Call Test:**
  A test file (`api_call_test.py`) was executed to verify the API call functionality and check if data could be retrieved successfully.
  ```
  python api_call_test.py
  ```

---

#### **4. S3 Bucket Creation and Data Upload**

Once the tests were successful, the following steps were performed to create an S3 bucket and upload data to it:

- **S3 Bucket Creation:**
  A script (`create_bucket.py`) was run to create an S3 bucket within the AWS account.
  ```
  python create_bucket.py
  ```

- **Uploading Data to S3:**
  Data was uploaded to the created S3 bucket using the script (`put_object_in_s3.py`).
  ```
  python put_object_in_s3.py
  ```
