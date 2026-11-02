import numpy as np

def f(x):
    return (x + 1) / (x + 2)

a, b = 0.0, 1.0
eps3 = 1e-4

# 2.1 с) Метод Сімпсона за правилом Рунге
m = 3
while True:
    n = 2 * m
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    I_s1 = (h / 3) * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]))

    m2 = 2 * m
    n2 = 2 * m2
    h2 = (b - a) / n2
    x2 = np.linspace(a, b, n2 + 1)
    y2 = f(x2)
    I_s2 = (h2 / 3) * (y2[0] + y2[-1] + 4 * np.sum(y2[1:-1:2]) + 2 * np.sum(y2[2:-2:2]))

    if abs(I_s2 - I_s1) / 15 <= eps3:
        I_simp = I_s2
        break
    m = m2

print(f"2.1. с) Метод Сімпсона: I ≈ {I_simp:.5f} (n = {n2})")

# 2.2. Апріорні похибки
n_rect = 5
h_rect = (b - a) / n_rect
M2 = 0.25  # максимум |f''(x)| на [0, 1]
delta_rect = (M2 * (b - a) / 24) * (h_rect  2)
delta_trap = (M2 * (b - a) / 12) * (h_rect  2)

n_simp = 6
h_simp = (b - a) / n_simp
M4 = 1.5  # максимум |f^(4)(x)| на [0, 1]
delta_simp = (M4 * (b - a) / 180) * (h_simp ** 4)

print(f"2.2. а) Апріорна похибка прямокутників (n=5): Δ ≤ {delta_rect:.6f}")
print(f"2.2. b) Апріорна похибка трапецій (n=5): Δ ≤ {delta_trap:.6f}")
print(f"2.2. с) Апріорна похибка Сімпсона (n=6): Δ ≤ {delta_simp:.6f}")
