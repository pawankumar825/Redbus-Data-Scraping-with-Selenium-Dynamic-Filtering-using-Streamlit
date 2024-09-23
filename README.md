## Project Overview
This project automates the extraction and analysis of bus route data from the Redbus website, utilizing Selenium for web scraping and Streamlit for dynamic data visualization and filtering.

### Files information :
1) Scrapping Routes Using Selenium.ipynb: The first part of the project that extracts data for 10 different bus routes and their corresponding links.

2) Extracting Data using Bus Links.ipynb: The second part that takes the CSV generated from the first part, which includes bus routes and links, and extracts detailed bus data.

3) Redbus_Mysql.ipynb: This notebook stores the entire scraped bus data into a MySQL database for efficient management and querying.

4) Streamlit_Redbus.py: A Streamlit application that allows dynamic filtering and visualization of the bus data.

5) Streamlit App - Redbus Data Analysis1.pdf: Contains screenshots of the Streamlit app for reference and demonstration.

6) all_bus_routes.csv: A CSV file containing bus routes and links for 10 different states.

7) redbus_all_bus_data.csv: A comprehensive CSV file that contains all the scraped bus data.

# Process Workflow :

### 1. Data Scraping
Functionality: A Python script leverages Selenium to navigate the Redbus website, extracting key information about bus routes including:
Bus names
Types
Departure and arrival times
Duration
Fares
Ratings
Seat availability
Data Storage: The scraped data is organized into a structured format and saved as a CSV file for further processing.

### 2. Data Processing
Data Cleaning: The script cleans and preprocesses the scraped data using Pandas. This includes:
Handling missing values
Normalizing the "Rating" column
Preparing the data for insertion into a MySQL database.

### 3. Database Integration
Storage: The cleaned data is stored in a MySQL database, allowing for efficient querying and retrieval.

### 4. Dynamic Data Visualization
Streamlit Application: A user-friendly web application is created with Streamlit, enabling users to:
Filter data by bus type, route, price range, availability, and star rating.
Visualize insights through interactive charts, including:
Price distribution
Count of buses by type
Star ratings distribution
Average price by bus type
Total seat availability

### 5. User Interaction
Experience: The Streamlit app allows for real-time interaction with the data, providing users with valuable insights into bus services available on Redbus.
Technologies Used
Languages: Python
Libraries:
Selenium for web scraping
Pandas for data manipulation
Streamlit for web app development
Matplotlib and Seaborn for visualizations
Database: MySQL for data storage

## Conclusion
This project illustrates the integration of web scraping, data processing, and dynamic visualization into a cohesive application, making it easier for users to explore and compare bus services on Redbus.
