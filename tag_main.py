#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Mohammed Jassim at 07/03/25
import os

from sqlalchemy import create_engine, text
import pandas as pd
from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()
# Step 1: Connect to MySQL
DATABASE_URI = os.getenv("DATABASE_URI")
engine = create_engine(DATABASE_URI)

# Step 2: Fetch table data
query = text("SELECT * FROM products")
df = pd.read_sql(query, engine)

# Step 3: Load text generation model
generator = pipeline("text-generation", model="gpt2")

# Step 4: Define few-shot examples
few_shot_examples = """
Example 1:
Product: Coffee Maker
Price: ₹5000
Rating: 4.5
Features: Automatic, 1.5L capacity, stainless steel
Description: The Coffee Maker is a premium appliance priced at ₹5000. With a 4.5-star rating, it offers advanced features like automatic operation, a 1.5-liter capacity, and a durable stainless steel build. Perfect for coffee enthusiasts, it ensures a seamless brewing experience.

Example 2:
Product: Blender
Price: ₹3500
Rating: 4.2
Features: 500W, 3-speed, BPA-free jar
Description: The Blender is a versatile kitchen tool priced at ₹3500. With a 4.2-star rating, it provides 500W power, 3-speed settings, and a BPA-free jar for safe and efficient blending. Ideal for smoothies, soups, and more.
"""


# Step 5: Generate dynamic prompts with few-shot learning
def generate_description(row):
    prompt = f"""
    Below are examples of product descriptions:

    Example 1:
    Product: Coffee Maker
    Price: ₹5000
    Rating: 4.5
    Features: Automatic, 1.5L capacity, stainless steel
    Description: The Coffee Maker is a premium appliance priced at ₹5000. With a 4.5-star rating, it offers advanced features like automatic operation, a 1.5-liter capacity, and a durable stainless steel build. Perfect for coffee enthusiasts, it ensures a seamless brewing experience.

    Example 2:
    Product: Blender
    Price: ₹3500
    Rating: 4.2
    Features: 500W, 3-speed, BPA-free jar
    Description: The Blender is a versatile kitchen tool priced at ₹3500. With a 4.2-star rating, it provides 500W power, 3-speed settings, and a BPA-free jar for safe and efficient blending. Ideal for smoothies, soups, and more.

    Now generate a description for the following product:

    Product: {row['name']}
    Price: ₹{row['price']}
    Rating: {row['rating']}
    Features: {row['features']}
    Description:"""

    response = generator(prompt, max_new_tokens=50, num_return_sequences=1, truncation=True)

    return response[0]['generated_text'].split("Description:")[-1].strip()


# Step 6: Apply the function to each row
df['description'] = df.apply(generate_description, axis=1)

# Step 7: Save results to MySQL
df.to_sql('product_descriptions', engine, if_exists='replace', index=False)
