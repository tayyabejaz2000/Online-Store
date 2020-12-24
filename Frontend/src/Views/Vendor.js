import React from 'react'
import {
	Fab,
	Grid,
	Tooltip,
	Typography,
} from '@material-ui/core'
import AddIcon from '@material-ui/icons/Add';
import VendorProductCard from '../Components/VendorProductCard'
import { vendorStyles } from '../MUI-Styles/Styles'

export default function Vendor(props) {
	const classes = vendorStyles()
	return (
		<React.Fragment>
			<Grid
				container
				justify="flex-start"
				alignItems="flex-start"
				spacing={4}
				lg={11}
				className={classes.root}
			>
				<Grid container item justify="space-between" alignItems="flex-start">
						<Typography variant="h4" component="p">
							Your Products
						</Typography>
				</Grid>

				<Grid item>
					<VendorProductCard productName="Product 1" category="House Products" price="$56.32" quantity="20" />
				</Grid>
				<Grid item>
					<VendorProductCard productName="Product 2" category="House Products" price="$20.95" quantity="1200" />
				</Grid>
				<Grid item>
					<VendorProductCard productName="Product 3" category="Food Products" price="$20.95" quantity="1200" />
				</Grid>
				<Grid item>
					<VendorProductCard productName="Product 4" category="Food Products" price="$20.95" quantity="1200" />
				</Grid>
				<Grid item>
					<VendorProductCard productName="Product 5" category="Health Products" price="$20.95" quantity="1200" />
				</Grid>
				<Grid item>
					<VendorProductCard productName="Product 6" category="Baby Products" price="$20.95" quantity="1200" />
				</Grid>
				
				<Grid container item justify="center">
					<Tooltip title="Add Product">
						<Fab variant="extended">
								<AddIcon />
								Add a Product
						</Fab>
					</Tooltip>
				</Grid>

				
			</Grid>
			
		</React.Fragment>
	)
}