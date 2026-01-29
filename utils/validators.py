def validate_name(text: str) -> bool:
    return text.replace(" ", "").isalpha()
