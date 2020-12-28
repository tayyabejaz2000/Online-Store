import React, { useState } from 'react'
import { getOrders } from '../Utilities/buyerUtilities'
import {
	Container,
	Grid,
	List,
	ListItem,
	Paper,
	Typography
} from '@material-ui/core'

function Orders() {
	const [orders, setOrders] = useState([])
	const [query, setQuery] = useState(false)
	if (!query) {
		getOrders()
			.then((data) => {
			console.log(data)
			setOrders(data)
		})
		setQuery(true)
	}
	return (
		<React.Fragment>
			<Grid
				container
				justify="center"
			>
				<Typography variant="h2">
						Orders
				</Typography>
			</Grid>
			<Container>
				<Paper elevation={3}>
					<List>
					
					</List>
				</Paper>
			</Container>
		</React.Fragment>
	)
}
export default Orders