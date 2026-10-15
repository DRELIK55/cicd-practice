"""
Простой калькулятор для демонстрации CI/CD pipeline.
"""


class Calculator:
    """Класс с базовыми арифметическими операциями."""

    def add(self, a, b):
        """Сложение двух чисел."""
        return a + b

    def subtract(self, a, b):
        """Вычитание: a - b."""
        return a - b

    def multiply(self, a, b):
        """Умножение двух чисел."""
        return a * b

    def divide(self, a, b):
        """Деление a на b. Бросает ValueError при делении на ноль."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        """Возведение a в степень b."""
        return a ** b
