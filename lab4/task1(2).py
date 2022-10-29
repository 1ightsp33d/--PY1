def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = str_.lower()
    nstr = [str_[i] for i in range(len(str_))]
    return {nstr[i]: nstr.count(nstr[i]) for i in range(len(nstr)) if (nstr[i].isalpha() and nstr[i] != nstr[i-1])}
#M355 WI7H 7H3 6357 Di3 1ik3 7h3 R357


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
