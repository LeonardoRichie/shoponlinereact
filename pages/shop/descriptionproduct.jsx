import React from 'react'

export const Descriptionproduct = (props) => {
    const {id, description, productName, price, productImage} = props.data;
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
    <button className = "addToCart">Add To Cart</button>
    </div>
  )
}
