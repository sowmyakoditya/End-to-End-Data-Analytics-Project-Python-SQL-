# Project Overview
This project involves data processing and analysis of order data using Python and SQL Server. The following steps were executed:

# Data Import:

Read CSV file orders.csv into a Pandas DataFrame.

# Handling Null Values:

Treated 'Not Available' and 'unknown' as NaN values for proper data handling.

# Data Cleaning:

Renamed columns to lower case and replaced spaces with underscores.
Derived new columns: discount, sale_price, and profit from existing data.

# Date Conversion:

Converted the order_date column from object type to datetime format for accurate date handling.

# Column Removal:

Dropped unnecessary columns: list_price, cost_price, and discount_percent.

# Database Connection:

Established a connection to SQL Server using SQLAlchemy.

# Data Upload:

Loaded data into SQL Server table df_orders using append option to add data to an existing table.

## SQL Queries:

# Top 10 Highest Revenue Generating Products:

SELECT TOP 10 product_id, SUM(sale_price) AS sales
FROM df_orders
GROUP BY product_id
ORDER BY sales DESC;

# Top 5 Highest Selling Products in Each Region:

WITH cte AS (
    SELECT region, product_id, SUM(sale_price) AS sales
    FROM df_orders
    GROUP BY region, product_id
)
SELECT *
FROM (
    SELECT *,
    ROW_NUMBER() OVER (PARTITION BY region ORDER BY sales DESC) AS rn
    FROM cte
) A
WHERE rn <= 5;

# Month-over-Month Growth Comparison for 2022 and 2023:

WITH cte AS (
    SELECT YEAR(order_date) AS order_year, MONTH(order_date) AS order_month,
    SUM(sale_price) AS sales
    FROM df_orders
    GROUP BY YEAR(order_date), MONTH(order_date)
)
SELECT order_month,
SUM(CASE WHEN order_year = 2022 THEN sales ELSE 0 END) AS sales_2022,
SUM(CASE WHEN order_year = 2023 THEN sales ELSE 0 END) AS sales_2023
FROM cte
GROUP BY order_month
ORDER BY order_month;

# Highest Sales Month for Each Category:

WITH cte AS (
    SELECT category, FORMAT(order_date, 'yyyyMM') AS order_year_month,
    SUM(sale_price) AS sales
    FROM df_orders
    GROUP BY category, FORMAT(order_date, 'yyyyMM')
)
SELECT *
FROM (
    SELECT *,
    ROW_NUMBER() OVER (PARTITION BY category ORDER BY sales DESC) AS rn
    FROM cte
) a
WHERE rn = 1;
