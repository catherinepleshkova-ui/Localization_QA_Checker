import csv
import re
from collections import Counter

# Находим переменные вида {gold}, {player_name}
PLACEHOLDER_PATTERN = re.compile(r"\{[^{}]+\}")


def find_placeholders(text):
    return Counter(PLACEHOLDER_PATTERN.findall(text))


with open("game_strings.csv", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    issues_found = 0

    for row in reader:
        source = row["source"]
        target = row["target"]

        source_placeholders = find_placeholders(source)
        target_placeholders = find_placeholders(target)

        if source_placeholders != target_placeholders:
            issues_found += 1

            print("ОШИБКА: несоответствие переменных")
            print("ID:", row["id"])
            print("Оригинал:", source)
            print("Перевод:", target)
            print("В оригинале:", dict(source_placeholders))
            print("В переводе:", dict(target_placeholders))
            print("-" * 40)

    print("Проверка завершена.")
    print("Найдено проблем:", issues_found)