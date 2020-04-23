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
- [ ] Acquire
    - [x] acquire.py
        - [x] Get data from `MySQL`: `telco_churn`: `customers`
        - [x] Determine which tables join on
        - [x] Make function to acquire data into a `pd.DataFrame`
    - [ ] Notebook
        - [ ] Demonstrate acquire.py
        - [ ] Summarize data
        - [ ] Plot Distributions
- [ ] Prepare
    - [ ] prepare.py
        - [ ] Ask if data dictionary should include created features
        - [ ] Split data
        - [ ] Handle Missing Values
            - [ ] Handle datatype issues
        - [ ] Encode strings
        - [ ] Scale data
        - [ ] Add new feature `tenure_years`
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
| --- | --- |
