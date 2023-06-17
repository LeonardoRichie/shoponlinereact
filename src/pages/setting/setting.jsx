import React, { useState, useEffect } from 'react';
import axios from 'axios';

export const Setting = () => {
  const [loginEmail, setLoginEmail] = useState('');
  const [loginPassword, setLoginPassword] = useState('');
  const [signupName, setSignupName] = useState('');
  const [signupEmail, setSignupEmail] = useState('');
  const [signupPassword, setSignupPassword] = useState('');
  const [signupAddress, setSignupAddress] = useState('');
  const [signupTelephone, setSignupTelephone] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Check if the user is logged in on component mount
  useEffect(() => {
    const loggedInUser = localStorage.getItem('user');
    if (loggedInUser) {
      setIsLoggedIn(true);
    }
  }, []);

  const handleLoginSubmit = async (e) => {
    e.preventDefault();

    try {
      const email = loginEmail.toLowerCase(); // Convert email to lowercase
      // Send a POST request to the login endpoint
      const response = await axios.post('http://localhost:8000/login', {
        email,
        password: loginPassword,
      });

      // User login successful, update state and save user data in local storage
      setIsLoggedIn(true);
      localStorage.setItem('user', JSON.stringify(response.data));
    } catch (error) {
      // User login failed, display error message or perform appropriate action
      console.log('Invalid email or password');
    }
  };

  const handleSignOut = () => {
    setIsLoggedIn(false);
    localStorage.removeItem('user');
    setLoginEmail('');
    setLoginPassword('');
  };

  const handleSignupSubmit = async (e) => {
    e.preventDefault();

    try {
      const email = signupEmail.toLowerCase(); // Convert email to lowercase
      // Send a POST request to the signup endpoint
      await axios.post('http://localhost:8000/signup', {
        name: signupName,
        email,
        password: signupPassword,
        address: signupAddress,
        telephone: signupTelephone,
      });

      // User signup successful, clear the signup form fields
      setSignupName('');
      setSignupEmail('');
      setSignupPassword('');
      setSignupAddress('');
      setSignupTelephone('');

      console.log('Signup submitted');
    } catch (error) {
      // User signup failed, display error message or perform appropriate action
      console.log('Error signing up');
    }
  };

  if (isLoggedIn) {
    const loggedInUser = JSON.parse(localStorage.getItem('user'));
    return (
      <div>
        <h2>User Profile</h2>
        <p>Welcome, {loggedInUser.name}!</p>
        <button onClick={handleSignOut}>Sign Out</button>
      </div>
    );
  } else {
    return (
      <div>
        <h2>Login</h2>
        <form onSubmit={handleLoginSubmit}>
          <div>
            <label>Email:</label>
            <input
              type="email"
              value={loginEmail}
              onChange={(e) => setLoginEmail(e.target.value)}
            />
          </div>
          <div>
            <label>Password:</label>
            <input
              type="password"
              value={loginPassword}
              onChange={(e) => setLoginPassword(e.target.value)}
            />
          </div>
          <button type="submit">Login</button>
        </form>

        <h2>Signup</h2>
        <form onSubmit={handleSignupSubmit}>
          <div>
            <label>Name:</label>
            <input
              type="text"
              value={signupName}
              onChange={(e) => setSignupName(e.target.value)}
            />
          </div>
          <div>
            <label>Email:</label>
            <input
              type="email"
              value={signupEmail}
              onChange={(e) => setSignupEmail(e.target.value)}
            />
          </div>
          <div>
            <label>Password:</label>
            <input
              type="password"
              value={signupPassword}
              onChange={(e) => setSignupPassword(e.target.value)}
            />
          </div>
          <div>
            <label>Address:</label>
            <input
              type="text"
              value={signupAddress}
              onChange={(e) => setSignupAddress(e.target.value)}
            />
          </div>
          <div>
            <label>Telephone:</label>
            <input
              type="text"
              value={signupTelephone}
              onChange={(e) => setSignupTelephone(e.target.value)}
            />
          </div>
          <button type="submit">Signup</button>
        </form>
      </div>
    );
  }
};
