
import pandas as pd
import random

# создаем DataFrame с 1 столбцом
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# переводим столбец в one hot вид
one_hot_data = pd.get_dummies(data, columns=['whoAmI'])
one_hot_data.head()