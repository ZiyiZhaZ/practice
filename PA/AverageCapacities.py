def avg_capacity(product_list):
    x = 0
    if len(product_list) == 0:
        return x
    for i in product_list:
        y = i.split('-')
        x += float(y[1])
    return x / len(product_list)

print(avg_capacity(['C12-100', 'G14-40', 'F131-50', 'D3-10']))