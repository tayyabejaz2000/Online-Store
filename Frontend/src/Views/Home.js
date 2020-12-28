import React, { useState } from "react"
import {
	Grid,
	Typography,
} from "@material-ui/core"
import UserProductCard from '../Components/UserProductCard'
import { getAllProducts } from '../Utilities/productsUtilities'
function Home(props) {
	const [products, setProducts] = useState([])
	const [query, setQuery] = useState(false)
	if (!query) {
		getAllProducts()
		.then((data) => {
			setProducts(data)	
		})
		setQuery(true)
	}
	return (
		<React.Fragment>
			<Typography variant="h3" component="p">
				Browse Products
			</Typography>
			<Grid
				container
			>
				{
					products.map((value) => {
						return (
							<Grid item>
								<UserProductCard product_id={value.id} productName={value.name} category={value.category_id} price={value.price} discount={value.discount}/>
							</Grid>
						)
					})
				}
			</Grid>
		</React.Fragment>
	)
}

export default Home
