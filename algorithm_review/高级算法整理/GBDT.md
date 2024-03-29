

### GBDT:gradient boosting decision tree 梯度增强决策树

GBDT是一种采用加法模型（即基函数的线性组合）与前向分步算法并以决策树作为基函数的提升方法。通俗来说就是，该算法由多棵决策树组成，所有树的结论加起来形成最终答案。

### 前向分布算法 ###

- 加法模型

![img](https://camo.githubusercontent.com/8d313a2a648a6b17d882a3cd0be9c96c0b288e12/68747470733a2f2f692e696d6775722e636f6d2f33786e4c7665672e706e67)

- 流程

![img](https://camo.githubusercontent.com/28195207523a186575b523a76113ecfb4ddc8475/68747470733a2f2f692e696d6775722e636f6d2f4235474a3245332e706e67)



### 负梯度拟合

Gradient Boost与传统的Boost的区别是，每一次的计算是为了减少上一次的残差(residual)，而为了消除残差，我们可以在残差减少的梯度(Gradient)方向上建立一个新的模型。所以说，在Gradient Boost中，每个新的模型的简历是为了使得之前模型的残差往梯度方向减少，与传统Boost对正确、错误的样本进行加权有着很大的区别

![img](https://camo.githubusercontent.com/a21f6f5aa98ea1bf1b0e0cadaa35408059ac60dc/68747470733a2f2f692e696d6775722e636f6d2f4e7853577836472e706e67)

### 损失函数 ###

![img](https://camo.githubusercontent.com/bd3dc509aea5f4e54920c87ce3eced63bda8ba36/68747470733a2f2f692e696d6775722e636f6d2f4644564f46696c2e706e67)

### 回归 ###

- GBDT之回归树

  ![img](https://camo.githubusercontent.com/f45c9ac15228f949cea22da1e27805eb9a2b64ce/68747470733a2f2f692e696d6775722e636f6d2f324d4a634d53482e706e67)

### 二分类，多分类 ###

- GBDT之分类树

​	在分类问题中，有一个很重要的内容叫做Multi-Class Logistic，也就是多分类的Logistic问题，它适用于那些类别数>2的问题，并且在分类结果中，样本x不是一定只属于某一个类可以得到样本x分别属于多个类的概率（也可以说样本x的估计y符合某一个几何分布），这实际上是属于Generalized Linear Model中讨论的内容，这里就用一个结论：如果一个分类问题符合几何分布，那么就可以用Logistic变换来进行之后的运算。
​	GBDT分类算法思想上和GBDT的回归算法没有什么区别，但是由于样本输出不是连续值，而是离散类别，导致我们无法直接从输出类别去拟合类别输出误差。为了解决这个问题，主要有两种方法。一是用指数损失函数，此时GBDT算法退化为AdaBoost算法。另一种方法是用类似于逻辑回归的对数似然损失函数的方法。也就是说，我们用的是类别的预测概率值和真实概率值的差来拟合损失。当损失函数为指数函数时，类似于AdaBoost算法，这里不做介绍，下面介绍损失函数为log函数时的GBDT二分类和多分类算法。

### 正则化 ###

- 1 CART树的剪枝
- 2 设置步长η, 。参数：Shrinkage–>(0, 1] 即在每一轮迭代获取最终学习器的时候按照一定的步长进行更新。其中0<η≤1是步长，对于同样的训练集学习效果，较小的η意味着需要更多的迭代次数；通常用步长和迭代最大次数一起来决定算法的拟合效果。参数：Shrinkage 注：步长如何设置才能防止过拟合？ 因为较小的η意味着需要更多的迭代次数，防止过拟合就要稍微加大步长，用步长和迭代最大次数一起来决定算法的拟合效果。
- 3 子采样。 参数subsample–>(0, 1]。这里是不放回随机抽样。选择小于1的比例可以减少方差，即防止过拟合，但是会增加样本拟合的偏差，因此取值不能太低，一般在[0.5, 0.8]之间。	GBDT子采样的过程：比如有100个样本，subsample=0.8，第一棵树训练时随机从100个样本中抽取80%，有80个样本训练模型；第二棵树再在100个样本再随机采样80%数据，也就是80个样本，训练模型；以此类推。

### 优缺点 ###

- 优点：
  - 预测精度高
  - 适合低维数据
  - 能处理非线性数据
  - 可以灵活处理各种类型的数据，包括连续值和离散值。
  - 在相对少的调参时间情况下，预测的准备率也可以比较高。这个是相对SVM来说的。
  - 使用一些健壮的损失函数，对异常值的鲁棒性非常强。比如 Huber损失函数和Quantile损失函数。
- 缺点：
  - 由于弱学习器之间存在依赖关系，难以并行训练数据。不过可以通过自采样的SGBT来达到部分并行。
  - 如果数据维度较高时会加大算法的计算复杂度

### sklearn参数 ###

### 应用场景 ###

