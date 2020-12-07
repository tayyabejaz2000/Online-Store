import React from 'react'
import { Typography , TextField } from "@material-ui/core";


function AddItem(props)
{
	return(
        <React.Fragment>

            <form >
            <Typography variant="h6" gutterBottom>
                Product Name*
            </Typography>
            <TextField id="product_name" label="" variant="filled" placeholder="required" />

            <Typography variant="h6" gutterBottom>
                Product Description*
            </Typography>
            <TextField id="product_description" label="" variant="filled" placeholder = "required" />

            <Typography variant="h6" gutterBottom>
                Product Quantity*
            </Typography>
            <TextField id="product_quantity" label="" variant="filled" placeholder = "required" />

            <Typography variant="h6" gutterBottom></Typography>

            <input type="submit" value="Submit" />
            </form>
      </React.Fragment>
	);
}

export default AddItem