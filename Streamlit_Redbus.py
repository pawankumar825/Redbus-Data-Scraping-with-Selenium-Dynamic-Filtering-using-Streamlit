import streamlit as st
import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import seaborn as sns

# Function to connect to MySQL and execute a query
def execute_query(query, params=None):
    myconnection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='12345',
        database='Redbus'  
    )

    try:
        df = pd.read_sql(query, myconnection, params=params)
        return df
    except Exception as e:
        st.error(f"Error: {e}")
        return pd.DataFrame()
    finally:
        myconnection.close()

# Function to generate SQL query based on filters
def generate_query(bustype, route, price_min, price_max, availability, star_rating):
    query = "SELECT * FROM bus_routes WHERE 1=1"
    
    if bustype and bustype != "All":
        query += f" AND bustype = %s"
    if route and route != "All":
        query += f" AND route_name = %s"
    if price_min is not None:
        query += f" AND price >= {price_min}"
    if price_max is not None:
        query += f" AND price <= {price_max}"
    if availability is not None:
        query += f" AND seats_available >= {availability}"
    if star_rating is not None:
        query += f" AND star_rating >= {star_rating}"
    
    return query

# Function to plot visualizations
def plot_visualizations(data):
    # Set the aesthetics for the plots
    sns.set(style="whitegrid")

    # 1. Price Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(data['price'], bins=30, kde=True)
    plt.title('Distribution of Bus Prices')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    st.pyplot(plt)

    # 2. Count of Buses by Type
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='bustype', order=data['bustype'].value_counts().index)
    plt.title('Count of Buses by Type')
    plt.xticks(rotation=45)
    plt.xlabel('Bus Type')
    plt.ylabel('Count')
    st.pyplot(plt)

    # 3. Star Ratings Distribution by Bus Type
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data, x='bustype', y='star_rating')
    plt.title('Star Ratings Distribution by Bus Type')
    plt.xticks(rotation=45)
    plt.xlabel('Bus Type')
    plt.ylabel('Star Rating')
    st.pyplot(plt)

    # 4. Average Price by Bus Type
    plt.figure(figsize=(10, 6))
    avg_price = data.groupby('bustype')['price'].mean().reset_index()
    sns.barplot(data=avg_price, x='bustype', y='price')
    plt.title('Average Price by Bus Type')
    plt.xticks(rotation=45)
    plt.xlabel('Bus Type')
    plt.ylabel('Average Price')
    st.pyplot(plt)

    # 5. Availability of Seats by Bus Type
    plt.figure(figsize=(10, 6))
    seat_availability = data.groupby('bustype')['seats_available'].sum().reset_index()
    sns.barplot(data=seat_availability, x='bustype', y='seats_available')
    plt.title('Total Seat Availability by Bus Type')
    plt.xticks(rotation=45)
    plt.xlabel('Bus Type')
    plt.ylabel('Total Seats Available')
    st.pyplot(plt)

# Streamlit application
def main():
    st.set_page_config(page_title="RedBus Data Analysis", layout="wide")
    
    st.markdown(
        """
        <style>
        .reportview-container {
            background-color: #eaeef2;
        }
        .sidebar .sidebar-content {
            background-color: #d4e2f2;
        }
        h1 {
            color: #4b0082;
        }
        h2 {
            color: #3e5b99;
        }
        </style>
        """, unsafe_allow_html=True
    )
    
    # Add Redbus logo
    st.image("C:\\Users\\abdpa\\Downloads\\redBus Logo.jpg", width=50)
    st.title('Redbus Data Analysis')
    st.sidebar.header('Filter Options')

    # Fetch unique values for filters
    bustypes_df = execute_query("SELECT DISTINCT bustype FROM bus_routes")
    routes_df = execute_query("SELECT DISTINCT route_name FROM bus_routes")

    # Ensure the columns exist
    if 'bustype' in bustypes_df.columns and 'route_name' in routes_df.columns:
        bustypes = ["All"] + bustypes_df['bustype'].tolist()
        routes = ["All"] + routes_df['route_name'].tolist()
    else:
        st.error("The necessary columns were not found in the database.")
        return

    # Sidebar filters with searchable dropdown
    selected_bustype = st.sidebar.selectbox(
        "Bus Type",
        options=bustypes,
        index=0,
        format_func=lambda x: x
    )
    
    selected_route = st.sidebar.selectbox(
        "Bus Route",
        options=routes,
        index=0,
        format_func=lambda x: x
    )

    price_range = st.sidebar.slider("Price Range", 0, 5000, (0, 5000))
    availability = st.sidebar.number_input("Minimum Availability", min_value=0, value=0, step=1)
    star_rating = st.sidebar.slider("Minimum Star Rating", 1.0, 5.0, 1.0, 0.1)

    # Generate and execute query
    query = generate_query(
        selected_bustype if selected_bustype != "All" else None,
        selected_route if selected_route != "All" else None,
        price_range[0],
        price_range[1],
        availability,
        star_rating
    )
    
    params = []
    if selected_bustype != "All":
        params.append(selected_bustype)
    if selected_route != "All":
        params.append(selected_route)
    
    filtered_df = execute_query(query, params)
    
    # Display the filtered data
    st.subheader('Filtered Data')
    if not filtered_df.empty:
        st.dataframe(filtered_df)
    else:
        st.warning("No results found for the selected filters.")

    # Plot visualizations
    if not filtered_df.empty:
        st.subheader('Visualizations')
        plot_visualizations(filtered_df)

if __name__ == '__main__':
    main()
