import React, {useContext} from 'react'
import { ShopContext } from '../../context/shop-context';

export const Descriptionproduct = (props) => {
    const {id, description, productName, price, productImage} = props.data;
    const {addToCart, cartItems} = useContext(ShopContext);

    const cartItemAmount = cartItems[id]  
  return(
  <div className = "product">
    
    <img src={productImage}/>
    <div className = "description">
        <p>
         <b>
            {productName}
         </b>
        </p>
        <p>${price}</p>
        <p> {description}</p>
    </div>
    <button className="addToCart" onClick={() => addToCart(id)}>
        Add To Cart {cartItemAmount > 0 && <> ({cartItemAmount})</>}
      </button>
    </div>
  )
}
