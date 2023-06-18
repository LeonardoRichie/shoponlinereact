from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from datetime import datetime
from pydantic import BaseModel

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
        "productName": 'Sparkly Ring',
        "price": 1.299,
        "productImage": "/assets/1.jpg",
        "description": 'Elegance meets brilliance in this captivating diamond ring. Crafted with precision, it features a dazzling centerpiece—a brilliant-cut diamond of exceptional quality. Set in a lustrous band, this exquisite ring is a timeless symbol of sophistication. Own a piece of everlasting beauty today.'
    },
    {
        "id": 2,
        "productName": 'Heart Beads Earrings',
        "price": 59,
        "productImage":"/assets/2.jpg",
        "description": 'Spread love with these adorable heart beads earrings. Delicate and playful, they add a touch of sweetness to any look. Perfect for all occasions. Embrace romance and style with these heart beads earrings'
    },
    {
        "id": 3,
        "productName": 'Blue Eye Bracelet',
        "price": 49,
        "productImage":"/assets/3.jpg",
        "description": 'Embrace protection and style with this captivating blue eye bracelet. Adorned with a mesmerizing blue eye charm, it symbolizes warding off negative energy and bringing good luck. The vibrant blue color adds a pop of elegance, while the adjustable chain ensures a perfect fit. Wear this bracelet as a fashionable talisman and exude confidence wherever you go.'
    },
    {
        "id": 4,
        "productName": 'Hologram Big O Bracelet',
        "price": 68,
        "productImage": "/assets/4.jpg",
        "description": 'Step into the future of fashion with this eye-catching hologram Big O bracelet. Its mesmerizing design displays a spectrum of vibrant colors, creating a stunning visual display with every movement. The sleek and adjustable band ensures a comfortable fit for all wrist sizes. Make a bold statement and add a touch of futuristic style to your outfits with this one-of-a-kind hologram Big O bracelet.'
    },
    {
        "id": 5,
        "productName": 'Red Quartz Ring',
        "price": 89.99,
        "productImage":"/assets/5.jpg",
        "description": 'Ignite your style with this captivating red quartz ring. The fiery red hue of the quartz gemstone commands attention, exuding confidence and passion. Set in a sleek band, this ring is a perfect blend of boldness and elegance. Whether for a special occasion or everyday wear, this red quartz ring will add a touch of allure and sophistication to any ensemble. Elevate your jewelry collection with this stunning statement piece.'
    },
    {
        "id": 6,
        "productName": 'Enchanted Curve Earrings',
        "price": 40,
        "productImage":"/assets/6.jpg",
        "description": 'Add a touch of modern elegance to your look with these stunning curve earrings. The gracefully curved design effortlessly enhances your style, making a subtle yet eye-catching statement. Crafted with precision and attention to detail, these earrings are perfect for both casual and formal occasions. Elevate your jewelry collection with these versatile and chic curve earrings that are sure to turn heads wherever you go.'
    },
    {
        "id": 7,
        "productName": 'Shimmering Cascade',
        "price": 199.99,
        "productImage":"/assets/7.jpg",
        "description": 'Make a bold and glamorous statement with this captivating black diamond ring. The striking black diamond centerpiece exudes mystery and sophistication, set in a sleek band that beautifully accentuates its allure. Perfect for those seeking a unique and dramatic piece, this black diamond ring is a testament to exquisite craftsmanship and timeless style. Embrace the allure of black and let this extraordinary ring elevate your jewelry collection to new heights.'
    },
    {
        "id": 8,
        "productName": 'Serendipity Bubble (1pcs)',
        "price": 55,
        "productImage":"/assets/8.jpg",
        "description": 'Delicately crafted, each earring features a cluster of tiny bubbles, adding a whimsical and lighthearted touch to your style. These earrings are perfect for both casual and dressy occasions, making them a versatile addition to your jewelry collection. Embrace a touch of fun and grace with these delightful bubble earrings that are sure to make you stand out.'
    },
    {
        "id": 9,
        "productName": 'Blue Radiant Stack',
        "price": 55,
        "productImage":"/assets/9.jpg",
        "description": 'Make a dazzling statement with this Blue Radiant Stack Necklace. The necklace features a captivating stack of radiant blue gemstones, each one emanating a brilliant sparkle. The stunning shades of blue create a harmonious and mesmerizing display, while the delicate chain adds a touch of elegance. This necklace is the perfect accessory to elevate any outfit, from casual to formal, and is sure to draw attention with its exquisite beauty. '
    },
    {
        "id": 10,
        "productName": 'Minimalist Celestial Sparkle',
        "price": 100,
        "productImage":"/assets/10.jpg",
        "description": 'Radiate celestial elegance with this Minimalist Celestial Sparkle Necklace. The necklace showcases a delicate celestial charm, adorned with shimmering crystals that reflect the light with a captivating sparkle. Its minimalist design exudes understated beauty, making it a versatile piece for any occasion. Whether worn alone or layered with other necklaces, this celestial-inspired necklace adds a touch of celestial magic and effortless style to your look. '
    },
    {
        "id": 11,
        "productName": 'Pearls Choker',
        "price": 29.99,
        "productImage":"/assets/11.jpg",
        "description": 'Indulge in timeless elegance with this exquisite Pearl Choker Necklace. The necklace features a stunning arrangement of lustrous pearls, delicately strung together to create a classic and sophisticated look. With its adjustable length, it gracefully sits at the base of the neck, enhancing your neckline with a touch of refinement. Whether for a formal event or a stylish everyday accessory, this pearl choker necklace adds an air of grace and sophistication to any outfit.'
    },
    {
        "id": 12,
        "productName": 'Serene Spirit',
        "price": 55,
        "productImage":"/assets/12.jpg",
        "description": 'Embrace mystique and elegance with this captivating Black Diamond Necklace. The sleek black diamond pendant on a delicate chain creates a bold and sophisticated look. Perfect for any occasion, this necklace exudes timeless allure and individuality. Make a statement with this stunning black diamond necklace.'
    }
]


