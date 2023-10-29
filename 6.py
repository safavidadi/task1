test_list = [5, 6, [], 3, [], [], 9]

# Boş sublistləri silmək üçün list comprehension istifadə etmək
filtered_list = [x for x in test_list if x]

# Qalan ədədləri ekrana yazdırmaq
for item in filtered_list:
    print(item)
