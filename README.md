# Table-Augmented Generation (TAG) with Python and MySQL

This project demonstrates how to implement **Table-Augmented Generation (TAG)** using Python, MySQL, and open-source libraries. The goal is to generate natural language descriptions from structured tabular data stored in a MySQL database.

---

## Table of Contents
1. [Overview](#overview)
2. [Tech Stack](#tech-stack)
3. [Installation](#installation)
4. [Setup MySQL Database](#setup-mysql-database)
5. [How It Works](#how-it-works)
6. [Optimizations](#optimizations)
7. [Contributing](#contributing)
8. [License](#license)
9. [Links](#Links)

---

## Overview
Table-Augmented Generation (TAG) is a technique that enhances text generation by incorporating structured data (e.g., tables) into the process. This project uses a MySQL database to store structured data and a pre-trained language model (GPT-2) from Hugging Face to generate natural language descriptions.

---

## Tech Stack
- **Python**: Primary programming language.
- **MySQL**: Database to store structured tables.
- **Hugging Face Transformers**: Open-source library for NLP models.
- **SQLAlchemy**: Python library for database interaction.
- **Pandas**: For handling tabular data.

---

## Installation
1. **Install Python**: Download and install Python from [python.org](https://www.python.org/).
2. **Install MySQL**: Download and install MySQL from [mysql.com](https://www.mysql.com/).
3. **Install Required Python Packages**:

### Install Required Python Packages:  


```bash
    pip install transformers sqlalchemy pandas torch pymysql
```

### Set Up Environment Variables:
Create a .env file and add:

```shell
DATABASE_URI=mysql+pymysql://username:password@host/database_name
```

---

## Setup MySQL Database

Run the following SQL commands in MySQL:

```shell
CREATE DATABASE test;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10,2),
    rating FLOAT,
    features TEXT
);

INSERT INTO products (name, price, rating, features) VALUES
('Coffee Maker', 5000, 4.5, 'Automatic, 1.5L capacity, stainless steel'),
('Blender', 3500, 4.2, '500W, 3-speed, BPA-free jar');
```

---

## How It Works

1. Connect to MySQL:
   - The script loads database credentials from the .env file.
       •	It connects using SQLAlchemy and fetches data from the products table.
2. Load GPT-2 for Text Generation:
   - Uses Hugging Face’s transformers library to load a pre-trained GPT-2 model.
3. Apply Few-Shot Learning:
   - Provides example descriptions to the model.
   - Dynamically generates a custom description for each product.
4. Store Generated Descriptions:
   - Saves the generated text back into the product_descriptions table in MySQL.

---

## Optimizations

- Use a better model: Try gpt-3.5-turbo for better descriptions.
- Fine-tune a custom model: Train on domain-specific data.
- Add error handling: Manage database and API errors effectively.

---


## License

This project is open-source under the MIT License.

## Links

- [TAG](https://mohammedjassimjasm.wixsite.com/blog/post/table-augmented-generation-tag)