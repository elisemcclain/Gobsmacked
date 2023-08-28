import { Link } from "react-router-dom";
import React, { useEffect, useState } from "react";

function Login({ newUser, setNewUser }) {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [userExists, setUserExists] = useState(true);

  function handleChange(e) {
    const { name, value } = e.target;
    setNewUser({ ...newUser, [name]: value });
  }

  return (
    <div>
      <div>
        <h1>*Welcome! Enter your email to log in or create an account*</h1>
      </div>
      <form>
        <label htmlFor="email">email</label>
        <input
          type="email"
          value={email}
          placeholder="email"
          id="email"
          name="email"
          onChange={(e) => {
            setEmail(e.target.value);
            setUserExists(true);
          }}
        />
        {userExists ? (
          <>
            <label htmlFor="password">password</label>
            <input
              type="email"
              value={password}
              placeholder="password"
              id="password"
              name="password"
              onChange={(e) => {
                setPassword(e.target.value);
                setUserExists(true);
              }}
            />
          </>
        ) : (
          <>
            <label htmlFor="first_name">first name</label>
            <input
              type="text"
              value={firstName}
              placeholder="first name"
              id="first_name"
              name="user_first_name"
              onChange={(e) => {
                setFirstName(e.target.value);
                setUserExists(false);
              }}
            />
            <label htmlFor="last_name">last name</label>
            <input
              type="text"
              value={lastName}
              placeholder="last name"
              id="last_name"
              name="user_last_name"
              onChange={(e) => {
                setLastName(e.target.value);
                setUserExists(false);
              }}
            />
            <label htmlFor="password">password</label>
            <input
              type="email"
              value={password}
              placeholder="password"
              id="password"
              name="password"
              onChange={(e) => {
                setPassword(e.target.value);
                setUserExists(false);
              }}
            />
          </>
        )}
        <button>Log In</button>
      </form>
    </div>
  );
}

export default Login;