import React from 'react'
import { useParams } from 'react-router-dom'
import {
	Typography,
	Container,
	CssBaseline,
	TextField,
	Grid,
	Button,
} from '@material-ui/core'
import { useFormik } from 'formik'
import { resolveComplaint } from '../Utilities/employeeUtilities'
import {
	loginStyles
} from "../MUI-Styles/Styles"

function ResolveComplaint(props) {
	const {id} = useParams()
	const formik = useFormik({
		initialValues: {
			response: "",
			complaint_id: id,
		},
		onSubmit: resolveComplaint,
	})
	const classes = loginStyles()
	return (
		<Container component="main" maxWidth="sm">
		<CssBaseline />
		<div className={classes.paper}>
			<Typography component="h1" variant="h5">
					Resolve Complaint
			</Typography>
			<form onSubmit={formik.handleSubmit}>
				<div className={classes.form}>
				<TextField
					fullWidth
					name="response"
					id="response"
					label="Response"
					value={formik.values.response}
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
		</Container>
	)
}

export default ResolveComplaint