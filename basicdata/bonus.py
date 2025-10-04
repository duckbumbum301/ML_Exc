import pandas as pd

def list_invoices_by_total(df, minValue, maxValue, SortType=True):
    """
    Trả về danh sách (OrderID, Sum) của các hóa đơn có tổng nằm trong [minValue, maxValue],
    sắp xếp theo SortType (True=tăng dần, False=giảm dần).
    Returns a list of (OrderID, Sum) within [minValue, maxValue], sorted by SortType.
    """
    # Tính tổng tiền mỗi hóa đơn / compute total per order
    totals = (
        df.assign(Total=df['UnitPrice'] * df['Quantity'] * (1 - df['Discount']))
          .groupby('OrderID', as_index=False)['Total'].sum()
          .rename(columns={'Total': 'Sum'})
    )

    # Lọc theo khoảng và sắp xếp / filter by range and sort
    filtered = totals[(totals['Sum'] >= minValue) & (totals['Sum'] <= maxValue)] \
                .sort_values('Sum', ascending=SortType)

    # Trả về list các tuple (OrderID, Sum) / return a list of tuples
    return list(filtered.itertuples(index=False, name=None))


# --- Ví dụ dùng / Example usage ---
df = pd.read_csv('../dataset/SalesTransactions/SalesTransactions.csv')

# ascending like "SortType=True" table
print(pd.DataFrame(list_invoices_by_total(df, 400, 1000, True), columns=['OrderID','Sum']))

# descending like "SortType=False" table
print(pd.DataFrame(list_invoices_by_total(df, 400, 1000, False), columns=['OrderID','Sum']))
