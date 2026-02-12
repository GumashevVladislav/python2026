Вопросы с выбором варианта: 54/100%  
# Вопрос 1. Тема: Сложные запросы
  
**1. Какой оператор используется для объединения двух таблиц в SQL?**
  
Варианты ответов:
1) UNION
2) COMBINE
3) ✅ JOIN
4) MERGE
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 2. Тема: Сложные запросы
  
**2. Как объединить таблицы Customers и Orders по полю CustomerID и выбрать все строки из таблицы Customers, даже если нет соответствующих записей в таблице Orders?**
  
Варианты ответов:
1) SELECT * FROM Customers INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID
2) SELECT * FROM Customers RIGHT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
3) SELECT * FROM Customers FULL JOIN Orders ON Customers.CustomerID = Orders.CustomerID
4) ✅ SELECT * FROM Customers LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 3. Тема: Сложные запросы
  
**3. Что вернёт запрос `SELECT Customers.Name, Orders.OrderID FROM Customers LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;`, если в таблице Customers есть клиенты без заказов?**
  
Варианты ответов:
1) ✅ Запрос вернёт всех клиентов (включая тех, у кого нет заказов) с пустыми значениями для OrderID
2) Запрос вернёт только клиентов с заказами
3) Запрос вернёт только заказы, без клиентов
4) Запрос не вернёт результатов
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 4. Тема: Сложные запросы
  
**4. Какой результат вернёт следующий SQL-запрос?**

```
SELECT Name FROM Customers
UNION
SELECT Name FROM Suppliers;
```
  
Варианты ответов:
1) Вернёт только совпадающие значения из обеих таблиц
2) ❌ Объединит результаты обеих таблиц, включая дубликаты
3) Вернёт только уникальные имена из таблиц Customers и Suppliers
4) Объединит результаты, но добавит NULL вместо отсутствующих значений
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 5. Тема: Сложные запросы
  
**5. Какой результат вернёт следующий SQL-запрос?**

```
SELECT ProductName FROM Products
EXCEPT
SELECT ProductName FROM DiscontinuedProducts;
```
  
Варианты ответов:
1) Вернёт только товары, которые присутствуют в обеих таблицах
2) Вернёт список всех товаров, включая устаревшие
3) ❌ Вернёт только устаревшие товары
4) Вернёт товары, которые есть в Products, но отсутствуют в DiscontinuedProducts
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
