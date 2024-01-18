def check_in_tuples(colors, search_c):
    result = any(search_c in ls for ls in colors)
    return result

colors = (
    ('Red', 'White', 'Blue'),
    ('Green', 'Pink', 'Purple'),
    ('Orange', 'Yellow', 'Lime'),
)
print("Original list:")
print(colors)
c1 = 'White'
print("\nCheck if",c1,"present in said tuple of tuples!")
print(check_in_tuples(colors, c1))
c1 = 'White'
print("\nCheck if",c1,"present in said tuple of tuples!")
print(check_in_tuples(colors, c1))
c1 = 'Olive'
print("\nCheck if",c1,"present in said tuple of tuples!")
print(check_in_tuples(colors, c1))