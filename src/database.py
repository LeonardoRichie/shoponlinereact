from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update with your React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (images)
app.mount("/assets", StaticFiles(directory="./assets"), name="assets")

# Your existing /products route
products = [
    {
        "id": 1,
        "productName": "IPhone 14ss",
        "price": 1200.0,
        "productImage": "/assets/1.png",
        "description": "The iPhone 14 display has rounded corners that follow a beautiful curved design...",
    },
    {
        "id": 2,
        "productName": "IPhone 14 Pro",
        "price": 999.0,
        "productImage": "/assets/2.jpg",
        "description": "The iPhone 14 Pro and iPhone 14 Pro Max are smartphones designed, developed...",
    },
    # Add more product entries as needed
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Product not found"}

# Mock data for cart items
cart_items = {}

# API route to get cart items
@app.get("/cart")
def get_cart_items():
    cart_items_with_total_price = []
    for item in cart_items.values():
        total_price = item["price"] * item["quantity"]
        item_with_total_price = {**item, "total_price": total_price}
        cart_items_with_total_price.append(item_with_total_price)
    return cart_items_with_total_price


# API route to add a product to the cart
@app.post("/cart/{product_id}")
def add_to_cart(product_id: int):
    for product in products:
        if product["id"] == product_id:
            if product_id in cart_items:
                cart_items[product_id]["quantity"] += 1
            else:
                cart_items[product_id] = {
                    "id": product["id"],
                    "productName": product["productName"],
                    "price": product["price"],
                    "productImage": product["productImage"],
                    "description": product["description"],
                    "quantity": 1,
                }
            return cart_items[product_id]
    raise HTTPException(status_code=404, detail="Product not found")

# API route to remove a product from the cart
@app.delete("/cart/{product_id}")
def remove_from_cart(product_id: int):
    if product_id not in cart_items:
        raise HTTPException(status_code=404, detail="Product not found")

    cart_items[product_id]["quantity"] -= 1
    if cart_items[product_id]["quantity"] <= 0:
        del cart_items[product_id]

    return {"message": "Product removed from cart"}

# API route to update the quantity of a product in the cart
@app.put("/cart/{product_id}")
def update_cart_item_quantity(product_id: int, quantity: int):
    if product_id not in cart_items:
        raise HTTPException(status_code=404, detail="Product not found")

    cart_items[product_id]["quantity"] = quantity
    return cart_items[product_id]

# API route to calculate the total amount of the cart
@app.get("/cart/total")
def get_cart_total():
    total_amount = 0.0
    for item in cart_items.values():
        total_amount += item["price"] * item["quantity"]
    return {"total_amount": total_amount}

# API route to decrement the quantity of a cart item by 1 based on ID
# API route to decrement the quantity of a product in the cart
@app.put("/cart/minus/{product_id}")
def decrement_cart_item_quantity(product_id: int):
    if product_id not in cart_items:
        raise HTTPException(status_code=404, detail="Product not found")

    cart_items[product_id]["quantity"] -= 1
    if cart_items[product_id]["quantity"] <= 0:
        del cart_items[product_id]

    return cart_items[product_id]


@app.delete("/cart")
def clear_cart():
    global cart_items
    cart_items = {}
    return {"message": "Cart cleared"}