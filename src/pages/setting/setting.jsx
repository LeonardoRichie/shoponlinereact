import React, { useState, useEffect } from 'react';

export const Setting = () => {
  const [loginEmail, setLoginEmail] = useState('');
  const [loginPassword, setLoginPassword] = useState('');
  const [signupName, setSignupName] = useState('');
  const [signupEmail, setSignupEmail] = useState('');
  const [signupPassword, setSignupPassword] = useState('');
  const [users, setUsers] = useState([]);
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Check if the user is logged in on component mount
  useEffect(() => {
    const loggedInUser = localStorage.getItem('user');
    if (loggedInUser) {
      setIsLoggedIn(true);
    }
  }, []);

  const handleLoginSubmit = (e) => {
    e.preventDefault();

    // Find the user with matching email and password in the array
    const loginUser = users.find(
      (user) => user.email === loginEmail && user.password === loginPassword
    );

    if (loginUser) {
      // User found, perform login logic
      setIsLoggedIn(true);
      localStorage.setItem('user', JSON.stringify(loginUser));
    } else {
      // User not found, display error message or perform appropriate action
      console.log('Invalid email or password');
    }
  };

  const handleSignOut = () => {
    setIsLoggedIn(false);
    localStorage.removeItem('user');
    setLoginEmail('');
    setLoginPassword('');
  };

  const handleSignupSubmit = (e) => {
    e.preventDefault();
    // Create a new user object
    const newUser = {
      name: signupName,
      email: signupEmail,
      password: signupPassword,
    };

    // Add the new user to the array
    setUsers([...users, newUser]);

    // Clear the signup form fields
    setSignupName('');
    setSignupEmail('');
    setSignupPassword('');

    console.log('Signup submitted');
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
          <button type="submit">Signup</button>
        </form>
      </div>
    );
  }
};