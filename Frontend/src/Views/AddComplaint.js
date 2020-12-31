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
import {
	useFormik,
} from 'formik'
import {
	loginStyles
} from "../MUI-Styles/Styles"
import { addComplaint } from '../Utilities/accountUtilities'
function AddComplaint() {
	const formik = useFormik({
		initialValues: {
			complaint_body: '',
		},
		onSubmit: addComplaint,
	})
	const classes = loginStyles()
	return (
		<Container component="main" maxWidth="sm">
			<Box>
			<CssBaseline />
			<div className={classes.paper}>
				<Typography component="h1" variant="h5">
						Add Complaint
				</Typography>
				<form onSubmit={formik.handleSubmit}>
					<div className={classes.form}>
					<TextField
						fullWidth
						name="complaint_body"
						id="complaint_body"
						label="Complaint"
						value={formik.values.complaint_body}
						onChange={formik.handleChange}
						style={{width:500}}
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
								Submit
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

export default AddComplaint