# Define an in_list function that accepts a list of strings and a separate string.

# Return the index where the string exists in the list. If the string does not exist, return -1.

# Do NOT use the find or index methods.

# strings = ["enchanted", "sparks fly", "long live"]
# in_list(strings, "enchanted")  ==> 0
# in_list(strings, "sparks fly") ==> 1
# in_list(strings, "fifteen")    ==> -1
# in_list(strings, "love story") ==> -1


# def in_list(words, search_for):
#     for index, word in enumerate(words):
#         if word == search_for:
#            return index
#         else:
#            return -1

def in_list(words, target):
    for index, word in enumerate(words):
        if word == target:
            return index

    return -1


print(in_list(["enchanted", "sparks fly", "long live"], "enchanted"))
print(in_list(["enchanted", "sparks fly", "long live"], "sparks fly"))
print(in_list(["enchanted", "sparks fly", "long live"], "fifteen"))
print(in_list(["enchanted", "sparks fly", "long live"], "love story"))
