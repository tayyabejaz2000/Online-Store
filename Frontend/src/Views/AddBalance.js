import React from 'react'
import {
	Typography,
	Container,
	CssBaseline,
	TextField,
	Grid,
	Button,
	Box
} from '@material-ui/core'
import { useFormik } from 'formik'
import { addBalance } from '../Utilities/buyerUtilities'
import {
	loginStyles
} from "../MUI-Styles/Styles"
function AddBalance() {
	const formik = useFormik({
		initialValues: {
			amount: 0,
			wallet_password: ''
		},
		onSubmit: addBalance,
	})
	const classes = loginStyles()
	return (
		<Container component="main" maxWidth="sm">
			<Box>
			<CssBaseline />
			<div className={classes.paper}>
				<Typography component="h1" variant="h5">
						Add Balance
				</Typography>
				<form onSubmit={formik.handleSubmit}>
					<div className={classes.form}>
					<TextField
						fullWidth
						name="amount"
						id="amount"
						label="Amount"
						type="number"		
						value={formik.values.amount}
						onChange={formik.handleChange}
					/>
					<TextField
						fullWidth
						name="wallet_password"
						id="wallet_password"
						label="Wallet Password"
						type="password"
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
								Add
							</Button>
						</Grid>
					</Grid>
					</div>
				</form>
				</div>
			</Box>
		</Container>
	)
}

export default AddBalance