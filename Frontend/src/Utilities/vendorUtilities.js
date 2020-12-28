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