# Data application

## The Empirical Rule

> A.k.a. the 68-95-99.7 rule

### Conditions

1. Continuous data
2. Normal distribution (skewness and kurtosis are close to 0)

### What can do

1. Find the outliers `$\mu +- 3 \sigma$`

## The Chebyshev's Rule

### Conditions

1. Continuous data

> **It does not need to care about the distribution!**


### What can do

At least $(1 - \frac{1}{k^2}) * 100%$ of the data falls within $ \mu +- k\sigma$ => can find the outliers

## Box Plot

### What can do

- Find the outliers: $Q1 - 1.5 * IQR$ and $Q3 + 1.5 * IQR$

## Z-Score

Formula: $Z = \frac{X - \mu}{\sigma}$

- Z +- 1 => 68%
- Z +- 2 => 95%
- Z +- 3 => 99.7% => outliers

### Conditions

1. Continuous data
2. Normal distribution (skewness and kurtosis are close to 0)

