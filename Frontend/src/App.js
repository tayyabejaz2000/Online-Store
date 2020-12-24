import React, { useState } from "react"
import { BrowserRouter as Router, Switch, Route, Redirect } from "react-router-dom"
import { ThemeProvider } from "@material-ui/core/styles"
import CssBaseline from "@material-ui/core/CssBaseline"

//Components
import Header from "./Components/Header"
import Footer from "./Components/Footer"

//Routes-Views
import Home from "./Views/Home"
import Login from "./Views/Login"
import Vendor from "./Views/Vendor"
import Signup from "./Views/Signup"

//Themes
import DarkTheme from "./Themes/darkTheme"
import LightTheme from "./Themes/lightTheme"
import MyAccount from "./Views/MyAccount"

function App(props) {
	const [dark_theme, changeThemePreference] = useState(true)
	console.log(DarkTheme)
	return (
		<ThemeProvider theme={dark_theme ? DarkTheme : LightTheme}>
			<CssBaseline />
			<Router>
				<Header theme={dark_theme} onThemeChange={changeThemePreference}/>
				<Switch>
					<Route exact path="/home">
						<Home />
					</Route>
					<Route exact path="/login">
						<Login />
					</Route>
					<Route exact path="/signup">
						<Signup />
					</Route>
					<Route exact path="/vendor">
						<Vendor />
					</Route>
					<Route exact path="/account">
						<MyAccount />
					</Route>
					<Route exact path="/user">
						{null}
					</Route>
					<Route path="/">
						<Redirect to="/home"/>
					</Route>
				</Switch>
				<Footer />
			</Router>
		</ThemeProvider>
  )
}

export default App
