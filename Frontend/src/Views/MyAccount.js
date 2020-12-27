import {
	Container,
	Grid,
	Typography
} from '@material-ui/core'
import React from 'react'
import { getAccountData } from '../Utilities/accountUtilities'

function MyAccount() {
	let accountData = getAccountData()
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
						{accountData.username}
						{accountData.user_type}
					</Typography>
				</Grid>
			</Grid>
		</Container>			
	)
}

export default MyAccount