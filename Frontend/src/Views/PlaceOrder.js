import React, { useState } from 'react'
import { loginStyles } from '../MUI-Styles/Styles'
import {
	TextField,
	Typography,
	Container,
	CssBaseline,
	Button,
	Grid,
	MenuItem,
} from '@material-ui/core'
import {
	useFormik,
} from 'formik'
import {getAddBillingAddresses, placeOrder} from '../Utilities/buyerUtilities'
function PlaceOrder() {
	const [billing_addresses, setBillingAddresses] = useState([])
	const [query, setQuery] = useState(false)
	if (!query) {
		getAddBillingAddresses()
		.then((data) => {
			setBillingAddresses(data)
		})
		setQuery(true)
	}
	const formik = useFormik({
		initialValues:{
			billing_address: "",
			wallet_password: ""
		},
		onSubmit: placeOrder,
	})
	const classes = loginStyles()
	return (
		<Container component="div" maxWidth="sm">
			<CssBaseline />
			<div className={classes.paper}>
				<Typography component="p" variant="h4">
						Place Order
				</Typography>
				<form onSubmit={formik.handleSubmit}>
					<div className={classes.form}>
						<TextField
							fullWidth
							value={formik.values.billing_address}
							select
							label="Billing Address"
							required
							helperText="Select Billing Address"
							onChange={(event) => { formik.setFieldValue("billing_address", event.target.value) }}
						>
							{
								billing_addresses.map((value) => {
									return (
										<MenuItem value={value.billingAddress}>
											{value.billingAddress}
										</MenuItem>
									)
								})
							}
						</TextField>
						<TextField
							fullWidth
							type="password"
							label="Wallet Password"
							name="wallet_password"
							id="wallet_password"
							helperText="Enter Wallet Password"
							value={formik.values.wallet_password}
							onChange={formik.handleChange}
						/>
					</div>
					<Grid
						container
						justify="space-between"
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
								Place Order
							</Button>
						</Grid>
						<Grid item xs={4}>
							<Button
								fullWidth
								variant="contained"
								className={classes.submit}
								onClick={() => {window.location.href="/cart"}}
								size="large"
							>
								Cancel
							</Button>
						</Grid>
					</Grid>
				</form>
			</div>
		</Container>
	)
}

export default PlaceOrder