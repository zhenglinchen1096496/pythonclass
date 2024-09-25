# Define the Product class
class Product:
    """
    A class to represent a product in a business context.
    """

    def __init__(self, name, price, quantity):
        """
        Initialize the product with a name, price, and quantity.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_value(self):
        """
        Calculate the total value of the product stock.
        """
        return self.price * self.quantity

        """
        Increase the quantity of the product by the given amount.
        """
        self.quantity += amount
        print(f"Restocked {self.name}. New quantity: {self.quantity}")

    def sell(self, amount):
        """
        Decrease the quantity of the product by the given amount if available.
        """
        if amount > self.quantity:
            print(f"Not enough {self.name} in stock to sell {amount}.")
        else:
            self.quantity -= amount
            print(f"Sold {amount} of {self.name}. Remaining quantity: {self.quantity}")
    
    def restock(num):
        """
        Increase the quantity of the product by the given amount.
        """
        self.quantity += amount
        print(f"Restocked {self.name}. New quantity: {self.quantity}")


    def __str__(self):
        """
        Return a string representation of the product.
        """
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"


# Create a product instance
laptop = Product(name="apple", price=12.00, quantity=100)

print(laptop)

laptop.sell(70)

print(laptop)
