import React, {
	useState
} from "react";
import {
	makeStyles,
} from '@material-ui/core/styles'
import {
	AppBar,
	Toolbar,
	Typography,
	IconButton,
	Menu,
	MenuItem,
	Button,
} from '@material-ui/core'

//Icons
import MenuIcon from '@material-ui/icons/Menu';
import AccountCircleIcon from '@material-ui/icons/AccountCircle'
import Brightness4Icon from '@material-ui/icons/Brightness4';
import Brightness7Icon from '@material-ui/icons/Brightness7';

const useStyles = makeStyles({
	title: {
		flexGrow: 1,
	},
})


function Header(props)
{
	const classes = useStyles()
	let themeIcon = <Brightness4Icon />
	const [darkTheme, themeChanger] = props.themeState()
	if (darkTheme === false)
		themeIcon = <Brightness7Icon />
	function themeChange() {
		themeChanger(!darkTheme)
	}
	return(
		<React.Fragment>
			<AppBar position="static">
					<Toolbar>
						<IconButton edge="start" color="inherit" aria-label="menu">
							<MenuIcon />
						</IconButton>
						<Typography variant="h6" className = {classes.title}>
						Online Store
						</Typography>
						<Button color="inherit" onClick={() => {window.location.href = "/login"}}>
							Login
						</Button>
						<IconButton color="inherit" aria-label="themeIcon" onClick={themeChange}>
							{themeIcon}
						</IconButton>
						<IconButton color="inherit" aria-label="account">
							<AccountCircleIcon />
						</IconButton>

					</Toolbar>
				</AppBar>
		</React.Fragment>
	)
}

export default Header