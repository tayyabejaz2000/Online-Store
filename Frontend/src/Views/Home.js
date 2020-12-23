import React from "react"
import {
	Grid,
} from "@material-ui/core"

import UserProductCard from '../Components/UserProductCard'

function Home(props) {
	return (
		<React.Fragment>
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
