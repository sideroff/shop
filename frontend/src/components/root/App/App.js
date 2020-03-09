import React from 'react'
import { BrowserRouter } from 'react-router-dom'

import { Router } from 'components/root'
import { Header } from 'components/organisms'

import './App.css'

function App() {
  return (
    <div className='app'>
      <BrowserRouter>
        <Header />
        <Router />
      </BrowserRouter>
    </div>
  )
}

export default App
