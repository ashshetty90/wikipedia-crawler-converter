# wikipedia-crawler-converter #

## Introduction

wikipedia-crawler-converter is a python based application used to crawl web pages and extract specific financial data out of them. This data is then converted to Danish currency for better understanding.


## Getting Started

Before starting up make sure python v2.7 is installed in your machine. Once that is ensured, clone this project in your local repository

## Pre-requisites

Once the project is available in your local environment run the below install commands :
`pip install bs4`\n
`pip install pyyaml`\n
`pip install CurrencyConverter`

## Running Test Cases

The below python test scripts can be run before running the applications : 
`python -m unittest discover -s test -p converter_test.py`\n
`python -m unittest discover -s test -p crawler_test.py`

## Running your App

Once all the test cases have passed run the below command to run the application :

`python app.py`

## Limitations
This application does scrapping only for the Tesla wikipedia page and does only USD to DKK conversion.
