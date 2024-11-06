str = input()
if ":)" in str:
    str = str.replace(":)", "🙂")
if ":(" in str:
    str = str.replace(":(", "🙁")
print(str)
# we also can use Unicode Characters!
