def moving_average(numbers_list, window_size):
    if window_size <= 0:
        raise ValueError("Размер окна должен быть больше нуля")

    result = []
    for i in range(len(numbers_list) - window_size + 1):
        result.append(sum(numbers_list[i:i + window_size]) / window_size)
    return result


if __name__ == "__main__":
    examples = [
        ([2, 12, 7, 8, 0], 3),
        ([1, 2, 3, 4, 5], 2),
        ([-3, 0, 3, 6], 3),
        ([10, 20, 30], 1),
        ([10, 20, 30], 3),
    ]

    for numbers_list, window_size in examples:
        result = moving_average(numbers_list, window_size)
        print(f"Список: {numbers_list}, окно: {window_size}, результат: {result}")
