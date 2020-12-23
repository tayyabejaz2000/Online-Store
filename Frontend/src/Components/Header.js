import React, { useState } from "react"
import {
	AppBar,
	Toolbar,
	Typography,
	IconButton,
	Button,
	Drawer,
} from '@material-ui/core'

import { headerStyles } from '../MUI-Styles/Styles'

//Components
import DrawerItems from './Drawer'

//Icons
import MenuIcon from '@material-ui/icons/Menu'
import AccountCircleIcon from '@material-ui/icons/AccountCircle'
import Brightness4Icon from '@material-ui/icons/Brightness4'
import Brightness7Icon from '@material-ui/icons/Brightness7'


function Header(props)
{
	const classes = headerStyles()
	let themeIcon = (props.theme === false) ? <Brightness4Icon /> : <Brightness7Icon />
	const [drawerState, changeDrawerState] = useState(false)
	function flipDrawer() {
		changeDrawerState(!drawerState)
	}
	return(
		<React.Fragment>
			<AppBar position="static" color="inherit">
				<Toolbar>
					<IconButton edge="start" aria-label="menu" onClick={flipDrawer}>
						<MenuIcon />
					</IconButton>
					<Drawer open={drawerState} onClose={() => {changeDrawerState(false)}}>
						<DrawerItems/>
					</Drawer>
					<Typography variant="h6" className = {classes.title}>
						Online Store
					</Typography>
					<Button onClick={() => { window.location.href = "/login"}}>
						Login
					</Button>
					<IconButton aria-label="themeIcon" onClick={() => {props.onThemeChange(!props.theme)}}>
						{themeIcon}
					</IconButton>
					<IconButton aria-label="account">
						<AccountCircleIcon />
					</IconButton>
				</Toolbar>
			</AppBar>
		</React.Fragment>
	)
}

export default Header