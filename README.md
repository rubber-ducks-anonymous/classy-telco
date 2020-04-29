# Telco Churn Classification Project

## Description

This project aims to answer why the customers churn for the telco company. This will be done through a jupyter notebook report that will explore the different features that are affecting churn. We will also be creating predictive model that tells both the likelyhood that a customer will churn and whether or not the customer will churn. We will also be making a presentation that walks through how the model works. Finally, we will have python files that contain functions that will deliver future data to our model in the same form that we have trained the model to receive.

## Goals

- [X] Notebook with report of the findings
- [x] `.csv` file with predictions
- [x] `.py` files:
    - [x] acquire.py 
    - [x] prepare.py
- [x] Presentation
- [x] Completed README

## How to Reproduce

### First clone this repo

### acquire.py 

* Must include `env.py` file in directory.
    * Contact [Codeup](https://codeup.com/contact/) to request access to the MySQL Server that the data is stored on.
    * `env.py` should include the following variables
        * `user` - should be your username
        * `password` - your password
        * `host` - the host address for the MySQL Server

* As long as you have the env file then `get_telco_data()` will do the rest on it's own.

### prep.py
* `prep_telco_data()` will split, clean, and encode the data for the preparation stage.

* `prep_all_data()` will clean and encode a dataframe for using in modeling

### telco_churn_report.ipynb

* This contains the report of what is causing churn and a walkthrough of the pipeline to creating a model to predict whether a customer will churn.

## Planning
- [x] Acquire
    - [x] acquire.py
        - [x] Get data from `MySQL`: `telco_churn`: `customers`
        - [x] Determine which tables join on
        - [x] Make function to acquire data into a `pd.DataFrame`
    - [x] Notebook
        - [x] Demonstrate acquire.py
        - [x] Summarize data
        - [x] Plot Distributions
- [x] Prepare
    - [x] prepare.py
        - [x] Split data
        - [x] Handle Missing Values
            - [x] Handle datatype issues
        - [x] Encode strings
        - [ ] Scale data
        - [x] Add new feature `tenure_years`
        - [ ] Create feature that combines `phone_service` and `multiple_lines`
        - [ ] Create feature that combines `dependents` and `partner`
        - [ ] Look into merging other variables
            - [ ] ` streaming_tv` and `streaming_movies`
            - [ ] `online_security` and `online_backup`
    - [x] Notebook
        - [x] Explore missing values and document takeaways/action plans for handling them.
        - [x] Document takeaways
        - [x] Explore datatypes
            - [x] Adapt types or data values as needed to have numeric representation of each attribute.
        - [x] Demonstrate prepare.py works by running it
- [x] Exploration
    - [ ] Answer key questions
- [ ] Feature Engineering
- [x] Modeling
    - [x] Notebook

## Data Dictionary

| Columns | Definition |
|:--------|-----------:|
|  customer_id | customer number  |
| gender  | gender identity |
| senior_citizen  | 0 = senior citizen, 1 = not senior citizen  |
| partner  | undefined  |
| dependents  | undefined  |
| tenure  | total months as customer  |
| phone_service  | yes, no = phone service  |
| multiple_lines  | yes, no, not phone service  |
| internet_service_type_id  | no, yes, no internet serivice  |
| online_security  | yes = subscribed, no = not subcribed, or no internet service |
| online_backup  | yes = subscribed, no = not subcribed, or no internet service  |
| device_protection  | yes = subscribed, no = not subcribed, or no internet service  |
| tech_support   | yes = subscribed, no = not subcribed, or no internet service  |
| streaming_tv   | yes = subscribed, no = not subcribed, or no internet service  |
| streaming_movies  | yes = subscribed, no = not subcribed, or no internet service  |
| contract_type_id  | refers to contract type  |
| paperless_billing  | no = sent by mail, yes = electronic notification  |
| payment_type_id  | id of method of payment  |
| monthly_charges  | current monthly charge |
| total_charges  | total charges since becoming a customer  |
| churn  | yes = no longer a customer, no = still a customer  |
| contract_type  | Month-to-month, Two year. One year  |
| internet_service_type | None, DSL, Fiber optic  |
| payment_type | method of payment |