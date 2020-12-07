import React , {useState} from 'react'
import Button from '@material-ui/core/Button';
import Modal from "react-modal";

import AddItem from "./AddItem";
import RemoveItem from "./RemoveItem";

function VendorOptions(props)
{

	const [ addItemModal , setaddItemModal] = useState(false);
	const [ removeItemModal , setRemoveModal] = useState(false);


	return(
		<React.Fragment>
			<Button onClick={() => setaddItemModal(true) } >Add Item</Button>
            <Button onClick={() => setRemoveModal(true) }>Delete Item</Button>

		<Modal
		  isOpen={addItemModal}
		  onRequestClose={()=> setaddItemModal(false)}  
        >
			<AddItem/>
    		<button onClick={() => setaddItemModal(false) }>Cancel Placement</button>
        </Modal>

		<Modal
		  isOpen={removeItemModal}
		  onRequestClose={()=> setRemoveModal(false)}  
        >
			<RemoveItem/>
    		<button onClick={() => setRemoveModal(false) }>Done</button>
        </Modal>


		</React.Fragment>
	)
}

export default VendorOptions