```sql
-- QUERY 1

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



-- QUERY 2

SELECT *
FROM (

    SELECT
        s.region,
        s.farm_name,
        SUM(o.total_price) AS total_revenue,

        RANK() OVER (
            PARTITION BY s.region
            ORDER BY SUM(o.total_price) DESC
        ) AS regional_rank

    FROM Suppliers s

    JOIN Orders o
    ON s.supplier_id = o.supplier_id

    GROUP BY
        s.region,
        s.farm_name

) ranked

WHERE regional_rank <= 3;
```
