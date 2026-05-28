```sql
CREATE TABLE Suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    farm_name TEXT NOT NULL,
    region TEXT NOT NULL,
    contact_person TEXT,
    phone TEXT UNIQUE
);

CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_id INTEGER NOT NULL,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    total_price REAL NOT NULL CHECK (total_price > 0),
    order_date TEXT NOT NULL,

    FOREIGN KEY (supplier_id)
    REFERENCES Suppliers(supplier_id)
);

CREATE TABLE Sales_Targets (
    region TEXT NOT NULL,
    quarter TEXT NOT NULL,
    target_amount REAL NOT NULL CHECK (target_amount > 0),

    PRIMARY KEY (region, quarter)
);

CREATE TABLE Certifications (
    certification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_id INTEGER NOT NULL,
    certification_name TEXT NOT NULL,
    issue_date TEXT NOT NULL,

    FOREIGN KEY (supplier_id)
    REFERENCES Suppliers(supplier_id)
);

CREATE TABLE Harvest_Log (
    harvest_id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_id INTEGER NOT NULL,
    crop_name TEXT NOT NULL,
    harvest_date TEXT NOT NULL,
    quantity_kg REAL NOT NULL CHECK (quantity_kg > 0),

    FOREIGN KEY (supplier_id)
    REFERENCES Suppliers(supplier_id)
);
```
