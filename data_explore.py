import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split

data = pd.read_csv('D:/code/datawhale/data.csv', encoding='gbk')

#数据类型的分析
cor=data.corr()
print(cor['status'][abs(cor['status'])<0.01])

#无关特征的删除
data=data.drop(['Unnamed: 0', 'custid', 'trade_no', 'bank_card_no', 'source', 'id_name'], axis=1, inplace=True)
print(data.shape)
# 数据类型转换
data = pd.get_dummies(data)
#缺失值处理用均值填充
data = data.fillna(data.mean())

#划分数据集
train_data, test_data = train_test_split(data, test_size=0.3, random_state=2018)
train_data.to_csv('x_train.csv', index=False, header=True)
test_data.to_csv('x_test.csv', index=False, header=True)