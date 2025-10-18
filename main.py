from typing import Callable, Dict, List

def iterative_binary_tree(
        height: int,
        root: int,
        left_leaf: Callable[[int], int] = lambda x: 2 - (x - 1),
        right_leaf: Callable[[int], int] = lambda x: x * 2
) -> Dict[str, List]:
    """
    Создаёт бинарное дерево в виде словаря (нерекурсивно)

    Параметры:
        height (int): Высота дерева — количество шагов рекурсии.
                      Если height = 0, создаётся только корень.
        root (int): Начальное значение (корень дерева).
        left_leaf(Callable[[int], int]): Функция для вычисления левого потомка.
        right_leaf (Callable[[int], int]): Функция для вычисления правого потомка.

    Возвращает:
        Dict[str, List]: Словарь, представляющий бинарное дерево.
                         Ключ — строковое значение корня,
                         значение — список потомков (поддеревьев).
    """
    # Высота не может быть отрицательной
    if height < 0:
        return {}
    # Высота 0: только корень
    if height == 0:
        return {str(root): []}
    tree = {str(root): []}
    current_level = [(root, str(root))]

    for _ in range(height - 1):
        next_level = []
        for root_value, key in current_level:
            left_val = left_leaf(root_value)
            right_val = right_leaf(root_value)

            tree[str(left_val)] = []
            tree[str(right_val)] = []
            tree[key].append({str(left_val): tree[str(left_val)]})
            tree[key].append({str(right_val): tree[str(right_val)]})

            next_level.append((left_val, str(left_val)))
            next_level.append((right_val, str(right_val)))

        current_level = next_level

    return {str(root): tree[str(root)]}
