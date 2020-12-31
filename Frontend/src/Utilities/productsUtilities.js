import axiosInstance from "../Axios/axiosAPI";

export function getAllCategories(categories, query) {
	axiosInstance.post('products/categories')
	.then((response) => {
		categories(response.data.categories)
	})
	.catch((error) => {
		console.log(error)
		throw error
	})
	query(true)
}

export function getProduct(id, formik, query) {
	axiosInstance.post('products/get-product', {
		product_id: id
	})
	.then((response) => {
		for (const key in response.data) {
			formik.setFieldValue(key, response.data[key])
		}
	})
	.catch((error) => {
		console.log(error)
		throw error
	})
	query(true)
}

export function addProduct(values) {
	axiosInstance.post('products/add-product', values)
	.catch((error) => {
		console.log(error)
		throw error
	})
}

export function editProduct(values) {
	axiosInstance.post('products/update-product', {
		product_id: values.id,
		product_name: values.name,
		product_desc: values.description,
		quantity: values.stock,
		price: values.price,
		discount: values.discount,
		category: values.category
	})
	.catch((error) => {
		console.log(error)
		throw error
	})
}

export function deleteProduct(product_id) {
	axiosInstance.post('/products/remove-product', {
		product_id: product_id
	})
	.catch((error) => {
		console.log(error)
		throw error
	})
}

export async function getAllProducts() {
	let products = null	
	await axiosInstance.post('/products/')
	.then((response) => {
		products = response.data.products
	})
	.catch((error) => {
		console.log(error)
		throw error
	})
	return products
}

export async function addReview(values) {
	await axiosInstance.post('/products/add-review', values)
	.catch((error) => {
		console.log(error)
		throw error
	})
}