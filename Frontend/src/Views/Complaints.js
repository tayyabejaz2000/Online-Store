import React, {
	useState
} from 'react'
import {
	Grid,
	Container,
	Typography,
	Paper,
	List,
	ListItem,
	ListItemText,
	ListItemSecondaryAction,
	IconButton,
	Tooltip
} from '@material-ui/core'
import CheckIcon from '@material-ui/icons/Check';
import { getUnresolvedComplaints } from '../Utilities/employeeUtilities'

function Complaints() {
	const [query, setQuery] = useState(false)
	const [complaint, setComplaints] = useState([])
	if (!query) {
		getUnresolvedComplaints()
		.then((data) => {
			setComplaints(data)	
		})
		setQuery(true)
	}
	return (
		<React.Fragment>
			<br/>
			<Grid
				container
				justify="center"
			>
				<Typography variant="h2">
						Complaints
				</Typography>
			</Grid>
			<br/>
			<Container>
				<Paper elevation={2}>
					<List>
					{
						complaint.map((value) => {
							return (
								<ListItem>
									<ListItemText
										secondary={value.complaint_body}
									/>
									<ListItemSecondaryAction>
										<Tooltip title="Resolve">
											<IconButton onClick={() => {window.location.href="/employee/complaints/resolve/" + value.id}}>
												<CheckIcon />
											</IconButton>
										</Tooltip>
									</ListItemSecondaryAction>
								</ListItem>
							)
						})
					}
					</List>
				</Paper>
			</Container>
		</React.Fragment>
	)
}

export default Complaints