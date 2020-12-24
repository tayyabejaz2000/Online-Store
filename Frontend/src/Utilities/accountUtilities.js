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
	})
}

export function signup(values) {
	// Do Signup
}

export function getAccountData() {
	let username = sessionStorage.getItem("username")
	let accountType = sessionStorage.getItem("accountType")
	if (username && accountType) {
		return {
			"username": username,
			"accountType": accountType,
		}
	}
	else {
		axiosInstance.get("/account/min-data/")
		.then((result) => {
			if (result.status === 200) {
				sessionStorage.setItem("username", result.data.username)
				sessionStorage.setItem("accountType", result.data.accountType)
			}
		})
		.catch((error) => {
			console.log(error)
		})
	}
}