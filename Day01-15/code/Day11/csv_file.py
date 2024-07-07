import csv

def csv_file():
    with open('a.csv', 'w', newline='') as w:
        headers = ["username", "age", "height"]
        values = [{'username': 'jack', 'age': 18, 'height': 123}]
        writer = csv.DictWriter(w, fieldnames=headers)
        writer.writeheader()  # 写入头部信息
        writer.writerows(values)

        # 使用csv.writer追加一些数据，但通常不会在同一文件内混用DictWriter和writer
        # 这里仅为演示
        a = csv.writer(w)
        a.writerow(['Sam','17','90'])
        a.writerow(['Lucy','19','97'])

    # 读取并打印文件内容
    with open('a.csv', 'r', newline='') as t:
        # 只读取第一行
        first_row = next(csv.reader(t))
        print("First row:", first_row)

        # 重新读取整个文件（从头开始），因为之前的迭代器已经耗尽
        reader = csv.reader(t)  # 注意这里重新创建了一个reader
        for row in reader:
            print(row)

    # 使用DictReader读取，注意这不会从头开始读取文件，需要重新打开文件
    with open('a.csv', 'r', newline='') as m:
        reader = csv.DictReader(m)  # 不会包含标题那行的内容，但自动处理标题行
        for x in reader:  # 每一个元素是一个字典
            print(x)

csv_file()
