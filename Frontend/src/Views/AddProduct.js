import React, { useState } from 'react'

import {
	TextField,
	Typography,
	Container,
	CssBaseline,
	Button,
	Grid,
	MenuItem,
} from '@material-ui/core'
import { useFormik } from 'formik'

import {
	loginStyles as formStyles
} from "../MUI-Styles/Styles"
import { addProduct, getAllCategories } from '../Utilities/productsUtilities'

function AddProduct() {
	const classes = formStyles()
	const [categories, setCategories] = useState([])
	const [query, setQuery] = useState(false)
	if (!query)
		getAllCategories(setCategories, setQuery)
	const formik = useFormik({
		initialValues: {
			product_name: "",
			product_desc: "",
			quantity: "",
			price: "",
			discount: "",
			category: "",
		},
		onSubmit: (values) => {
			addProduct(values)
			window.location.href = "/vendor/"
		}
	})
	return (
		<Container component="main" maxWidth="sm">
			<CssBaseline />
			<div className={classes.paper}>
				<Typography component="h1" variant="h5">
						Add a Product
				</Typography>
				<form onSubmit={formik.handleSubmit}>
					<div className={classes.form}>
						<TextField
							variant="outlined"
							margin="normal"
							required
							fullWidth
							id="product_name"
							label="Product Name"
							name="product_name"
							value={formik.values.product_name}
							onChange={formik.handleChange}
						/>
						<TextField
							variant="outlined"
							margin="normal"
							required
							fullWidth
							id="product_desc"
							label="Product Description"
							name="product_desc"
							value={formik.values.product_desc}
							onChange={formik.handleChange}
						/>
						<TextField
							variant="outlined"
							margin="normal"
							required
							fullWidth
							type="number"
							id="quantity"
							label="Stock"
							name="quantity"
							value={formik.values.quantity}
							onChange={formik.handleChange}
						/>
						<Grid
								container
								direction="row"
								justify="space-between"
								alignItems="center"
								spacing={2}
						>
							<Grid item xs={12} sm={6}>
								<TextField
									variant="outlined"
									margin="normal"
									required
									fullWidth
									type="number"
									id="price"
									label="Price"
									name="price"
									value={formik.values.price}
									onChange={formik.handleChange}
								/>
							</Grid>
							<Grid item xs={12} sm={6}>
								<TextField
									variant="outlined"
									margin="normal"
									required
									fullWidth
									type="number"
									id="discount"
									label="Discount"
									name="discount"
									value={formik.values.discount}
									onChange={formik.handleChange}
								/>
							</Grid>
						</Grid>
						<TextField
							fullWidth
							value={formik.values.category}
							select
							required
							helperText="Select Category"
							onChange={(event) => { formik.setFieldValue("category", event.target.value) }}
						>
							{
								categories.map((value) => {
									return (
										<MenuItem value={value.name}>
											{value.name}
										</MenuItem>
									)
								})
							}
						</TextField>
						<Grid
							container
							justify="space-around"
							alignItems="center"
						>
							<Grid item xs={4}>
								<Button
									fullWidth
									variant="contained"
									className={classes.submit}
									type="submit"
									size="large"
								>
									Add
								</Button>
							</Grid>
							<Grid item xs={4}>
								<Button
									fullWidth
									variant="contained"
									className={classes.submit}
									onClick={() => {window.location.href="/vendor/"}}
									size="large"
								>
									Cancel
								</Button>
							</Grid>
						</Grid>
					</div>
				</form>
			</div>
		</Container>
	)
}

export default AddProduct