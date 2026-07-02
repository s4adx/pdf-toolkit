
# WINDOW
class Window:
    TITLE = "PDF Toolkit"

    WIDTH = 1000
    HEIGHT = 650

    ICON = None

# COLORS
class Colors:

    # Main
    BACKGROUND = "#F5F7FA"
    SURFACE = "#FFFFFF"

    # Primary
    PRIMARY = "#2563EB"
    PRIMARY_HOVER = "#1D4ED8"

    # Text
    TEXT_PRIMARY = "#1F2937"
    TEXT_SECONDARY = "#6B7280"

    # Borders
    BORDER = "#D1D5DB"

    # Status
    SUCCESS = "#16A34A"
    ERROR = "#DC2626"
    WARNING = "#F59E0B"

    # Cards
    CARD = "#FFFFFF"
    CARD_HOVER = "#EEF4FF"


# FONTS
class Fonts:

    FAMILY = "Segoe UI"
    TITLE = (FAMILY, 22, "bold")
    HEADING = (FAMILY, 16, "bold")
    SUBHEADING = (FAMILY, 13, "bold")
    BODY = (FAMILY, 11)
    SMALL = (FAMILY, 10)
    BUTTON = (FAMILY, 11, "bold")


# SPACING
class Spacing:

    XS = 5
    SMALL = 10
    MEDIUM = 20
    LARGE = 30
    XL = 40


# BUTTONS
class ButtonStyle:

    WIDTH = 18
    HEIGHT = 2


# TOOL CARDS
class CardStyle:

    WIDTH = 220
    HEIGHT = 120
    PADDING = 15