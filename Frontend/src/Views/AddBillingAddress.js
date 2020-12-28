import React from 'react'
import { loginStyles } from '../MUI-Styles/Styles'
import {
	TextField,
	Typography,
	Container,
	CssBaseline,
	Button,
	Grid,
} from '@material-ui/core'
import {
	useFormik,
} from 'formik'
import {addBillingAddress} from '../Utilities/buyerUtilities'

function AddBillingAddress() {
	const formik = useFormik({
		initialValues:{
			billingAddress: ""
		},
		onSubmit: addBillingAddress,
	})
	const classes = loginStyles()
	return (
		<Container component="div" maxWidth="lg">
			<CssBaseline />
			<div className={classes.paper}>
				<Typography component="p" variant="h4">
						Add Billing Address
				</Typography>
				<form onSubmit={formik.handleSubmit}>
					<div className={classes.form}>
						<TextField
							variant="outlined"
							margin="normal"
							required
							fullWidth
							id="billingAddress"
							label="Billing Address"
							name="billingAddress"
							value={formik.values.billingAddress}
							onChange={formik.handleChange}
							autoFocus
						/>
					</div>
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
								onClick={null}
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

export default AddBillingAddress