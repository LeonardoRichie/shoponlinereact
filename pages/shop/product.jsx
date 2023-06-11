import React from 'react';
import { Link } from 'react-router-dom';

export const Product = (props) => {
  const { id, productName, price, productImage } = props.data;

  return (
    <div className="product">
      <img src={productImage} />
      <div className="description">
        <p>
          <Link to={`/description/${id}`}>{productName}</Link>
        </p>
        <p>${price}</p>
      </div>
      <button className="addToCart">Add To Cart</button>
    </div>
  );
};
