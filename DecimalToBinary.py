def decimal_to_binary(decimal: int) -> str:
    """Converts an integer from decimal to its binary representation."""
    if decimal == 0:
        return "0"
    binary_str = ""
    while decimal > 0:
        remainder = decimal % 2
        binary_str = str(remainder) + binary_str  # sett á undan the remainder sem string
        decimal = decimal // 2
    return binary_str


