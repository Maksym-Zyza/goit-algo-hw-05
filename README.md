# Алгоритмічне порівняння: Пошук підрядка

## Вхідні дані
Порівнювалися три алгоритми пошуку підрядка:

- **Boyer-Moore**
- **Кнут-Морріс-Пратт (KMP)**
- **Рабін-Карп (Rabin-Karp)**

Тести проводилися на двох текстових файлах (`article_1.txt` та `article_2.txt`) із двома підрядками:

- Існуючий підрядок: `"інтервал sqrt"`
- Неіснуючий підрядок: `"nonexistent123"`

---

## Результати вимірювання (в секундах)

### 📄 article_1.txt

| Алгоритм      | Існуючий | Неіснуючий |
|---------------|----------|-------------|
| Boyer-Moore   | 0.021363 | 0.025968    |
| KMP           | 0.072406 | 0.121424    |
| Rabin-Karp    | 0.084913 | 0.207180    |

✅ **Найшвидший:** Boyer-Moore (обидва випадки)

---

### 📄 article_2.txt

| Алгоритм      | Існуючий | Неіснуючий |
|---------------|----------|-------------|
| Boyer-Moore   | 0.045710 | 0.035514    |
| KMP           | 0.215088 | 0.176961    |
| Rabin-Karp    | 0.296571 | 0.299108    |

✅ **Найшвидший:** Boyer-Moore (обидва випадки)

---

## Загальний висновок

📌 **Boyer-Moore** є найшвидшим алгоритмом у всіх протестованих випадках — як для існуючих, так і для неіснуючих підрядків у кожному з текстів.
