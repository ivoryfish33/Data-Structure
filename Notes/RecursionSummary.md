# 6.4 递归小结

递归是解决某些具有自相似性的复杂问题
- 某些情况下，递归可以代替迭代循环(for, while)
- 递归算法能够和问题的表达自然契合
- 递归不总是最优算法，有时候递归有引发巨量的重复计算
- “记忆化/函数值缓存”可以通过附加储存空间记录中间计算结果来有效减少重复计算（查表）
- 如果一个问题最优解包括规模更小的相同问题的最优解，可以用动态规划来解决

### 递归三定律
- 递归算法必须具有基本结束条件
- 递归算法必须要减小规模，改变状态，向基本结束条件演进
- 递归算法必须调用自身



