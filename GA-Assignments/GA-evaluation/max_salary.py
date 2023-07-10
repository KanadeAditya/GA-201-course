def max_salary(lists):
    max = 0
    max_item = {}
    for item in lists:
        if item["salary"]>max:
            max = item["salary"]
            max_item = item
    return max_item

salaries = [
    {"name" : "John","salary": 3000 , "designation": "developer" },
    {"name" : "Emma","salary": 4000 , "designation": "manager" },
    {"name" : "Kelly","salary": 3500 , "designation": "tester" }
]

ans = max_salary(salaries)

print(ans)