const mongoose = require("mongoose");

const ProductSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true
  },

  sku: {
    type: String,
    required: true
  },

  category: {
    type: String
  },

  quantity: {
    type: Number,
    default: 0
  }
});

module.exports = mongoose.model("Product", ProductSchema);