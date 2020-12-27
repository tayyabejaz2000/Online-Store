import React, { useState } from 'react'
import {
	IconButton,
	Tooltip,
	Grid,
} from '@material-ui/core'

import DeleteIcon from '@material-ui/icons/Delete'
import EditIcon from '@material-ui/icons/Edit'

import ProductCard from './ProductCard'
import {
	deleteProduct
} from '../Utilities/vendorUtilities'

function VendorProductCard(props) {
	const [deleted, setDeleted] = useState(false)
	const controlButtons = (
		<Grid
			container
			item
			justify="flex-end"
		>
			<Grid item>
				<Tooltip title="Remove">
					<IconButton onClick={() => { deleteProduct(props.product_id); setDeleted(true) }}>
						<DeleteIcon color="error"/>
					</IconButton>
				</Tooltip>
			</Grid>
			<Grid item>
				<Tooltip title="Edit">
					<IconButton>
						<EditIcon />
					</IconButton>
				</Tooltip>
			</Grid>
		</Grid>
	)
	if (!deleted) {
		return (
			<ProductCard productName={props.productName} category={props.category} price={props.price} discount={props.discount} control_buttons={controlButtons} onClick={props.onClick}/>
			)
	}
	else {
		return (
			<React.Fragment>
			</React.Fragment>
		)
	}
}

export default VendorProductCard