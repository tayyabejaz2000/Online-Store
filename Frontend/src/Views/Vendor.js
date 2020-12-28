import React, { useState } from 'react'
import {
	Fab,
	Grid,
	Tooltip,
	Typography,
} from '@material-ui/core'
import AddIcon from '@material-ui/icons/Add';
import VendorProductCard from '../Components/VendorProductCard'
import { vendorStyles } from '../MUI-Styles/Styles'
import { getVendorProducts } from '../Utilities/vendorUtilities';

export default function Vendor(props) {
	const classes = vendorStyles()
	const [products, setProducts] = useState([])
	const [query, setQuery] = useState(false)
	if (!query)
		getVendorProducts(setProducts, setQuery)
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

				{
					products.map((value) => {
						console.log(value)
						return (
							<VendorProductCard product_id={value.id} productName={value.name} category={value.category_id} price={value.price} discount={value.discount} />
					)})
				}
				
				<Grid container item justify="center">
					<Tooltip title="Add Product">
						<Fab variant="extended" title="Add a Product" onClick={() => {window.location.href = "/vendor/addproduct/"}}>
								<AddIcon />
								Add a Product
						</Fab>
					</Tooltip>
				</Grid>

				
			</Grid>
			
		</React.Fragment>
	)
}