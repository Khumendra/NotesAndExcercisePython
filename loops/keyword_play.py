import keyword

keyword_list = keyword.kwlist
key = 'for'
# print(* keyword.kwlist, sep=', ')

if key in keyword_list:
    print(keyword_list.index(key))