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
		localStorage.setItem('access_token', result.data.access)
		if (values.rememberMe)
			localStorage.setItem('refresh_token', result.data.refresh)
		if (result.status === 200) {
			window.location.href = "/home"
		}
	})
	.catch((error) => {
		console.log(error)
		//Show Error that login Failed Try Again.
	})
}

export function signup(values) {
	// Do Signup
}

export function getAccountData() {
	let username = sessionStorage.getItem("username")
	let account = sessionStorage.getItem("")
	if (username) {
		return username
	}
	else {
		
	}
}

export function getAccountType() {
	let accountType = sessionStorage.getItem("accountType")
	if (accountType) {
		return accountType
	}
	else {
		//Do Post Query from Refresh Token, save Access Token, username and accountType
	}
}
