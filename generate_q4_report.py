```python
import sqlite3
import csv

try:

    # CONNECT
    conn = sqlite3.connect("karoo_organics.db")

    cursor = conn.cursor()

    print("Database connected successfully")

    # CREATE TABLES
    with open("schema.sql", "r") as file:
        schema = file.read()

    cursor.executescript(schema)

    # INSERT DATA
    with open("data.sql", "r") as file:
        data = file.read()

    cursor.executescript(data)

    conn.commit()

    # QUERY
    query = """

    SELECT
        s.region,
        COALESCE(SUM(o.total_price), 0) AS actual_revenue,
        st.target_amount,

        CASE
            WHEN st.target_amount = 0 THEN 0
            ELSE ROUND(
                (SUM(o.total_price) / st.target_amount) * 100,
                2
            )
        END AS percent_of_target

    FROM Suppliers s

    JOIN Orders o
    ON s.supplier_id = o.supplier_id

    JOIN Sales_Targets st
    ON s.region = st.region

    WHERE st.quarter = 'Q4-2025'

    GROUP BY
        s.region,
        st.target_amount;

    """

    cursor.execute(query)

    results = cursor.fetchall()

    # PRINT RESULTS
    print("\nQ4 PERFORMANCE REPORT\n")

    for row in results:
        print(row)

    # EXPORT CSV
    with open("q4_performance.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Region",
            "Actual Revenue",
            "Target Amount",
            "Percent of Target"
        ])

        writer.writerows(results)

    print("\nCSV report generated successfully")

except Exception as e:

    print("Error:", e)

finally:

    if 'conn' in locals():
        conn.close()

    print("\nDatabase connection closed")
```
