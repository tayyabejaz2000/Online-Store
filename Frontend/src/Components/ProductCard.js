import React from 'react'
import {
	Card,
	CardContent,
	CardHeader,
	Typography,
} from '@material-ui/core'
import { productCardStyles } from '../MUI-Styles/Styles'


function ProductCard(props) {
	const classes = productCardStyles()
	return (
		<Card variant="outlined" className={classes.root}>
			<img src="https://picsum.photos/305/200" alt="null"/>
			<CardHeader
				title={"Name: " + props.productName}
				subheader={"Category: " + props.category}
			/>
			<CardContent>
				<Typography variant="body2" component="p">
					Price: {props.price}
				</Typography>
				<Typography variant="body 2" component="p">
					Stock Left: {props.quantity}
				</Typography>
			</CardContent>
			{props.control_buttons}
		</Card>
	)
}

export default ProductCard