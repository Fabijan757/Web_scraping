Book Analysis – Automated Data Pipeline (Airflow + Python + MySQL)

This project demonstrates a fully automated data processing pipeline.
The goal was to collect book data from a website, automate the entire workflow using Apache Airflow, store the data in a MySQL database, and finally analyze and visualize the results.

1. Web scraping
The project starts with a Python web scraping script.
Book data is automatically collected from a website, including:
- book title
- price
- availability

The data is saved into a CSV file called books_raw.csv.

2. Automation with Airflow
The entire process is orchestrated using Apache Airflow:
- a DAG is defined
- the process runs automatically
- Airflow executes the scraping script
- reliable and repeatable execution is ensured

3. Data ingestion into MySQL
The generated CSV file is loaded into a MySQL database:
- a table named books is created
- data is stored for further analysis
- the database serves as a central analytics layer

4. SQL analysis
Analytical SQL queries are executed in MySQL, including:
- average book price
- most expensive book
- cheapest book
- top 8 most expensive books
- top 8 cheapest books

5. Data visualization
The analysis results are used to build a Python dashboard:
- key metrics overview
- tabular data view
- book price charts

6. Final result
The project demonstrates a complete data workflow:
Web → Scraping → Airflow → CSV → MySQL → SQL Analysis → Visualization
