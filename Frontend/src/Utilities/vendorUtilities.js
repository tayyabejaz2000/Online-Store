import axiosInstance from '../Axios/axiosAPI'

export function getVendorProducts(products, query) {
	axiosInstance.post('/seller/products')
		.then((response) => {
			products(response.data.products)
			query(true)
	})
	.catch((error) => {
		console.log(error)
		throw error
	})
}

export function deleteProduct(product_id) {
	console.log(product_id)
	axiosInstance.post('/seller/remove-product', {
		product_id: product_id
	})
	.then((response) => {
	})
	.catch((error) => {
		console.log(error)
		throw error
	})
}