@app.get("/products")
def get_all_products():
    return products

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

# Mock data for cart items
cart_items = {}
history = []
users = []

# Pydantic model for user signup request
class UserSignupRequest(BaseModel):
    name: str
    email: str
    password: str
    address: str
    telephone: str

# Pydantic model for user login request
class UserLoginRequest(BaseModel):
    email: str
    password: str

# API route for user signup
@app.post("/signup")
def signup(user_data: UserSignupRequest):
    # Check if user with the same email already exists
    existing_user = next((user for user in users if user["email"] == user_data.email), None)
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists")

    # Add the new user to the list
    users.append(user_data.dict())
    return {"message": "User registered successfully"}

# API route for user login
@app.post("/login")
def login(credentials: UserLoginRequest):
    # Find the user with matching email and password
    user = next((user for user in users if user["email"] == credentials.email), None)
    if user and user["password"] == credentials.password:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid email or password")

# API route to get user details
@app.get("/user/{email}")
def get_user(email: str):
    user = next((user for user in users if user["email"] == email), None)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

# API route to get cart items
@app.get("/cart")
def get_cart_items():
    cart_items_with_total_price = []
    for item in cart_items.values():
        total_price = item["price"] * item["quantity"]
        item_with_total_price = {**item, "total_price": total_price}
        cart_items_with_total_price.append(item_with_total_price)
    return cart_items_with_total_price


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
                    "timestamp": datetime.now().strftime("%Y-%m-%d/%H:%M:%S")  # Format timestamp
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
    history.extend(cart_items.values())  # Move all items to history
    cart_items = {}
    return {"message": "Cart cleared"}

@app.put("/cart/increment/{product_id}")
def increment_cart_item_quantity(product_id: int):
    if product_id not in cart_items:
        raise HTTPException(status_code=404, detail="Product not found")

    cart_items[product_id]["quantity"] += 1
    return cart_items[product_id]

@app.get("/cart/history")
def get_cart_history():
    return history

