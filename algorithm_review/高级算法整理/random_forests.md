### 1、集成学习的概念

构建过个学习器完成学习任务

### 2、个体学习器的概念

构成集成学习的学习器

### 3、boosting bagging的概念、异同点

boosting的基本思想是不断拟合基础学习器的残差，其基础学习器通常偏差较高
bagging的基本思想是对样本进行有放回抽样构造不同的训练集训练基础学习器，其基础分类器通常方差较高

### 4、理解不同的结合策略(平均法，投票法，学习法)

平均法：所有学习器预测结果的平均值作为最终预测结果
投票法：所有学习器预测结果的众数最为最终预测结果
学习法：利用所有学习器的预测结果训练模型得到最终预测结果

### 5、随机森林的思想

基于bagging的思想，将决策树作为基础学习器，对样本进行有放回抽样构造不同的训练集，并且在决策树训练过程中引入随机属性的选择

### 6、随机森林的推广

sklearn.ensemble.ExtraTreesClassifier/ExtraTreeRegressor：随机选择划分点
sklearn.ensemble.IsolationForest：异常点检测

### 7、随机森林的优缺点

优点：良好的benchmark

缺点：随机森林已经被证明在某些噪音较大的分类或回归问题上会

### 8、随机森林在sklearn中的参数解释

n_estimators：基础分类器数量
criterion：划分衡量指标
max_depth：决策树最大深度
min_samples_split：决策树叶结点继续分裂最小样本数量
min_samples_leaf：决策树叶结点最小样本数量
min_weight_fraction_leaf：决策树叶结点最小加权样本数量
max_features：搜索划分时考虑的特征数量
max_leaf_nodes：决策树最大叶结点数量
min_impurity_decrease：决策树叶结点最小衡量指标提升
bootstrap：是否进行有放回取样
oob_score：是否通过未参加训练的样本估计模型效果
n_jobs：控制并行
random_state：随机种子
verbose：控制输出
warm_start：是否使用之前的输出
class_weight：类别权重
RandomForestRegressor类似

### 9、随机森林的应用场景

常见分类问题、回归问题均可使用随机森林

