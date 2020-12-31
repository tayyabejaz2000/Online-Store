import React, { useState } from 'react'
import Rating from '@material-ui/lab/Rating';
import {
	TextField,
	Typography,
	Container,
	CssBaseline,
	Grid,
	Button
} from '@material-ui/core'
import {
	loginStyles
} from "../MUI-Styles/Styles"
import {
	useFormik,
} from 'formik'
import { useParams } from 'react-router-dom';
import { addReview } from '../Utilities/productsUtilities';


function Form(props) {
	const { id } = useParams();
	const classes = loginStyles()
	const formik = useFormik({
		initialValues: {
			product_id: id,
			stars: 0,
			feedback: '',
		},
		onSubmit: addReview,
	})
	return (
		<form onSubmit={formik.handleSubmit}>
			<div className={classes.form}>
				<Typography component="legend">Stars</Typography>
				<Rating
					value={formik.values.stars}
					name="stars"
					onChange={formik.handleChange}
				/>
				<TextField
					fullWidth
					name="feedback"
					id="feedback"
					label="Feedback"
					value={formik.values.feedback}
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
							Submit
						</Button>
					</Grid>
				</Grid>
			</div>
		</form>
	)
}

function AddReview(props) {
	const classes = loginStyles()

	return (
		<Container component="main" maxWidth="sm">
		<CssBaseline />
		<div className={classes.paper}>
			<Typography component="h1" variant="h5">
					Add a Review
			</Typography>
			<Form />
		</div>
		</Container>
	)
}
export default AddReview