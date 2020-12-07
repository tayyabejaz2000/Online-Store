import React , {useState} from 'react'
import Button from '@material-ui/core/Button';
import Modal from '@material-ui/core/Modal';

import AddItem from "./AddItem";
import RemoveItem from "./RemoveItem";

function VendorOptions(props)
{
	const [ addItemModal , setaddItemModal] = useState(false);
	const [ removeItemModal , setRemoveModal] = useState(false);

	return(
		<React.Fragment>
			<Button onClick={() => setaddItemModal(true)}>Add Item</Button>
            <Button onClick={() => setRemoveModal(true) }>Delete Item</Button>

		<Modal
			open={addItemModal}
			onClose={()=> setaddItemModal(false)}
			color="inherit"
        >
			<AddItem/>
    		<Button onClick={() => setaddItemModal(false) }>Cancel Placement</Button>
        </Modal>

		<Modal
			open={removeItemModal}
			onClose={() => setRemoveModal(false)}
			color="inherit"
        >
			<RemoveItem/>
    		<Button onClick={() => setRemoveModal(false) }>Done</Button>
        </Modal>


		</React.Fragment>
	)
}

export default VendorOptions