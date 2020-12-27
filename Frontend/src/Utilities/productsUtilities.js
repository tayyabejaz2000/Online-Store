import axiosInstance from "../Axios/axiosAPI";

export function getAllCategories(categories) {
	axiosInstance.post('products/categories')
	.then((response) => {
		categories(response.data.categories)
	})
	.catch((error) => {
		console.log(error)
		throw error
	})
}