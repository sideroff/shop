import React from 'react'
import { NavLink } from 'react-router-dom'
import { FaBars } from 'react-icons/fa'

import './Header.scss'

function Header() {

  return (
    <header>

      <NavLink to='/home'>Home <FaBars /></NavLink>
      <NavLink to='/about'>About</NavLink>
      <NavLink to='/contacts'>Contacts</NavLink>
    </header>
  )
}

export default Header