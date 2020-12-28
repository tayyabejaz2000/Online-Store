import React, {
	useState
} from 'react'
import {
	Button,
	Container,
	Divider,
	Grid,
	List,
	ListItem,
	ListItemText,
	Paper,
	TextField,
	Typography
} from '@material-ui/core'
import { getCartProducts, updateCart } from '../Utilities/buyerUtilities'
import { loginStyles } from '../MUI-Styles/Styles';

function useForceUpdate() {
    const [state, setState] = useState(false); // integer state
    return () => setState(!state); // update the state to force render
}

function Cart() {
	const classes = loginStyles()
	const [query, setQuery] = useState(false)
	const [products, setProducts] = useState([])
	const [total, setTotal] = useState(0)
	const forceUpdate = useForceUpdate();
	if (!query) {
		getCartProducts()
		.then((data) => {
			setProducts(data.products)
			setTotal(data.total)
		})
		setQuery(true)
	}
	return (
		<React.Fragment>
			<br />
			<Grid
				container
				justify="center"
			>
			<Typography variant="h2">
					Cart
			</Typography>
			<br /><br /><br /><br />
			</Grid>
			<Container>
			<Paper elevation={3}>
				<List>
					{
						products.map((value, index) => {
							let price = null
							if (value.product.discount === 0) {
								price = (
									<Typography variant="subtitle1" component="p">
										Price: {value.product.price * value.quantity}
									</Typography>
								)
							}
							else {
								price = (
									<React.Fragment>
										<Typography variant="subtitle1" component="p">
											Price:
											<strike>{(value.product.price) * (value.quantity)}</strike> {(value.product.price - (value.product.price * (value.product.discount/100))) * (value.quantity)}
										</Typography>
									</React.Fragment>
								)
							}
							return (
								<React.Fragment>
									<ListItem>
										<ListItemText primary={value.product.name} />
										<ListItemText>
											<Typography component="caption">
												{price}
											</Typography>
										</ListItemText>
										<TextField
											type="number"
											value={value.quantity}
											onChange={(event) => { products[index].quantity = event.target.value; forceUpdate() }}
											helperText="Quantity"
										>
										</TextField>
									</ListItem>
									<Divider />
								</React.Fragment>
							)
						})
					}
					</List>
					<br />
					<Paper elevation={5}>
						<Grid
							container
							justify="center"
						>
						<Typography component="p" variant="h4">
							Total: {total}
						</Typography>
						</Grid>
					<br />
					</Paper>
				</Paper>
					<Grid
						container
						justify="space-around"
						alignItems="center"
					>
						<Grid item xs={4}>
							<Button
								fullWidth
								variant="contained"
							className={classes.submit}
							onClick={() => {
								updateCart(products)
								getCartProducts()
								.then((data) => {
									setProducts(data.products)
									setTotal(data.total)
								})
							}}
								size="large"
							>
							Save
						</Button>
					</Grid>
					<Grid item xs={4}>
						<Button
							fullWidth
							variant="contained"
							className={classes.submit}
							onClick={() => {
								if (products.length > 0)
									window.location.href = "/user/placeorder"
							}}
							size="large"
						>
							Order Cart
						</Button>
					</Grid>
				</Grid>
			</Container>
		</React.Fragment>
	)
}

export default Cart