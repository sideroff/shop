import React from 'react'
import {
  Switch,
  Route
} from 'react-router-dom'


import {
  About,
  Contacts,
  Home
} from 'components/pages'

export default function Router() {
  return (
    <Switch>
      <Route exact path='/' component={Home} />
      <Route path='/about' component={About} />
      <Route path='/contacts' component={Contacts} />
    </Switch>
  )
}