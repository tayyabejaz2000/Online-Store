import axiosInstance from '../Axios/axiosAPI'

export function checkLoggedIn() {
	return ((localStorage.getItem('access_token') === null)? false : true )
}

export function login(values) {
	axiosInstance.post('/login/', {
		username: values.username,
		password: values.password,
	})
	.then((result) => {
		axiosInstance.defaults.headers['Authorization'] = "JWT " + result.data.access
		sessionStorage.removeItem("username")
		sessionStorage.removeItem("user_type")
		localStorage.setItem('access_token', result.data.access)
		getAccountData()
		if (values.rememberMe)
			localStorage.setItem('refresh_token', result.data.refresh)
		if (result.status === 200) {
			window.location.href = "/home"
		}
	})
	.catch((error) => {
		console.log(error)
	})
}

export function signup(values) {
	let post_data = {
		username: values.username,
		email: values.email,
		first_name: values.firstName,
		last_name: values.lastName,
		phone_number: values.phoneNumber,
		password: values.password,
		wallet_password: values.wallet_password,
		user_type: (values.sellerAccount)? 'S' : 'B'
	}
	if (values.sellerAccount) {
		post_data["shop_name"] = values.shop_name
		post_data["shop_location"] = values.shop_location
	}
	axiosInstance.post('/signup/', post_data)
	.then((response) => {
		if (response.status === 201)
			window.location.href = "/login/"
		else
			throw response
	})
	.catch((error) => {
		console.log(error)
		throw error
	})
}

export function getAccountData() {
	if (localStorage.getItem("access_token")) {
		let username = sessionStorage.getItem("username")
		let user_type = sessionStorage.getItem("user_type")
		if (!username || !user_type) {
			axiosInstance.post("/account/min-data")
			.then((result) => {
				if (result.status === 200) {
					sessionStorage.setItem("username", result.data.username)
					sessionStorage.setItem("user_type", result.data.user_type)
				}
			})
			.catch((error) => {
				console.log(error)
			})
		}
	}
	return {
		"username": sessionStorage.getItem("username"),
		"user_type": sessionStorage.getItem("user_type"),
	}
}