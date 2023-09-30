# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 16:23:43 2023

@author: superuser
"""
import sqlite3

conn = sqlite3.connect('BBQ.db')

cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS meat (
                   id INTEGER,
                   name TEXT,
                   price INTEGER,
                   quantity INTEGER
               )''')
               
cursor.execute("INSERT INTO meat (name, price, quantity) VALUES ('chicken', 30, 5)")  
cursor.execute("INSERT INTO meat (name, price, quantity) VALUES ('beaf', 55, 10)")
cursor.execute("INSERT INTO meat (name, price, quantity) VALUES ('pork', 40, 15)")    
conn.commit()

cursor.execute("SELECT * FROM meat")
meat = cursor.fetchall()
print("肉列表:")
for Meat in meat:
   print (Meat)  

cursor.execute("UPDATE meat SET price = 35 WHERE name = 'pork'")
cursor.execute("UPDATE meat SET quantity = 30 WHERE name = 'chicken'")
conn.commit()

cursor.execute("SELECT * FROM meat")
meat = cursor.fetchall()
print("更新後的肉列表:")
for Meat in meat:
   print (Meat)

cursor.execute("DELETE FROM meat WHERE price = 40")
conn.commit()

cursor.execute("SELECT * FROM meat")
meat = cursor.fetchall()
print("刪除後的肉列表:")
for Meat in meat:
   print (Meat)
   
cursor.close()
conn.close()




