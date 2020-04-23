# Telco Churn Classification Project

## Description

This project aims to answer why the customers churn for the telco company. This will be done through a jupyter notebook report that will explore the different features that are affecting churn. We will also be creating predictive model that tells both the likelyhood that a customer will churn and whether or not the customer will churn. We will also be making a presentation that walks through how the model works. Finally, we will have python files that contain functions that will deliver future data to our model in the same form that we have trained the model to receive.

## Goals

- [ ] Notebook with report of the findings
- [ ] `.csv` file with predictions
- [ ] `.py` files:
    - [x] acquire.py 
    - [ ] prepare.py
    - [ ] model.py
- [ ] Presentation
- [ ] Completed README

## How to Reproduce

**In progress**

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
- [ ] Prepare
    - [ ] prepare.py
        - [ ] Ask if data dictionary should include created features
        - [x] Split data
        - [x] Handle Missing Values
            - [ ] Handle datatype issues
        - [ ] Encode strings
        - [ ] Scale data
        - [x] Add new feature `tenure_years`
        - [ ] Create feature that combines `phone_service` and `multiple_lines`
        - [ ] Create feature that combines `dependents` and `partner`
        - [ ] Look into merging other variables
            - [ ] ` streaming_tv` and `streaming_movies`
            - [ ] `online_security` and `online_backup`
    - [ ] Notebook
        - [ ] Explore missing values and document takeaways/action plans for handling them.
        - [ ] Document takeaways
        - [ ] Explore datatypes
        - [ ] Demonstrate prepare.py works by running it
- [ ] Exploration
    - [ ] Answer key questions
- [ ] Feature Engineering
- [ ] Modeling
    - [ ] model.py
    - [ ] Notebook

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