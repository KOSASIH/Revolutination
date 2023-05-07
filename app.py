import streamlit as st


# Define a Product class to represent a product
class Product:

    def __init__(self, name, price, description, image):
        self.name = name
        self.price = price
        self.description = description
        self.image = image


# Define some example products
products = [
    Product(
        "Product 1",
        10.99,
        "Description of Product 1",
        "https://via.placeholder.com/150",
    ),
    Product(
        "Product 2",
        24.99,
        "Description of Product 2",
        "https://via.placeholder.com/150",
    ),
    Product(
        "Product 3",
        39.99,
        "Description of Product 3",
        "https://via.placeholder.com/150",
    ),
]


# Define a function to display a product card
def display_product(product):
    st.write(f"### {product.name}")
    st.image(product.image)
    st.write(product.description)
    st.write(f"Price: ${product.price}")
    if st.button("Add to Cart"):
        st.write(f"{product.name} added to cart")


# Display the products
for product in products:
    display_product(product)


# Define a function to display the cart
def display_cart(cart):
    if len(cart) == 0:
        st.write("Your cart is empty")
    else:
        st.write("### Your Cart")
        total = 0
        for item in cart:
            st.write(f"{item.name} - ${item.price}")
            total += item.price
        st.write(f"Total: ${total}")


# Define a function to process the checkout
def process_checkout(cart):
    total = 0
    for item in cart:
        total += item.price
    st.write(f"Your total is: ${total}")
    if st.button("Checkout"):
        st.write("Thank you for your purchase!")
        cart.clear()


# Create a cart object to store the items
cart = []

# Display the
