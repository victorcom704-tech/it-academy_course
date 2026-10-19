import re

# 1
# def even_numbers(iterable):
#     for i in iterable:
#         if i % 2 == 0:
#             yield i


# print(list(even_numbers([1, 2, 3, 4, 5, 6])))


# 2
# def filter_lines(path, keyword):
#     with open(path) as f:
#         for line in f:
#             if keyword in line:
#                 yield line.strip()


# for line in filter_lines("app.log", "ERROR"):
#     print(line)


# 3
# def chain(iter1, iter2):
#     for i in iter1:
#         yield i

#     for i in iter2:
#         yield i


# print(list(chain([1, 2], [3, 4])))


# 4
# def counter(start=0):
#     while True:
#         yield start
#         start += 1


# c = counter(10)
# print(next(c))
# print(next(c))
# print(next(c))


# 5
# def counter(start=0):
#     while True:
#         yield start
#         start += 1


# def takke(n, iterable):
#     for i in range(n):
#         yield next(iterable)


# c = counter(100)
# print(list(takke(5, c)))

# 6
# s = "one two three\tfour"
# res = re.sub(r"\s+", ",", s)
# print(res)

# 7
# emails = ["a@test.com", "b@mail.ru", "user@sub.example.org"]
# domains = [re.search(r"@(.+)", email).group(1) for email in emails]
# print(domains)


# 8
# def is_valid_date(date: str) -> bool:
#     pattern = r"^\d{4}-\d{2}-\d{2}$"
#     return re.match(pattern, date) is not None


# assert is_valid_date("2025-12-23")
# assert not is_valid_date("25-12-23")

# 9
# log = '127.0.0.1 - - "GET /api/v1/users HTTP/1.1" 200 123 "-"'
# m = re.search(r'"\s+(\d{3})', log)
# res = m.group(1) if m else None
# print(res)


# 10
# def is_strong_password(password: str) -> bool:
#     if len(password) < 8:
#         return False

#     if re.search(r"[A-Z]", password) is None:
#         return False

#     if re.search(r"\d", password) is None:
#         return False

#     return True


# assert is_strong_password("Abcdef12")
# assert not is_strong_password("abcdef12")
# assert not is_strong_password("Abcdefgh")

# 11
# text = "<p>Hello <b>world</b>!</p>"
# res = re.sub(r"<.*?>", "", text)
# print(res)

# 12
# s = "name=John; age=30; city=London;"
# res = dict(re.findall(r"(\w+)=(\w+)", s))
# print(res)


# 13
# def find_phones(text):
#     pattern = r"(?:\+7|8)(?:[\s-]?\(?\d{3}\)?){1,2}[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}"
#     return re.findall(pattern, text)


# text = "Мой телефон: +7-999-123-45-67, офис: 8 (812) 555-66-77."
# print(find_phones(text))

# 14
# text = "one,two;three four"
# result = re.split(r"[ ,;]+", text)
# print(result)

# 15
# url = "/api/v1/users/123/orders/456"
# m = re.search(r"users/(\d+)/orders/(\d+)", url)
# result = m.groups() if m else None
# print(result)
