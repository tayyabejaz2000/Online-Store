import axiosInstance from '../Axios/axiosAPI'

export function getVendorProducts(products, query) {
	axiosInstance.post('/seller/products')
	.then((response) => {
		products(response.data.products)
	})
	.catch((error) => {
		console.log(error)
		throw error
	})
	query(true)
}

export async function getShopDetails() {
	let shopData = null
	await axiosInstance.post('/seller/shop')
	.then((response) => {
		shopData = response.data
	})
	.catch((error) => {
		console.log(error)
		throw error
	})
	return shopData
}

export async function editShop(values) {
	await axiosInstance.post('seller/edit-shop', {
		shop_name: values.name,
		shop_location: values.location,
	})
	.catch((error) => {
		console.log(error)
		throw error	
	})
}