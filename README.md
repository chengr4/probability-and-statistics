# Probability and Statistics

- [Three Axios of Probability 機率三公理](#three-axios-of-probability-機率三公理)
- [Conditional Probability 條件機率](./conditional-probability/)
- [Independent Events](#independent-events)
- [Counting](#counting)
- [Random Variables](./random-variable/)

## 統計常用圖表

- 散佈圖：兩個變數的關係

## Three Axioms of Probability 機率三公理

1. For any event A, P(A) >= 0
2. P(S) = 1 (S = 樣本空間)
3. if events A1, A2, ... 互斥 (互斥：不可能同時發生) => P(A1⋃A2⋃A3...) = P(A1)+P(A2)+P(A3)...

### Derived from three axioms

- P(∅) = 0: Empty set
  ```math
  S \cap ∅ = ∅: S, ∅ mutually exclusive
  加以 S \cup ∅ = S
  => P(S) = P(S \cup ∅) = P(S) + P(∅)
  => P(∅) = 0
  ```
- P(A) + P(A') = 1: Complement
- P(A) = P(A-B) + P(A∩B): DeMorgan's Law
- P(A⋃B) = P(A) + P(B) - P(A∩B): Union and Intersection
- If $A \in B$ => P(A) <= P(B): Inclusion-Exclusion Principle
- Bool's Inequality: n個事件的連集機率 <= n個事件的機率之和
- Bonferroni's Inequality: n個事件交集的機率 >= 1 - n個事件補集的機率之和

## Independent Events

$$ P(A | B) = P(A) $$

> I love this formula, it's so simple and elegant.

多事件的獨立:

在 n 個事件中任取 m 個事件，若**全部**皆滿足:

$$ P(A_1 \cap A_2, \cap ..., \cap A_m) = P(A_1)P(A_2)...P(A_m) $$

則稱這 n 個事件為獨立事件。

若 n = 5，要計算 $\binom{5}{2} + \binom{5}{3} + \binom{5}{4} + \binom{5}{5}$ 種事件

## Counting

### Before Counting

- Distinguishable
- With/Without Replacement
- Order matters or not

## Run python code

1. activate virtualenv

```bash
source .venv/bin/activate
```

```
deactivate
```

2. Run python code

```bash
python <filename>.py
```