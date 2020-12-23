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
		if (result.status === 200)
			sessionStorage.setItem("username", values.username)
			window.location.href = "/home"
	})
	.catch((error) => {
		console.log(error)
		throw error
	})
}

export function signup(values) {
	// Do Signup
}

export function getUsername() {
	let username = sessionStorage.getItem("username")
	if (username) {
		return username
	}
	else {
		//Do Get Query from access Token
	}
}
