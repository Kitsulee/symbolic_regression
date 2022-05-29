from src.constants import ZERO


def safe_div(a, b):
    return a / b if abs(b) >= ZERO else a if abs(b) >= ZERO else 1


ADD = {
    "func": lambda a, b: a + b,
    "arg_count": 2,
    "format_str": lambda a, b: f"({a} + {b})",
}
SUB = {
    "func": lambda a, b: a - b,
    "arg_count": 2,
    "format_str": lambda a, b: f"({a} - {b})",
}
MUL = {
    "func": lambda a, b: a * b,
    "arg_count": 2,
    "format_str": lambda a, b: f"({a} * {b})",
}
DIV = {"func": safe_div, "arg_count": 2, "format_str": lambda a, b: f"({a} / {b})"}
NEG = {
    "func": lambda a: -a,
    "arg_count": 1,
    "format_str": lambda a: f"-({a})",
}
