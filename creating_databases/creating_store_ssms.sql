IF NOT EXISTS(SELECT * FROM sys.databases WHERE name = 'store_db')
	CREATE DATABASE store_db;

USE store_db;

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='products')
    CREATE TABLE products (
        product_id INT CHECK (product_id >= 0) NOT NULL IDENTITY PRIMARY KEY,
		product_name NVARCHAR(50) NOT NULL,
		category NVARCHAR(50) NOT NULL,
		price SMALLINT CHECK (price >= 0) NOT NULL,
		color NVARCHAR(50) NOT NULL,
		size TINYINT CHECK (size >= 0) NOT NULL,
		stock INT CHECK (stock >= 0) NOT NULL DEFAULT 0,
		);

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='customers')
    CREATE TABLE customers (
        customer_id INT CHECK (customer_id >= 0) NOT NULL IDENTITY PRIMARY KEY,
	    first_name NVARCHAR(50) NOT NULL,
		last_name NVARCHAR(50) NOT NULL,
		customer_address NVARCHAR(100) NOT NULL,
		phone_number NCHAR(10) NOT NULL,
		email NVARCHAR(100) NOT NULL,
		);

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='shipments')
    CREATE TABLE shipments (
        shipping_id INT CHECK (shipping_id >= 0) NOT NULL IDENTITY PRIMARY KEY,
	    shipping_type NVARCHAR(50) NOT NULL,
		shipping_cost INT CHECK (shipping_cost >=0) NOT NULL,
		);

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='billing')
    CREATE TABLE billing (
        billing_id INT CHECK (billing_id >= 0) NOT NULL IDENTITY PRIMARY KEY,
	    billing_address NVARCHAR(100) NOT NULL,
		card_number NCHAR(16) NOT NULL,
	    card_exp_date NCHAR(10) NOT NULL,
		card_security_code NCHAR(4) NOT NULL,
		);

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='orders')
    CREATE TABLE orders (
        order_id INT CHECK (order_id >= 0) NOT NULL IDENTITY PRIMARY KEY,
		customer_id INT CHECK (customer_id >= 0) NOT NULL,
		billing_id INT CHECK (billing_id >= 0) NOT NULL,
		shipping_id INT CHECK (shipping_id >= 0) NOT NULL,
		order_date DATE NOT NULL,
		total_price INT CHECK (total_price >= 0) NOT NULL,
		shipment_address NVARCHAR(100) NOT NULL,
		shipment_date DATE NOT NULL,
		CONSTRAINT fk_o_customers FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
		CONSTRAINT fk_o_shipment FOREIGN KEY(shipping_id) REFERENCES shipments(shipping_id),
		CONSTRAINT fk_o_billing FOREIGN KEY(billing_id) REFERENCES billing(billing_id)
		);

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='order_products')
    CREATE TABLE order_products (
        order_products_id INT CHECK (order_products_id >= 0) NOT NULL IDENTITY PRIMARY KEY,
	    order_id INT CHECK (order_id >= 0) NOT NULL,
	    product_id INT CHECK (product_id >= 0) NOT NULL,
	    quantity SMALLINT CHECK (quantity >= 0) NOT NULL DEFAULT 1,
	    CONSTRAINT fk_od_orders FOREIGN KEY(order_id) REFERENCES orders(order_id),
	    CONSTRAINT fk_od_products FOREIGN KEY(product_id) REFERENCES products(product_id)
		);


CREATE ROLE store_rd;
CREATE ROLE store_wrt;
GRANT SELECT ON DATABASE :: store_db TO store_rd
GRANT SELECT, INSERT, UPDATE ON DATABASE :: store_db TO store_wrt;

CREATE LOGIN store_rd1@localhost WITH PASSWORD = '123456';
CREATE USER store_rd1@localhost FOR LOGIN store_rd1@localhost;

CREATE LOGIN store_wrt1@localhost WITH PASSWORD = '123456';
CREATE USER store_wrt1@localhost FOR LOGIN store_wrt1@localhost;

ALTER ROLE store_rd ADD MEMBER store_rd1@localhost;
ALTER ROLE store_wrt ADD MEMBER store_wrt1@localhost;














