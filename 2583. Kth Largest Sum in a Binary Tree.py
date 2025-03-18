from collections import deque


def level_sums(tree):
    if not tree:
        return []

    result = []
    queue = deque([0])  # Починаємо з індексу 0 (корінь)

    while queue:
        level_size = len(queue)  # Кількість елементів на поточному рівні
        level_sum = 0

        for _ in range(level_size):
            index = queue.popleft()

            if index >= len(tree) or tree[index] is None:
                continue

            level_sum += tree[index]  # Додаємо значення поточного вузла

            # Додаємо лівого і правого нащадка до черги
            left_index = 2 * index + 1
            right_index = 2 * index + 2

            if left_index < len(tree) and tree[left_index] is not None:
                queue.append(left_index)

            if right_index < len(tree) and tree[right_index] is not None:
                queue.append(right_index)

        result.append(level_sum)  # Додаємо суму поточного рівня

    return result