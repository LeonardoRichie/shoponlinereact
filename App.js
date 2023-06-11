
import './App.css';
import {BrowserRouter as Router,Routes,Route} from 'react-router-dom'
import { Navbar } from './components/navbar';
import { Cart } from './pages/cart/cart';
import { Shop } from './pages/shop/shop';
import { Setting } from './pages/setting/setting';
import { Description } from './pages/shop/description';

function App() {
  return (
    <div className="App">
      <Router>
        <Navbar />
        <Routes>
          <Route>
            <Route path="/" element={<Shop />} />
            <Route path="/description/:id" element={<Description />} />
            <Route path="/cart" element={<Cart />} />
            <Route path= "/setting" element={<Setting />}/>
          </Route>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
