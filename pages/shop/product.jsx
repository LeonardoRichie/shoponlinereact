import React, {useContext} from 'react';
import { Link } from 'react-router-dom';
import { ShopContext } from '../../context/shop-context';
import { CartItem } from '../cart/cart-item';

export const Product = (props) => {
  const { id, productName, price, productImage } = props.data;
  const {addToCart, cartItems} = useContext(ShopContext);

  const cartItemAmount = cartItems[id]
  return (
    <div className="product">
      <img src={productImage} />
      <div className="description">
        <p>
          <Link to={`/description/${id}`}>{productName}</Link>
        </p>
        <p>${price}</p>
      </div>
      <button className="addToCart" onClick={() => addToCart(id)}>
        Add To Cart {cartItemAmount > 0 && <> ({cartItemAmount})</>}
      </button>
    </div>
  );
};
