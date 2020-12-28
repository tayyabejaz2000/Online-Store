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
import { editProduct, getAllCategories, getProduct } from '../Utilities/productsUtilities'
import { useParams } from 'react-router-dom'

function EditProduct(props) {
	const { id } = useParams()
	const classes = formStyles()
	const [categories, setCategories] = useState([])
	const [cat_query, setCatQuery] = useState(false)
	if (!cat_query)
		getAllCategories(setCategories, setCatQuery)
	const formik = useFormik({
		initialValues: {
			id:  "",
			name: "",
			description:  "",
			stock: "",
			price:  "",
			discount:  "",
			category: "",
		},
		onSubmit: (values) => {
			editProduct(values)
			window.location.href = "/vendor/"
		}
	})
	const [prod_query, setProdQuery] = useState(false)
	if (!prod_query)
		getProduct(id, formik, setProdQuery)
	return (
		<Container component="main" maxWidth="sm">
			<CssBaseline />
			<div className={classes.paper}>
				<Typography component="h1" variant="h5">
						Update Product
				</Typography>
				<form onSubmit={formik.handleSubmit}>
					<div className={classes.form}>
						<TextField
							variant="outlined"
							margin="normal"
							required
							fullWidth
							id="name"
							label="Product Name"
							name="name"
							value={formik.values.name}
							onChange={formik.handleChange}
						/>
						<TextField
							variant="outlined"
							margin="normal"
							required
							fullWidth
							id="description"
							label="Product Description"
							name="description"
							value={formik.values.description}
							onChange={formik.handleChange}
						/>
						<TextField
							variant="outlined"
							margin="normal"
							required
							fullWidth
							type="number"
							id="stock"
							label="Stock"
							name="stock"
							value={formik.values.stock}
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
									Save
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

export default EditProduct