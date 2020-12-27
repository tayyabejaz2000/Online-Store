import React from 'react'
import {
	Card,
	CardActionArea,
	CardContent,
	CardHeader,
	Typography,
} from '@material-ui/core'


function ProductCard(props) {
	let price = null
	if (props.discount === 0) {
		price = (
			<Typography variant="body 2" component="p">
				Price: {props.price}
			</Typography>
		)
	}
	else {
		price = (
			<React.Fragment>
				<Typography variant="subtitle1" component="p">
					Price:
					<strike>{props.price}</strike> {props.price - (props.price * (props.discount/100))}
				</Typography>
			</React.Fragment>
		)
	}
	return (
		<Card variant="outlined">
			<CardActionArea onClick={props.onClick}>
				<CardHeader
					title={"Name: " + props.productName}
					subheader={"Category: " + props.category}
					/>
				<CardContent>
					{price}
				</CardContent>
			</CardActionArea>
			{props.control_buttons}
		</Card>
	)
}

export default ProductCard