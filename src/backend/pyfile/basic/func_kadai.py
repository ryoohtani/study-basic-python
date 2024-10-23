"""
消費税が現在１０％
消費税 = 商品価格 * 0.1
100 = 1000 * 0.1

消費税を含む商品合計は１１００円
"""

def calculate_total_price(price: int, tax_rate: float) -> float:
    tax = price * tax_rate
    total_price = price + tax
    return total_price

total = calculate_total_price(2500, 0.1)
print(total)