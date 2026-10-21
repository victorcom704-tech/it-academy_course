import json
import yaml
import xml.etree.ElementTree as ET


def dummy_test(data):
    if data <= 5:
        return True
    else:
        return False


tests = [
    (dummy_test(5), True),
    (dummy_test(7), True),
    (dummy_test(6), False),
    (dummy_test(2), True),
    (dummy_test(4), False),
    (dummy_test(8), True),
    (dummy_test(1), False),
]

total = len(tests)
passed = 0
failed = 0
errors = []

for result, expected in tests:
    try:
        assert result == expected
        passed += 1
    except AssertionError:
        failed += 1
        errors.append(f"Ожидалось {expected}, получили {result}")
        print(
            f"Тест не пройден! Ожидается что пароль результат {expected}, "
            + f"но фактический результат {result}"
        )
        continue
    print("Тест прошёл!")

percentage = round((passed / total) * 100, 1)
res = {
    "total": total,
    "passed": passed,
    "failed": failed,
    "percentage": percentage,
    "errors": errors,
}

with open("test_runner_result.json", "w", encoding="utf-8") as f:
    json.dump(res, f, indent=2, ensure_ascii=False)

with open("test_runner_result.yaml", "w", encoding="utf-8") as f:
    yaml.dump(res, f, allow_unicode=True, sort_keys=False)

root = ET.Element("report")
ET.SubElement(root, "total").text = str(total)
ET.SubElement(root, "passed").text = str(passed)
ET.SubElement(root, "failed").text = str(failed)
ET.SubElement(root, "percentage").text = str(percentage)

errors_el = ET.SubElement(root, "errors")

for er in errors:
    ET.SubElement(errors_el, "error").text = er

tree = ET.ElementTree(root)
with open("test_runner_result.xml", "wb") as f:
    tree.write(f, encoding="utf-8", xml_declaration=True)

print("Отчеты успешно сохранены в JSON, YAML и XML")
