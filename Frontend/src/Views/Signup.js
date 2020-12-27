import React from 'react'
import {
	TextField,
	Typography,
	Container,
	CssBaseline,
	Button,
	Grid,
	Switch,
	FormControlLabel,
} from '@material-ui/core'
import {
	useFormik,
} from 'formik'

import {
	loginStyles
} from "../MUI-Styles/Styles"
import { signup } from '../Utilities/accountUtilities'



function Signup(props) {
	let error = null
	const classes = loginStyles()
	const formik = useFormik({
		initialValues:{
			email: '',
			username: '',
			password: '',
			firstName: '',
			lastName: '',
			phoneNumber: '',
			wallet_password: '',
			shop_name: '',
			shop_location: '',
			sellerAccount: false,
		},
		onSubmit: (values) => {
			try {
				signup(values)
			}
			catch {
				error = (
					<Typography variant="caption" component="p" color="error">
						{error.data}
					</Typography>
				)
			}
		},
	})
	let accountRelatedForm = null
	if (formik.values.sellerAccount) {
		accountRelatedForm = (
			<React.Fragment>
				<TextField
					variant="outlined"
					margin="normal"
					required
					fullWidth
					id="shop_name"
					label="Shop Name"
					name="shop_name"
					value={formik.values.shop_name}
					onChange={formik.handleChange}
				/>
				<TextField
					variant="outlined"
					margin="normal"
					required
					fullWidth
					id="shop_location"
					label="Shop Location"
					name="shop_location"
					value={formik.values.shop_location}
					onChange={formik.handleChange}
				/>
			</React.Fragment>
		)
	}
	return (
		<Container component="main" maxWidth="sm">
			<CssBaseline />
			<div className={classes.paper}>
				<Typography component="h1" variant="h5">
						Sign up
				</Typography>
				<form onSubmit={formik.handleSubmit}>
					<div className={classes.form}>
						<TextField
							variant="outlined"
							margin="normal"
							required
							fullWidth
							id="username"
							label="Username"
							name="username"
							value={formik.values.username}
							onChange={formik.handleChange}
							autoFocus
						/>
						<TextField
							variant="outlined"
							margin="normal"
							required
							fullWidth
							id="email"
							label="Email"
							name="email"
							value={formik.values.email}
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
									fullWidth
									id="firstName"
									label="First Name"
									name="firstName"
									value={formik.values.firstName}
									onChange={formik.handleChange}
								/>
							</Grid>
							<Grid item xs={12} sm={6}>
								<TextField
									variant="outlined"
									margin="normal"
									fullWidth
									id="lastName"
									label="Last Name"
									name="lastName"
									value={formik.values.lastName}
									onChange={formik.handleChange}
								/>
							</Grid>
						</Grid>
						<TextField
							variant="outlined"
							margin="normal"
							fullWidth
							id="phoneNumber"
							label="Phone Number"
							name="phoneNumber"
							value={formik.values.phoneNumber}
							onChange={formik.handleChange}
						/>
						<TextField
							variant="outlined"
							margin="normal"
							required
							fullWidth
							id="password"
							type="password"
							label="Password"
							name="password"
							value={formik.values.password}
							onChange={formik.handleChange}
						/>
						<TextField
							variant="outlined"
							margin="normal"
							fullWidth
							id="wallet_password"
							type="password"
							label="Wallet Password"
							name="wallet_password"
							value={formik.values.wallet_password}
							onChange={formik.handleChange}
						/>
						{accountRelatedForm}
						<FormControlLabel
							control={<Switch checked={formik.values.sellerAccount} value={formik.values.sellerAccount} onChange={() => (formik.setFieldValue('sellerAccount', !formik.values.sellerAccount))} />}
							label={(formik.values.sellerAccount)? "Seller Account": "Buyer Account"}
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
									Sign Up
								</Button>
							</Grid>
						</Grid>
						{ error }
					</div>
				</form>
			</div>
		</Container>
	)
}

export default Signup