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
} from '../Utilities/productsUtilities'

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
					<IconButton onClick={() => {window.location.href = "/vendor/editproduct/" + props.product_id}}>
						<EditIcon />
					</IconButton>
				</Tooltip>
			</Grid>
		</Grid>
	)
	if (!deleted) {
		return (
			<React.Fragment>
				<ProductCard productName={props.productName} category={props.category} price={props.price} discount={props.discount} control_buttons={controlButtons} onClick={props.onClick}/>
			</React.Fragment>
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