# Portfolio Website - [Abhishek Pednekar](https://AbhishekPednekar.com)

[![Build Status](https://travis-ci.org/AbhishekPednekar84/personal-portfolio.svg?branch=master)](https://travis-ci.org/AbhishekPednekar84/personal-portfolio) [![Coverage Status](https://coveralls.io/repos/github/AbhishekPednekar84/personal-portfolio/badge.svg?branch=master)](https://coveralls.io/github/AbhishekPednekar84/personal-portfolio?branch=master)

This is my personal portfolio site developed using Flask and Sass with a little bit of jQuery. Base layout credits go to [Traversy Media](https://TraversyMedia.com).

## Steps to run a local setup

1. Clone the repository - `git clone https://github.com/AbhishekPednekar84/personal-portfolio`
2. Create and activate a virtual rnvironment
3. Install dependencies - `python -m pip install -r requirements.txt`
4. Create a **.env** file (refer to the **.env.example** file) containing the Flask `SECRET_KEY`, `SQLALCHEMY_DATABASE_URI`, `EMAIL_USER`, `EMAIL_PASS`, `EMAIL_RECIPIENT` and `CELERY_BROKER_URL` values.
5. To discover and run unit tests - `python -m unittest discover tests`
6. To evaluate code coverage - `coverage run -m tests.test_app`
7. To run a coverage report - `coverage report -m`
8. To run the application - `python app.py`
9. To run the browser automation tests (on Chrome) - Install the latest Chrome webdriver and run `python -m browser_automation.automation_tests.py`

Note: Remember to `omit` your virtual environment directory in **.coveragerc** before running `coverage report -m`
