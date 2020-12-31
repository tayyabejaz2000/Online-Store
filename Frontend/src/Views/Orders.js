import React, { useState } from 'react'
import { cancelOrder, getOrders, returnItem } from '../Utilities/buyerUtilities'
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import {
	Accordion,
	AccordionDetails,
	AccordionSummary,
	Button,
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
					{
						orders.map((value) => {
							return (
								<Accordion>
									<AccordionSummary
										expandIcon={<ExpandMoreIcon/>}
									>
										<Typography>
											Order #{value.id} Total: {value.invoice.net}
										</Typography>
									</AccordionSummary>
									<AccordionDetails>
										<Grid
											container
											direction="column"
											spacing={1}
										>
										{ value.ordered_products.map((value) => {
											let status = ""
											switch (value.status) {
												case "P":
													status = "Placed"
													break;
												case "S":
													status = "Shipped"
													break;
												case "R":
													status = "Returned"
													break;
												case "C":
													status = "Complete"
													break
												default:
													status = ""
											}
											return (
												<Grid
													item
												>
													<Accordion>
														<AccordionSummary
														expandIcon={<ExpandMoreIcon/>}
														>
															<Typography>
																Product: {value.product.name}
															</Typography>
														</AccordionSummary>
														<AccordionDetails>
															<List>
																<ListItem>
																	<Typography variant="body2">
																		Quantity: {value.quantity}
																	</Typography>
																</ListItem>
																<ListItem>
																	<Typography variant="body2">
																		Status:
																		{ status }
																	</Typography>
																</ListItem>
																<ListItem
																	alignItems="center"
																>
																	<Button variant="contained" disabled={value.status !== "P"} name="Cancel_Button" id="Cancel_Button" onClick={(event) => { cancelOrder(value.id) }}>
																		Cancel
																	</Button>
																	<Button variant="contained" disabled={value.status!=="C"} onClick={(event) => { returnItem(value.id) }}>
																		Return Item
																	</Button>
																</ListItem>
															</List>
														</AccordionDetails>
													</Accordion>
												</Grid>
											)
										}) }
										</Grid>
									</AccordionDetails>
								</Accordion>
							)
						})
					}
				</Paper>
			</Container>
		</React.Fragment>
	)
}
export default Orders