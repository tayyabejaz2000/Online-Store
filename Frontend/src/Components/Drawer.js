import React from 'react'
import { List, ListItem, ListItemText, Typography } from '@material-ui/core'
import { drawerStyles } from '../MUI-Styles/Styles'

function DrawerItems(props) {
	const classes = drawerStyles()
	return (
		<div className={classes.list} role="presentation">
			<List component="nav">
				<Typography variant="h6" className = {classes.title}>
					Online Store
				</Typography>
				<ListItem button key="home">
					<ListItemText primary="Home"/>
				</ListItem>
				<ListItem button key="myOrders">
					<ListItemText primary="My Orders"/>
				</ListItem>
				<ListItem button key="home">
					<ListItemText primary="Cart"/>
				</ListItem>
			</List>
		</div>
	)
}

export default DrawerItems