import React from 'react';

export const CartItem = ({ data, decrementCartItemQuantity, updateCartItemCount }) => {
  const { id, description, productName, price, productImage, quantity } = data;
  const imageURL = `http://localhost:8000${productImage}`;
  
  const handleDecrement = () => {
    decrementCartItemQuantity(id);
    if (quantity ===1){
      window.location.reload();} // Refresh the page
  };

  return (
    <div className="cartItem">
      <img src={imageURL} alt={productName} />
      <div className="description">
        <p>
          <b>{productName}</b>
        </p>
        <p>${price}</p>
        <div className="countHandler">
          <button onClick={handleDecrement}>-</button>
          <input
            value={quantity}
            onChange={(e) =>
              updateCartItemCount(id, Number(e.target.value))
            }
          />
          <button onClick={() => updateCartItemCount(id, quantity + 1)}>
            +
          </button>
        </div>
      </div>
    </div>
  );
};
