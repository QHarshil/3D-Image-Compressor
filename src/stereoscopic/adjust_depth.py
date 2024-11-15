def get_offset(depth):
    """
    Returns the offset value based on the specified depth level.

    Args:
        depth (str): Depth level ('close', 'medium', or 'far').

    Returns:
        int: Offset value.
    """
    offset_map = {"close": 30, "medium": 15, "far": 5}
    return offset_map.get(depth, 15)
