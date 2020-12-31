import axiosInstance from "../Axios/axiosAPI";

export async function addToCart(product_id, quantity) {
	await axiosInstance.post('/user/add-to-cart', {
		product_id: product_id,
		quantity: quantity,
	})
	.catch((error) => {
		console.log(error)
		throw error	
	})
}

export async function getCartProducts() {
	let data=null
	await axiosInstance.post('/user/cart')
	.then((response) => {
		data = response.data
	})
	.catch((error) => {
		console.log(error)
		throw error	
	})
	return data
}
export async function updateCart(products) {
	products.map((value) => {
		axiosInstance.post('user/update-cart', {
			product_id: value.product.id,
			quantity: value.quantity
		})
		.catch((error) => {
			console.log(error)
			throw error	
		})
		return null
	})
}

export async function getAddBillingAddresses() {
	let billingAddresses = null
	await axiosInstance.post('user/get-billing-addresses')
	.then((response) => {
		billingAddresses = response.data.billing_addresses
	})
	.catch((error) => {
		console.log(error)
		throw error	
	})
	return billingAddresses
}

export function addBillingAddress(values) {
	axiosInstance.post('user/add-billing-address', {
		address: values.billingAddress
	})
	.catch((error) => {
		console.log(error)
		throw error
	})
}

export async function placeOrder(values) {
	axiosInstance.post('user/place-order', {
		billing_address: values.billing_address,
		discount: 0,
		wallet_password: values.wallet_password,
	})
	.then((response) => {
		if (response.status === 200)
			window.location.href = "/home"
	})
	.catch((error) => {
		console.log(error)
		throw error
	})
}

export async function getOrders() {
	let orders = null
	await axiosInstance.post('user/orders')
	.then((response) => {
		orders = response.data
	})
	.catch((error) => {
		console.log(error)
		throw error
	})
	return orders
}

export function cancelOrder(ordered_product_id) {
	axiosInstance.post('/user/cancel-item', {
		ordered_product_id: ordered_product_id
	})
	.catch((error) => {
		console.log(error)
		throw error
	})
}

export function returnItem(ordered_product_id) {
	axiosInstance.post('/user/return-item', {
		ordered_product_id: ordered_product_id
	})
	.catch((error) => {
		console.log(error)
		throw error
	})
}