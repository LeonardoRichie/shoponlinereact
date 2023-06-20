import React from 'react'
import { Link } from 'react-router-dom'

export const Checkout = () => {
  
  return (
    <div className="checkout">
        <Link to="/">
            <button>back</button>
          </Link>
          <h1>payment will be to 001230830850285 BCA bank account</h1>
          <h1>Tracking number will be send via email</h1>
          <h1>Thank you</h1>
    </div>
  )
}
