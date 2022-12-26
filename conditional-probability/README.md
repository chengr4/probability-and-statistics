# Conditional Probability 條件機率

> 機率常反映我們對於事件的了解程度

$$P(X|Y) = \frac{P(X \cap Y)}{P(Y)}$$

> P of X given Y

- X: 所關心的事件
- Y: 已知的事件 (條件)

> If outcome `o` and `Y` are mutually exclusive, then $P(o|Y) = 0$

## Atributes

## Total Probability Theorem

$$P(A) = \sum_{i=1}^{n} P(A|C_i)P(C _i)$$

## Bayes' Theorem

若 $C_1$, $C_2$, ..., $C_n$ 是一組互斥且完整的事件，且 $C_1 \cup C_2 \cup C_3 \cup ... \cup C_n = S $ ，則對任意事件 $A$ 有

$$P(C_j|A) = \frac{P(A|C_j)P(C_j)}{\sum_{i=1}^{n} P(A|C_i)P(C_i)}$$

### When to use?

- 要把條件轉成關心的事件的時候
