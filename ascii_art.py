def add_border(message):
    # 테두리를 추가
    bordered_message = f"""
    ╔{'═' * len(message)}╗
    ║{message}║
    ╚{'═' * len(message)}╝
    """
    return bordered_message
