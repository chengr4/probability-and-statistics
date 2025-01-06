# Probability and Statistics

How to use this repository:

The main content is provided in the **PDF**, with supplementary information available in the **Markdown** file

## 統計常用圖表

- 散佈圖：兩個變數的關係

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