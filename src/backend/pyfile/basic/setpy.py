set_list = ["a", "b", "c", "d", "a", "b"]

# 重複文字を取り除く(set型変換)
set_sort = set(set_list) 
print(set_sort)

# リスト型に変換(list型変換)
sList = list(set_sort)
print(sList)

# set型に対して値を追加(add)
set_sort.add("12345")
print(set_sort)

# set型の中身を削除(remove)
set_sort.remove("a")
print(set_sort)