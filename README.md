# NGender

根据中文姓名猜测其性别

- 不到20行纯Python代码(核心部分)
- 无任何依赖库
- 兼容python3, python2, pypy
- 82%的准确率
- 可用于猜测性别
- 也可用于判断名字的男性化/女性化程度

## 使用

> pip install ngender

或者(OSX)

> brew install https://raw.githubusercontent.com/observerss/homebrew/61b3623967dc9507958dfb517e7f746baa96dcf1/Library/Formula/ngender.rb

然后在命令行中

```bash
$ ng 赵本山 宋丹丹
name: 赵本山 => gender: male, probability: 0.9836229687547046
name: 宋丹丹 => gender: female, probability: 0.9759486128949907
```

当然也可以在Python程序中用

```py
>>> import ngender
>>> ngender.guess('赵本山')
('male', 0.9836229687547046)

>>> ngender.guess('宋丹丹')
('female', 0.9759486128949907)

>>> %timeit guess('宋丹丹')
100000 loops, best of 3: 4.01 µs per loop
```

## 原理

### 数学

贝叶斯公式: ```P(Y|X) = P(X|Y) * P(Y) / P(X)```

当X条件独立时, ```P(X|Y) = P(X1|Y) * P(X2|Y) * ...```

应用到猜名字上

```
P(gender=男|name=本山) 
= P(name=本山|gender=男) * P(gender=男) / P(name=本山)
= P(name has 本|gender=男) * P(name has 山|gender=男) * P(gender=男) / P(name=本山)
```

### 计算

0. 文件`charfreq.csv`是怎么来的?
 
	曾经有个东西叫开房记录.avi(雾)，里面有名字和性别, 2000w条, 统计一下得出

0. 怎么算 `P(name has 本|gender=男)`?
 
	“本”在男性名字中出现的次数 / 男性字出现的总次数
	
0. 怎么算 `P(gender=男)`?
 
	男性名出现的次数 / 总次数

0. 怎么算 `P(name=本山)`?
 
	不用算, 在算概率的时候会互相约去
	


## 坑

```py
>>> ngender.guess('李胜男')
('male', 0.851334658742)
```

虽然两个字都很偏男性，但是结合起来就是女性名

