import React, { useState } from 'react'
import {
	Typography,
	Container,
	CssBaseline,
	TextField,
	Grid,
	Button,
} from '@material-ui/core'
import { useFormik } from 'formik'
import { loginStyles } from '../MUI-Styles/Styles'
import { getShopDetails } from '../Utilities/vendorUtilities'
import {editShop} from '../Utilities/vendorUtilities'

function EditShop() {
	let formik = useFormik({
		initialValues: {
			name: '',
			location: '',
		},
		onSubmit: editShop,
	})
	const [query, setQuery] = useState(false)
	if (!query) {
		getShopDetails()
			.then((data) => {
			console.log(data)
			for (const key in formik.values) {
				formik.setFieldValue(key, data[key])
			}	
		})
		setQuery(true)
	}
	const classes = loginStyles()
	return (
		<Container component="div" maxWidth="sm">
			<CssBaseline />
			<div className={classes.paper}>
				<Typography component="p" variant="h3">
						Edit Shop
				</Typography>
				<form onSubmit={formik.handleSubmit}>
					<div className={classes.form}>
						<TextField
							variant="outlined"
							margin="normal"
							fullWidth
							id="name"
							name="name"
							label="Shop Name"
							value={formik.values.name}
							onChange={formik.handleChange}
						/>
						<TextField
							variant="outlined"
							margin="normal"
							fullWidth
							id="location"
							name="location"
							label="Shop Location"
							value={formik.values.location}
							onChange={formik.handleChange}
						/>
						<Grid
							container
							justify="center"
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
						</Grid>
					</div>
				</form>
			</div>
		</Container>
	)
}

export default EditShop