import React from 'react'
import {
	Tooltip,
	Grid,
	IconButton
} from '@material-ui/core'
import ProductCard from '../Components/ProductCard'
import AddShoppingCartIcon from '@material-ui/icons/AddShoppingCart';
import StarIcon from '@material-ui/icons/Star';
import { addToCart } from '../Utilities/buyerUtilities';

function UserProductCard(props) {
	const controlButtons = (
		<Grid
			container
			item
			direction="row-reverse"
			justify="flex-start"
			alignContent="baseline"
		>
			<Grid item>
				<Tooltip title="Add to Cart">
					<IconButton onClick={() => {addToCart(props.product_id, 1)}}>
						<AddShoppingCartIcon />
					</IconButton>
				</Tooltip>
				<Tooltip title="Add Review">
					<IconButton onClick={() => {window.location.href="/product/review/" + props.product_id}}>
						<StarIcon />
					</IconButton>
				</Tooltip>
			</Grid>
		</Grid>
	)
	return (
		<ProductCard productName={props.productName} category={props.category} price={props.price} discount={props.discount} control_buttons={controlButtons} onClick={props.onClick}/>
	)
}

export default UserProductCard