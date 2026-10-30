class Product:
    def __init__(self, name, price,quantity):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if price < 0 | quantity < 0:
            raise ValueError("Price or Quantity cannot be negative")
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name}: {self.quantity} * R{self.price:.2f}"