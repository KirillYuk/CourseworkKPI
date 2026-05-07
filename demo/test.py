from core.stream import generate_csv, filter_by_symbol

generate_csv("history.csv", "BTC", 30)

for row in filter_by_symbol("history.csv", "BTC"):
    print(row)
