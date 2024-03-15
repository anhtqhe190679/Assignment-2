class ChungKhoan:
    def __init__(self, ma_chung_khoan, gia_mo_cua, gia_dong_cua):
        self.ma_chung_khoan = ma_chung_khoan
        self.gia_mo_cua = gia_mo_cua
        self.gia_dong_cua = gia_dong_cua

def read_data(filename):
    data = []
    with open(filename, 'w') as file:
        N = int(file.readline().strip())
        for _ in range(N):
            for _ in range(10):  
                line = file.readline().strip()
                if line:
                    ma, gia_mo, gia_dong = line.split()
                    data.append(ChungKhoan(ma, float(gia_mo), float(gia_dong)))
    return data

def print_sorted_stock_info(data):
    stock_info = {}
    for stock in data:
        if stock.ma_chung_khoan not in stock_info:
            stock_info[stock.ma_chung_khoan] = []
        stock_info[stock.ma_chung_khoan].append(stock.gia_dong_cua - stock.gia_mo_cua)

    for symbol in sorted(stock_info.keys()):
        average_diff = sum(stock_info[symbol]) / len(stock_info[symbol])
        print(f"{symbol}: {average_diff:.3f}")

def search_stock_by_symbol(data, symbol):
    max_close = float('-inf')
    min_close = float('inf')
    found = False
    for stock in data:
        if stock.ma_chung_khoan == symbol:
            found = True
            max_close = max(max_close, stock.gia_dong_cua)
            min_close = min(min_close, stock.gia_dong_cua)
    if found:
        print(f"Highest closing price for {symbol}: {max_close:.3f}")
        print(f"Lowest closing price for {symbol}: {min_close:.3f}")
    else:
        print("Không tìm thấy mã chứng khoán.")


def find_upward_trend_stocks(data):
    upward_trend_stocks = set()
    for i in range(0, len(data), 10):  
        for j in range(i, i + 10, 5):  
            day1_open = data[j].gia_mo_cua
            day1_close = data[j].gia_dong_cua
            day2_open = data[j + 1].gia_mo_cua
            day2_close = data[j + 1].gia_dong_cua
            if day1_close > day1_open and day2_close > day2_open:
                upward_trend_stocks.add(data[j].ma_chung_khoan)
    return upward_trend_stocks

def find_max_upward_trend(data):
    stock_upward_trend_count = {}
    for i in range(0, len(data), 10):
        stock = data[i].ma_chung_khoan
        count = 0
        for j in range(i, i + 10, 5):
            day_open = data[j].gia_mo_cua
            day_close = data[j].gia_dong_cua
            if day_close > day_open:
                count += 1
        stock_upward_trend_count[stock] = count

    max_count = max(stock_upward_trend_count.values())
    max_stocks = [stock for stock, count in stock_upward_trend_count.items() if count == max_count]

    print("Mã có số ngày tăng lớn nhất:")
    for stock in max_stocks:
        print(f"{stock}: {max_count} ngày")

def menu():
    print("Chọn chức năng:")
    print("1. Đọc file")
    print("2. Tìm kiếm theo mã chứng khoán")
    print("3. Tìm kiếm những mã chứng khoán có xu hướng tăng ")
    print("4. Tìm mã có số ngày tăng lớn nhất")
    print("5. Thoát chương trình")
    return int(input("Nhập lựa chọn của bạn: "))

def main():
    data = []
    while True:
        choice = menu()
        if choice == 1:
            data = read_data("data.txt")
            print_sorted_stock_info(data)
        elif choice == 2:
            symbol = input("Nhập mã chứng khoán bạn muốn tìm kiếm: ")
            search_stock_by_symbol(data, symbol)
        elif choice == 3:
            upward_trend_stocks = find_upward_trend_stocks(data)
            print("Các mã có xu hướng tăng trong ngày 1 và ngày 2:")
            for stock in upward_trend_stocks:
                print(stock)
        elif choice == 4:
            find_max_upward_trend(data)
        elif choice == 5:
            print("Trần Quang Anh - HE190679")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
