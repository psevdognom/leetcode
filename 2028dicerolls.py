# https://leetcode.com/problems/find-missing-observations/description/?envType=daily-question&envId=2025-01-29

class Solution(object):
    def missingRolls(self, rolls, mean, n):
        m = len(rolls)
        total_sum = mean * (n + m)  # Загальна сума всіх кидків
        known_sum = sum(rolls)  # Сума відомих кидків
        missing_sum = total_sum - known_sum  # Сума відсутніх кидків

        # Перевірка, чи можлива така сума для відсутніх кидків
        if missing_sum < n or missing_sum > 6 * n:
            return []  # Якщо сума виходить за межі, неможливо знайти відсутні кидки

        # Розподіляємо суму на n відсутніх кидків
        result = [1] * n  # Початково присвоюємо кожному значенню 1
        missing_sum -= n  # Залишок після того, як кожному кидку дали 1

        # Додаємо залишок по черзі до кожного кидка
        for i in range(n):
            add = min(missing_sum, 5) # Додаємо мінімальне значення, яке можна додати
            result[i] += add
            missing_sum -= add

        return result