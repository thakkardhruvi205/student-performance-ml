const express = require("express")
const cors = require("cors")
const mongoose = require("mongoose")

const app = express()

app.use(cors())
app.use(express.json())

mongoose.connect("mongodb://127.0.0.1:27017/inventory")

const ProductSchema = new mongoose.Schema({

customer:String,
name:String,
sku:String,
category:String,
quantity:Number,
price:Number,
total:Number,
date:String

})

const Product = mongoose.model("Product",ProductSchema)

app.get("/",(req,res)=>{
res.send("Inventory API Running")
})

app.get("/products", async(req,res)=>{

const products = await Product.find()

res.json(products)

})

app.post("/products", async(req,res)=>{

const product = new Product(req.body)

await product.save()

res.json(product)

})

app.listen(5000,()=>{
console.log("Server running on port 5000")
})