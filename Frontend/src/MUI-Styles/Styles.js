import { makeStyles } from '@material-ui/core/styles'

export const loginStyles = makeStyles((theme) => ({
	paper: {
		marginTop: theme.spacing(8),
		display: 'flex',
		flexDirection: 'column',
		alignItems: 'center',
	},
	avatar: {
		margin: theme.spacing(1),
		backgroundColor: theme.palette.secondary.main,
	},
	form: {
		width: '100%', // Fix IE 11 issue.
		marginTop: theme.spacing(1),
	},
	submit: {
		margin: theme.spacing(3, 0, 2),
	},
}))

export const headerStyles = makeStyles((theme) => ({
	title: {
		flexGrow: 1,
	},
}))

export const drawerStyles = makeStyles((theme) => ({
	list: {
	  width: 250,
	},
}))

export const productCardStyles = makeStyles((theme) => ({
	root: {
		minHeight:300,
	},
}))

export const vendorStyles = makeStyles((theme) => ({
	root: {
		margin: theme.spacing(3, 3),
	},
	shop: {
		margin: theme.spacing(3, 1),
	},
	addProduct: {
		position: 'fixed',
		left: '90%',
		top: '90%',
	},
	addCard: {
		minHeight: 410,
		minWidth: 310,
	}
}))