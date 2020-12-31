import axiosInstance from "../Axios/axiosAPI";

export async function getUnresolvedComplaints() {
	let complaints = null
	await axiosInstance.post('employee/complaints')
	.then((response) => {
		complaints = response.data	
	})
	.catch((error) => {
		console.log(error)
		throw error
	})
	return complaints
}

export async function resolveComplaint(values) {
	axiosInstance.post('employee/complaints/resolve', values)
	.then((response) => {
		if (response.status === 200)
			window.location.href = "/employee/complaints"
	})
	.catch((error) => {
		console.log(error)
		throw error
	})
}