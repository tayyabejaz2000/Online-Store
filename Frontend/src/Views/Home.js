import React from "react"
import {
	Grid, Typography,
} from "@material-ui/core"
import UserProductCard from '../Components/UserProductCard'

function Home(props) {
	return (
		<React.Fragment>
			<Typography variant="h3" component="p">
				Browse Products
			</Typography>
			<Grid
				container
			>
				<Grid item>
					<UserProductCard />
				</Grid>
			</Grid>
		</React.Fragment>
	)
}

export default Home
