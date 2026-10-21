import json
import yaml
import xml.etree.ElementTree as ET

# 1.1
# res_1 = {"test_suite": "api_tests", "total": 10, "passed": 8, "failed": 2}
# with open("test_results.json", "w") as f:
#     json.dump(res_1, f)

# 1.2
# res_2 = [{"id": 1, "name": "Sasha", "role": "admin"}]
# with open("user.json", "w") as f:
#     json.dump(res_2, f)

# 1.3
# with open("test_results.json", "r") as f:
#     loaded_1 = json.load(f)

# print(f"Успешно пройдено тестов: {(loaded_1['passed'])/(loaded_1['total']) * 100} %")

# 1.4
# with open("user.json", "r") as f:
#     loaded_2 = json.load(f)

# loaded_2[0]["user"] = "Victor"

# with open("user.json", "w") as f:
#     json.dump(loaded_2, f)

# print(loaded_2)

# 2.1
# res_3 = {"test_suite": "api_tests", "total": 10, "passed": 8, "failed": 2}
# with open("test_results.yaml", "w") as f:
#     yaml.dump(res_3, f)

# 2.2
# res_4 = [{"id": 1, "name": "Sasha", "role": "admin"}]
# with open("user.yaml", "w") as f:
#     yaml.dump(res_4, f)

# 2.3
# with open("test_results.yaml", "r") as f:
#     loaded_3 = yaml.safe_load(f)

# print(f"Успешно пройдено тестов: {(loaded_3['passed'])/(loaded_3['total']) * 100} %")

# 2.4
# with open("user.yaml", "r") as f:
#     loaded_4 = yaml.safe_load(f)

# loaded_4[0]["user"] = "Victor"

# with open("user.yaml", "w") as f:
#     yaml.dump(loaded_4, f)

# print(loaded_4)

# 3.1
# tree = ET.parse("employees.xml")
# root = tree.getroot()

# employees = root.findall("employee")
# total_count = len(employees)

# total_salary = 0
# for empl in employees:
#     salary_text = empl.find("salary").text
#     total_salary += int(salary_text)


# print(f"Количество сотрудников: {total_count}")
# print(f"Суммарная зарплата: {total_salary}")
