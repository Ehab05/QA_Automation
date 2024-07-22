# QA_Automation
API Testing Project
Overview
This project is an API testing suite developed to interact with the FakeRestAPI. It performs CRUD operations on the API endpoints for activities, authors, and books, using Python and associated libraries.

Features
CRUD Operations: Create, Read, Update, and Delete operations for Activities, Authors, and Books.
Data Generation: Random data generation for testing purposes.
Configurable Endpoints: Endpoints and configurations are specified in a JSON configuration file.
Logging: Logs API interactions and results.
Technologies Used
Python: Programming language used.
Requests: For making HTTP requests.
Pytest: For running tests and assertions.
Postman: For manual API testing and validation.
Pytz: For handling time zones and datetime operations.
Installation:

Clone the repository:
git clone <repository_url>
cd <repository_directory>

Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:
pip install -r requirements.txt

Ensure the configuration file is in place:
Place the fake_rest_config.json file in the appropriate directory (../../fake_rest_config.json).

Usage
Running Tests
Run Tests with Pytest:
pytest
This will execute all tests defined in the tests directory.

Example Endpoints
Activities Endpoint: /Activities
Authors Endpoint: /Authors
Books Endpoint: /Books

Configuration:
Configuration for API endpoints and other parameters are specified in the fake_rest_config.json file. Ensure this file contains the correct base URL and any other relevant configuration parameters.

Testing:
The testing suite includes various test cases to ensure the correctness of API interactions. The tests are organized into categories such as:
Get Operations
Post Operations
Put Operations
Delete Operations

Contact
For any questions or feedback, please contact:

Name: Ehab Khalil
Email: ehabkalil5@gmail.com

Acknowledgements
FakeRestAPI: For providing the API to test.
Python Libraries: Requests, Pytest, Pytz.

