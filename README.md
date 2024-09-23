## Project Overview
This project automates the extraction and analysis of bus route data from the Redbus website, utilizing Selenium for web scraping and Streamlit for dynamic data visualization and filtering.

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
