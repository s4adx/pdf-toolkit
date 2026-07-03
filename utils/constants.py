# ==========================
# WINDOW
# ==========================

class Window:
    TITLE = "PDF Toolkit"

    WIDTH = 800
    HEIGHT = 600

    ICON = None


# ==========================
# COLORS
# ==========================

class Colors:

    # Main
    BACKGROUND = "#1E293B"
    SURFACE = "#334155"

    # Primary
    PRIMARY = "#60A5FA"
    PRIMARY_HOVER = "#3B82F6"

    # Text
    TEXT_PRIMARY = "#F8FAFC"
    TEXT_SECONDARY = "#CBD5E1"

    # Borders
    BORDER = "#475569"

    # Status
    SUCCESS = "#22C55E"
    ERROR = "#EF4444"
    WARNING = "#F59E0B"

    # Cards
    CARD = "#334155"
    CARD_HOVER = "#475569"


# ==========================
# FONTS
# ==========================

class Fonts:

    FAMILY = "Segoe UI"

    TITLE = (FAMILY, 24, "bold")
    HEADING = (FAMILY, 16, "bold")
    SUBHEADING = (FAMILY, 13, "bold")
    BODY = (FAMILY, 11)
    SMALL = (FAMILY, 10)
    BUTTON = (FAMILY, 11, "bold")


# ==========================
# SPACING
# ==========================

class Spacing:

    XS = 5
    SMALL = 10
    MEDIUM = 20
    LARGE = 30
    XL = 40


# ==========================
# BUTTONS
# ==========================

class ButtonStyle:

    WIDTH = 18
    HEIGHT = 2


# ==========================
# TOOL CARDS
# ==========================

class CardStyle:

    WIDTH = 170
    HEIGHT = 130
    PADDING = 15