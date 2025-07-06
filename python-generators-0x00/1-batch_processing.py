def stream_users_in_batches(batch_size=25):
    """
    Simulate streaming users in batches from a data source, like:
    SELECT * FROM user_data LIMIT batch_size OFFSET ...
    """
    # Simulated user data (could be loaded from a DB or file in a real app)
    user_data = [
        {'user_id': '00234e50-34eb-4ce2-94ec-26e3fa749796', 'name': 'Dan Altenwerth Jr.', 'email': 'Molly59@gmail.com', 'age': 67},
        {'user_id': '006bfede-724d-4cdd-a2a6-59700f40d0da', 'name': 'Glenda Wisozk', 'email': 'Miriam21@gmail.com', 'age': 119},
        {'user_id': '006e1f7f-90c2-45ad-8c1d-1275d594cc88', 'name': 'Daniel Fahey IV', 'email': 'Delia.Lesch11@hotmail.com', 'age': 49},
        {'user_id': '00af05c9-0a86-419e-8c2d-5fb7e899ae1c', 'name': 'Ronnie Bechtelar', 'email': 'Sandra19@yahoo.com', 'age': 22},
        {'user_id': '00cc08cc-62f4-4da1-b8e4-f5d9ef5dbbd4', 'name': 'Alma Bechtelar', 'email': 'Shelly_Balistreri22@hotmail.com', 'age': 102},
        {'user_id': '01187f09-72be-4924-8a2d-150645dcadad', 'name': 'Jonathon Jones', 'email': 'Jody.Quigley-Ziemann33@yahoo.com', 'age': 116},
        # You can add more simulated users here...
    ]

    total = len(user_data)
    offset = 0

    while offset < total:
        # Simulate SQL-like batch selection:
        batch = user_data[offset : offset + batch_size]  # SELECT * FROM user_data LIMIT batch_size OFFSET offset
        if not batch:
            break
        for user in batch:
            yield user
        offset += batch_size


def batch_processing(batch_size=25):
    """
    Processes users in batches greater than batch_size, yielding each user.
    """
    # Use stream_users_in_batches to get users lazily
    for user in stream_users_in_batches(batch_size):
        # You could add additional processing/filtering here if needed, e.g.:
        if user['age'] > 0:  # Example condition: age > 0
            yield user

    return  # Explicitly returning None at the end (optional)
