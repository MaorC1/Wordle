# ANSI escape codes for bold and colors
class TextStyle:
    # Regular text styles
    RESET = "\033[0m"       # reset all attributes
    BOLD = "\033[1m"        # bold

    # Regular text colors
    DEFAULT = "\033[39m"    # default text color
    BLACK = "\033[30m"      # black
    RED = "\033[31m"        # red
    GREEN = "\033[32m"      # green
    YELLOW = "\033[33m"     # yellow
    BLUE = "\033[34m"       # blue
    MAGENTA = "\033[35m"    # magenta
    CYAN = "\033[36m"       # cyan
    WHITE = "\033[37m"      # white

    @staticmethod
    def color_letter(text, color, is_bold=False):
        # Determine bold style
        bold_code = TextStyle.BOLD if is_bold else ""

        # Get color escape code
        color_code = getattr(TextStyle, color.upper(), TextStyle.DEFAULT)

        # Combine style, color, and text with reset
        painted_text = f"{bold_code}{color_code}{text}{TextStyle.RESET}"

        return painted_text

