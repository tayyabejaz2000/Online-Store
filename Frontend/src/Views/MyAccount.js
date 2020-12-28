import {
	Container,
	Grid,
	Typography,
	TextField,
	CssBaseline,
	Button,
	Switch,
	FormControlLabel,
} from '@material-ui/core'
import { useFormik } from 'formik'
import React, { useState } from 'react'
import { loginStyles } from '../MUI-Styles/Styles'
import { getAccountDetails } from '../Utilities/accountUtilities'

function MyAccount() {
	const formik = useFormik({
		initialValues: {
			email: '',
			username: '',
			password: '',
			first_name: '',
			last_name: '',
			phone_number: '',
			wallet_password: '',
			user_type: '',
		},
		onSubmit: null,
	})
	const [query, setQuery] = useState(false)
	if (!query) {
		getAccountDetails()
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
		<Container component="main" maxWidth="sm">
			<Grid
				container
				justify="center"
			>
				<Grid item>
					<Typography component="p" variant="h3">
						My Account
					</Typography>
				</Grid>
			</Grid>
			<CssBaseline />
			<div className={classes.paper}>
				<Typography component="h1" variant="h5">
					Edit Account Details
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
									id="first_name"
									label="First Name"
									name="first_name"
									value={formik.values.first_name}
									onChange={formik.handleChange}
								/>
							</Grid>
							<Grid item xs={12} sm={6}>
								<TextField
									variant="outlined"
									margin="normal"
									fullWidth
									id="last_name"
									label="Last Name"
									name="last_name"
									value={formik.values.last_name}
									onChange={formik.handleChange}
								/>
							</Grid>
						</Grid>
						<TextField
							variant="outlined"
							margin="normal"
							fullWidth
							id="phone_number"
							label="Phone Number"
							name="phone_number"
							value={formik.values.phone_number}
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

export default MyAccount