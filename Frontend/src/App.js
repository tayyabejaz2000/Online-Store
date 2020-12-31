import React, { useState } from "react"
import {
	BrowserRouter as Router,
	Switch,
	Route,
	Redirect
} from "react-router-dom"
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
import MyAccount from "./Views/MyAccount"
import AddProduct from "./Views/AddProduct"
import EditProduct from "./Views/EditProduct"
import Cart from "./Views/Cart"
import AddBillingAddress from "./Views/AddBillingAddress"
import PlaceOrder from "./Views/PlaceOrder"
import EditShop from "./Views/EditShop"
import Orders from "./Views/Orders"
import AddReview from "./Views/AddReview"
import AddComplaint from "./Views/AddComplaint"

//Themes
import DarkTheme from "./Themes/darkTheme"
import LightTheme from "./Themes/lightTheme"
import Complaints from "./Views/Complaints"
import ResolveComplaint from "./Views/ResolveComplaint"

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
					<Route exact path="/vendor/addproduct">
						<AddProduct />
					</Route>
					<Route exact path="/vendor/editshop">
						<EditShop />
					</Route>
					<Route path="/vendor/editproduct/:id">
						<EditProduct />
					</Route>
					<Route exact path="/account">
						<MyAccount />
					</Route>
					<Route exact path="/user/addbillingaddress">
						<AddBillingAddress />
					</Route>
					<Route exact path="/complaint">
						<AddComplaint />
					</Route>
					<Route exact path="/user/placeorder">
						<PlaceOrder />
					</Route>
					<Route exact path="/user/orders">
						<Orders />
					</Route>
					<Route exact path="/product/review/:id">
						<AddReview />
					</Route>
					<Route exact path="/employee/complaints">
						<Complaints />
					</Route>
					<Route exact path="/employee/complaints/resolve/:id">
						<ResolveComplaint />
					</Route>
					<Route exact path="/cart">
						<Cart />
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
