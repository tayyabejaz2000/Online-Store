import {
	Container,
	Grid,
	Typography
} from '@material-ui/core'
import React from 'react'

function MyAccount() {
	return (
		<Container>
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
		</Container>			
	)
}

export default MyAccount