data = [['ID','Name', 'Price', 'Amount', 'Supplier'],
        ['321','Ibalgin', 40.50, 2841, 'Zentiva'],
        ['534','Paralen', 19.90, 3229, 'Zentiva'],
        ['327','Smecta', 68.00, 2709, 'Sipsen'],
        ['242','Uniclophen', 76.00, 476, 'UNIMED']]

total_price = 0
total_amount = 0
zentiva_items = 0

dict_data = {}
header = data[0][1:]

for row in data[1:]:
        total_price += row[2] * row[3]
        total_amount += row[3]
        if row[4] == "Zentiva":
                zentiva_items += 1
        id = row[0]
        dict_data[id] = {}
        for i, data in enumerate(row[1:]):
                key = header[i]
                dict_data[id].update({key:data})




print("Total price is:", total_price)
print("Total amount is:", total_amount)
print("Number of items from Zentiva:", zentiva_items)
print(dict_data)
