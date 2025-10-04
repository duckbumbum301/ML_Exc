import sqlite3
import pandas as pd
try:
    sqliteConnection=sqlite3.connect('../databases/Chinook_Sqlite.sqlite')
    cursor=sqliteConnection.cursor()
    print('DB Init')
    query='SELECT * FROM InvoiceLine LIMIT 5;'
    cursor.execute(query)
    df=pd.DataFrame(cursor.fetchall())
    print(df)
    cursor.close()

except sqlite3.Error as error:
    print('Error occured - ',error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')

import sqlite3
import pandas as pd

# (1) TOP N invoices with total in [a, b], sorted DESC by total
def top_invoices_in_range(conn, a, b, n):
    sql = """
    SELECT InvoiceId AS InvoiceID, Total
    FROM Invoice
    WHERE Total BETWEEN ? AND ?
    ORDER BY Total DESC
    LIMIT ?;
    """
    return pd.read_sql_query(sql, conn, params=(a, b, n))

# (2) TOP N customers with the most invoices
def top_customers_by_invoice_count(conn, n):
    sql = """
    SELECT c.CustomerId,
           c.FirstName || ' ' || c.LastName AS CustomerName,
           COUNT(i.InvoiceId) AS InvoiceCount
    FROM Customer c
    LEFT JOIN Invoice i ON i.CustomerId = c.CustomerId
    GROUP BY c.CustomerId
    ORDER BY InvoiceCount DESC, CustomerName ASC
    LIMIT ?;
    """
    return pd.read_sql_query(sql, conn, params=(n,))

# (3) TOP N customers by highest total invoice value
def top_customers_by_total_spent(conn, n):
    sql = """
    SELECT c.CustomerId,
           c.FirstName || ' ' || c.LastName AS CustomerName,
           ROUND(SUM(i.Total), 2) AS TotalSpent,
           COUNT(i.InvoiceId) AS InvoiceCount
    FROM Customer c
    JOIN Invoice i ON i.CustomerId = c.CustomerId
    GROUP BY c.CustomerId
    ORDER BY TotalSpent DESC
    LIMIT ?;
    """
    return pd.read_sql_query(sql, conn, params=(n,))

with sqlite3.connect("../databases/Chinook_Sqlite.sqlite") as conn:
    print(top_invoices_in_range(conn, 5, 25, 3))         # (1)
    print(top_customers_by_invoice_count(conn, 5))       # (2)
    print(top_customers_by_total_spent(conn, 5))         # (3)
