# Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit

**Objective of the Project:**

  The "Redbus Data Scraping and Filtering with Streamlit Application" aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.

**Approach:**

Data Scraping: 
Use Selenium to automate the extraction of Redbus data including routes, schedules, prices, and seat availability.

Data Storage: 
Store the scraped data in a SQL database.

Streamlit Application: 
Develop a Streamlit application to display and filter the scraped data.
Implement various filters for example bustype, route, price range, star rating, availability.

Data Analysis/Filtering using Streamlit:
Use SQL queries to retrieve and filter data based on user inputs.
Use Streamlit to allow users to interact with and filter the data through the application.

**Technologies used :**

1. MySQL
2. Python
3. Selenium
4. Streamlit

**Process :**
1. Retrieving Data from Redbus website using Selenium
2. Data Cleaning using Pandas
3. Data Storage by connecting Python and MySQL
4. App created using Streamlit in order to view the data

**Libraries Used :**

* from selenium import webdriver
* from selenium.webdriver import ActionChains
* from selenium.webdriver.common.by import By
* from selenium.webdriver.common.keys import Keys
* from selenium.common.exceptions import TimeoutException, NoSuchElementException
* import time
* from selenium.webdriver.support.ui import WebDriverWait
* from selenium.webdriver.support import expected_conditions as EC
* import pandas as pd
* import numpy as np
* import pymysql
* from tabulate import tabulate
* import streamlit as st
* from streamlit_option_menu import option_menu
* import plotly.express as px 
