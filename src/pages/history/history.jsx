import React, {useContext} from 'react'
import { PRODUCTS } from '../../products'
import { ShopContext } from '../../context/shop-context'
import { CartItem } from '../cart/cart-item';


export const History = () => {
  const {cartItems} = useContext(ShopContext);
  return (
    <div className="cartItems">
          {PRODUCTS.map((product)=>{
              if (cartItems[product.id] !== 0){
                return <CartItem data={product} />
              }
          })}
          </div>
  )
}
