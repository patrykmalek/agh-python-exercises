class CommonFunction:
    @staticmethod
    def create_bordered_string(text, length=60, fill_char='-'):
        if len(text) > length:
            return text[:length]
        remaining_length = length - len(text)
        left_fill = fill_char * (remaining_length // 2)
        remaining_length = remaining_length - len(left_fill)
        right_fill = fill_char * remaining_length
        return f"{left_fill}{text}{right_fill}"
