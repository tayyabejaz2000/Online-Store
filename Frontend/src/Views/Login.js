import React from 'react'
import {
	Avatar,
	Button,
	CssBaseline,
	TextField,
	FormControlLabel,
	Checkbox,
	Link,
	Grid,
	Typography,
	Container
} from '@material-ui/core'
import {
	useFormik,
} from 'formik'
import LockOutlinedIcon from '@material-ui/icons/LockOutlined'

import {
	loginStyles
} from "../MUI-Styles/Styles"

import {
	login,
} from '../Utilities/accountUtilities'

export default function Login(props) {
	const classes = loginStyles()
	const formik = useFormik({
		initialValues:{
			username: '',
			password: '',
			rememberMe: false,
		},
		onSubmit: login,
	})

	return (
		<Container component="main" maxWidth="xs">
			<CssBaseline />
			<div className={classes.paper}>
				<Avatar className={classes.avatar}>
					<LockOutlinedIcon />
				</Avatar>
				<Typography component="h1" variant="h5">
					Sign in
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
							autoComplete="username"
							color="inherit"
							value={formik.values.username}
							onChange={formik.handleChange}
							autoFocus
						/>
						<TextField
							variant="outlined"
							margin="normal"
							required
							fullWidth
							name="password"
							label="Password"
							type="password"
							id="password"
							autoComplete="current-password"
							value={formik.values.password}
							onChange={formik.handleChange}
						/>
						<FormControlLabel
							control={<Checkbox value={formik.values.rememberMe} onChange={()=>{formik.setFieldValue("rememberMe", !formik.values.rememberMe)}}/>}
							label="Remember me"
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
									Sign In
								</Button>
							</Grid>
						</Grid>

						<Grid container>
							<Grid item>
								<Link href="/signup" variant="body2" color="inherit">
									Don't have an account? Sign Up
								</Link>
							</Grid>
						</Grid>

					</div>
				</form>
			</div>
		</Container>
	)
}