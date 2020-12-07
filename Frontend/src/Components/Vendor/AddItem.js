import React, { useState } from 'react'
import { TextField, Button, Grid } from "@material-ui/core";
import axiosInstance from '../../Axios/axiosAPI'


function AddItem(props)
{
    const [product_name, setProductName] = useState("")
    const [product_description, setProductDescription] = useState("")
    const [quantity,setQuantity] = useState(0)
    
    function AddProduct() {
        axiosInstance.post('/vendor/add-product/'

        )
    }

    return (
        <Grid
            container
            direction="column"
            justify="center"
            alignItems="center"
            alignContent="center"
        >
            <TextField variant="outlined"
						margin="normal"
						required
						fullWidth
						id="product_name"
						label="Product Name"
						name="product_name"
						value={product_name}
						onChange={(event)=>{setProductName(event.target.value)}}
                        autoFocus
            />
            <TextField variant="outlined"
						margin="normal"
						required
						fullWidth
						id="description"
						label="Description"
						name="description"
						value={product_description}
						onChange={(event)=>{setProductDescription(event.target.value)}}
                        autoFocus
            />
            <TextField variant="outlined"
						margin="normal"
						required
						fullWidth
						id="quantity"
						label="Quantity"
						name="quantity"
						value={quantity}
						onChange={(event)=>{setQuantity(parseInt(event.target.value))}}
                        autoFocus
            />
            <Button type="submit" value="Submit">Add Product</Button>
        </Grid>
	);
}

export default AddItem