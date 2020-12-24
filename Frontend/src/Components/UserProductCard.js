import React from 'react'
import {
	Tooltip,
	Grid,
	Fab,
} from '@material-ui/core'
import ProductCard from '../Components/ProductCard'
import AddShoppingCartIcon from '@material-ui/icons/AddShoppingCart';

function UserProductCard(props) {
	const controlButtons = (
		<Grid
			container
			item
			justify="center"
			alignContent="baseline"
		>
			<Grid item>
				<Tooltip title="Add to Cart">
					<Fab variant="extended" onClick={null}>
						<AddShoppingCartIcon />
						Add to Cart
					</Fab>
				</Tooltip>
			</Grid>
		</Grid>
	)
	return (
		<ProductCard productName={props.productName} category={props.category} price={props.price} quantity={props.quantity} control_buttons={controlButtons} onClick={props.onClick}/>
	)
}

export default UserProductCard