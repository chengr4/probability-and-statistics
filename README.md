# Probability

- [Three Axios of Probability 機率三公理](#three-axios-of-probability-機率三公理)
- [Conditional Probability 條件機率](./conditional-probability/)
- [Independent Events](#independent-events)

## Three Axios of Probability 機率三公理

1. For any event A, P(A) >= 0
2. P(S) = 1 (S = 樣本空間)
3. if events A1, A2, ... 互斥 (互斥：不可能同時發生) => P(A1⋃A2⋃A3...) = P(A1)+P(A2)+P(A3)...

### Derived from three axios

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

