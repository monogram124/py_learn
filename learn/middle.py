# средний уровень

# СЛОВАРИ - еще один тип коллекций, который позволяет сопоставлять произвольные ключи со значениями, так же как и списки могут быть проиндексированы

ages = {
    "Dave": 24,
    "Mary": 42,
    "John": 58
}
ages["Dave"] # 24
ages["John"] # 58

# функции словарей
# чтобы определить находиться ли ключ в словаре можно использовать in или not in

nums = {
    1: "one",
    2: "two",
    3: "three"
}

print(1 in nums) # True
print("three" in nums) # False
print(4 not in nums) # True

# get(), по сути делает то же самое что и индексирование но если не нашел нужный элемент возрващает значение стоящее вторым аргуентом
print(nums.get(4, "not found"))

# КОРТЕЖИ TURPLES ТЮРПЛЫ, очень похожи на списки, но их нельзя изменить

words = ("spam", "eggs", "sausages")
print(words[0]) # если бы я попробовал переназначить значение words[1] = "cheese", это привело бы к ошибке

# так же кортеж можно создать и без использования скобок, просто отделяя запятыми
my_tuple = "one", "two", "three"

# распаковка кортежа, позволяет присвоить каждому элементу в коллецкции переменную
numbers = [1, 2, 3, 4]
a, *b, c = numbers # если переменная со звездочкой то ей будут присвоены значения лиюо до конца лиюо до следующей перменной

# SETS или МНОЖЕСТВА, похожи на списки и словари, но они не упорядочены что значит что не могут быть проиндексированы, так же множества не могут сожержать дубликаты элементов
num_set = {1, 2, 3, 4, 5}
print(3 in nums)

num_set.add(-7) # добавить элемент
num_set.remove(2) # удалить элемент
print(nums) # 1, 3, 4, 5, -7

# повторяющиеся элементы будут автоматически удалены из множества

# множества могут быть объединены использую мат операторы
first = {1, 2, 3}
second = {4, 5, 6}

print(first | second) # склеит два множества {1, 2, 3, 4, 5, 6}
print(first & second) # выводит те элементы которые есть в обоих множествах {}
print(first - second) # выводит те элементы которые есть в первом множестве но нет во втором
print(second - first) # наборот
print(first ^ second) # ???

# СПИСКОВОЕ ВКЛЮЧЕНИЕ
