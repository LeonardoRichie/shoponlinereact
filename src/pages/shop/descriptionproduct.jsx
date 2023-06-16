import React, { useState, useContext } from 'react';
import { ShopContext } from '../../context/shop-context';

export const Descriptionproduct = (props) => {
  const { id, description, productName, price, quantity, productImage } = props.data;
  const imageURL = `http://localhost:8000${productImage}`;
  const [cartItemAmount, setCartItemAmount] = useState(0);
  const { addToCart, cartItems } = useContext(ShopContext);

  const handleAddToCart = async () => {
    try {
      await addToCart(id); // Use the addToCart function from ShopContext
      setCartItemAmount((prevAmount) => prevAmount + 1);
    } catch (error) {
      console.error('Error adding product to cart:', error);
    }
  };


  

  return (
    <div className="product">
      <img src={imageURL} />
      <div className="description">
        <p>
          <b>{productName}</b>
        </p>
        <p>${price}</p>
        <p>{description}</p>
      </div>
      <button className="addToCart" onClick={handleAddToCart}>
        Add To Cart
      </button>
    </div>
  );
};
