def stream_user_ages():
    """
    Generator that yields user ages one at a time.
    """
    users = [
        {'age': 67},
        {'age': 119},
        {'age': 49},
        {'age': 22},
        {'age': 102},
        {'age': 116},
        # Add more user dicts here if needed
    ]
    for user in users:
        yield user['age']


def calculate_average_age():
    """
    Calculates the average age using the generator stream_user_ages().
    """
    total_age = 0
    count = 0

    for age in stream_user_ages():  # Loop 1
        total_age += age
        count += 1

    if count == 0:
        return 0

    return total_age / count


if __name__ == "__main__":
    avg_age = calculate_average_age()
    print(f"Average age of users: {avg_age:.2f}")
