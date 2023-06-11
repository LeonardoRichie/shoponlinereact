import React from 'react';
import { Descriptionproduct } from './descriptionproduct';
import { PRODUCTS } from '../../products';
import { Link, useParams } from 'react-router-dom';

export const Description = () => {
  const { id } = useParams();
  const productId = parseInt(id, 10);
  const product = PRODUCTS.find((p) => p.id === productId);

  return (
    <div className="shop">
      <div>
        <div className="shopTitle">
          <h1>Description</h1>
          <Link to="/">
            <button>back</button>
          </Link>
        </div>
        <div className="products">
          <Descriptionproduct data={product} />
        </div>
      </div>
    </div>
  );
};
