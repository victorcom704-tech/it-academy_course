# 1
# class TestCase:

#     def __init__(self, name, status):
#         self.name = name
#         self.status = status

#     def __str__(self):
#         return f"Test '{self.name}' [{self.status}]"

#     def __repr__(self):
#         return f"TestCase(name={self.name!r}, status={self.status!r})"


# t = TestCase("test_login", "passed")
# print(t)
# print([t])


# 2
# class TestSuite:

#     def __init__(self, tests):
#         self.tests = tests

#     def __len__(self):
#         return len(self.tests)

#     def __bool__(self):
#         return len(self.tests) > 0


# suite = TestSuite(["test_login", "test_signup"])
# print(len(suite))
# if suite:
#     print("Suite не пустой")


# 3
# class Result:
#     def __init__(self):
#         self._data = {}

#     def __getitem__(self, test_name):
#         return self._data[test_name]

#     def __setitem__(self, test_name, status):
#         self._data[test_name] = status


# results = Result()
# results["test_login"] = "passed"
# print(results["test_login"])


# 4
# class TestSuite:
#     def __init__(self, tests):
#         self.tests = tests

#     def __iter__(self):
#         return iter(self.tests)


# for t in TestSuite(["test_login", "test_signup"]):
#     print(t)


# 5
# class Duration:
#     def __init__(self, seconds):
#         self.seconds = seconds

#     def __add__(self, other):
#         return Duration(self.seconds + other.seconds)

#     def __str__(self):
#         return f"{self.seconds:.2f} сек"


# t1 = Duration(1.5)
# t2 = Duration(2.3)
# print(t1 + t2)


# 6
# class TestRunner:
#     def __init__(self, tests):
#         self.tests = tests

#     def __call__(self):
#         print("Запуск тестов:")
#         for t in self.tests:
#             print(f"-{t}")


# runner = TestRunner(["test_login", "test_logout"])
# runner()


# 7
# class Version:
#     def __init__(self, major, version):
#         self.major = major
#         self.version = version

#     def __eq__(self, other):
#         return (self.major, self.version) == (other.major, other.version)

#     def __lt__(self, other):
#         return (self.major, self.version) < (other.major, other.version)


# v1 = Version(1, 2)
# v2 = Version(1, 3)
# print(v1 < v2)
# print(v1 == v2)
