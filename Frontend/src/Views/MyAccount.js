import {
	Container,
	Grid,
	Typography
} from '@material-ui/core'
import React, { useState } from 'react'
import { getAccountDetails } from '../Utilities/accountUtilities'

function MyAccount() {
	const [accountDetails, setAccountDetails] = useState({})
	getAccountDetails()
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
					<Typography component="p" variant="h3">
					</Typography>
				</Grid>
			</Grid>
		</Container>			
	)
}

export default MyAccount