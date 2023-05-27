class Field:
    """A field where bees can gather food from food sources."""

    def __init__(self, width=100, height=100):
        """Create a field with the given width and height."""
        self.width = width
        self.height = height
        self.food_sources = []


class FoodSource:
    """A food source where bees can gather food."""

    def __init__(self, position, food_amount):
        """Create a food source with the given position and food amount."""
        self.position = position
        self.food_amount = food_amount
        self.honey_quality = 1
        self.taken_food = 0