import React from 'react'
import {
	IconButton,
	Tooltip,
	Grid,
} from '@material-ui/core'

import DeleteIcon from '@material-ui/icons/Delete'
import EditIcon from '@material-ui/icons/Edit'

import ProductCard from './ProductCard'

function VendorProductCard(props) {
	const controlButtons = (
		<Grid
			container
			item
			justify="flex-end"
		>
			<Grid item>
				<Tooltip title="Remove">
					<IconButton>
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
	return (
		<ProductCard productName={props.productName} category={props.category} price={props.price} quantity={props.quantity} control_buttons={controlButtons}/>
	)
}

export default VendorProductCard