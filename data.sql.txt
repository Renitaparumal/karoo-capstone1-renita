```sql
INSERT INTO Suppliers
(farm_name, region, contact_person, phone)
VALUES
('Karoo Fresh Farms', 'Western Cape', 'John Daniels', '0821111111'),
('Eastern Harvest', 'Eastern Cape', 'Lebo Mokoena', '0822222222'),
('Northern Organics', 'Northern Cape', 'Sarah Adams', '0823333333'),
('Cape Crop Solutions', 'Western Cape', 'Megan Smith', '0824444444');

INSERT INTO Orders
(supplier_id, product_name, quantity, total_price, order_date)
VALUES
(1, 'Organic Apples', 100, 12000, '2025-10-05'),
(1, 'Organic Pears', 80, 9000, '2025-10-15'),
(2, 'Spinach', 150, 7000, '2025-11-01'),
(2, 'Potatoes', 200, 15000, '2025-11-12'),
(3, 'Carrots', 180, 11000, '2025-11-25'),
(3, 'Tomatoes', 120, 9500, '2025-12-01'),
(4, 'Lettuce', 140, 8500, '2025-12-05'),
(4, 'Cabbage', 170, 10500, '2025-12-10'),
(1, 'Peaches', 90, 10000, '2025-12-15'),
(2, 'Beetroot', 100, 6500, '2025-12-20');

INSERT INTO Sales_Targets
(region, quarter, target_amount)
VALUES
('Western Cape', 'Q4-2025', 50000),
('Eastern Cape', 'Q4-2025', 30000),
('Northern Cape', 'Q4-2025', 25000);

INSERT INTO Harvest_Log
(supplier_id, crop_name, harvest_date, quantity_kg)
VALUES
(1, 'Apples', '2025-10-01', 500.50),
(2, 'Spinach', '2025-10-10', 300.00),
(3, 'Carrots', '2025-11-05', 450.75),
(4, 'Lettuce', '2025-11-18', 250.25),
(1, 'Peaches', '2025-12-01', 600.00);
```
