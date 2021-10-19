import cart from "./spa.js";

function process_product_form(productForm) {
  return {
    id: productForm.currentTarget[0].value,
    price: Number(productForm.currentTarget[1].value),
    title: productForm.currentTarget[2].value,
  };
}

function truncateChars(value, length) {
  return value.substring(0, length) + "...";
}

function addToCart(cart, product) {
  let pc = $("<div>", {"class": "d-flex justify-content-between align-items-center mb-1 dropdown-item dropdown-cart-item"})

  let col1 = $("<div>", {"class": "cart-col"});
  col1.html(truncateChars(product.title, 19));
  let col2_div = $("<div>")
  let col2 = $("<div>", {"class": "cart-col"});
  let col2_btn = $("<button>", {"class": "btn btn-primary btn-sm btn-product"});
  let col2_rm_btn = $("<button>", {"class": "btn btn-primary btn-sm btn-danger mx-1"});
  col2_rm_btn.append($("<i>", {"class": "fas fa-trash-alt"}))
  col2_btn.html(`$ ${product.price}`);
  col2.append(col2_btn);
  col2.append(col2_rm_btn);

  pc.append(col1);
  pc.append(col2);

  $("#cart-total-amount").html(`$ ${cart.total()}`);

  $("#cart-dropdown-items").append(pc);

}

$(function () {
    let form_class = ".product-book-add-cart-form";
    $(form_class).click(function (e) {
      e.preventDefault();
      let product = process_product_form(e);
      let added = cart.add(product)
      if (added) {
        addToCart(cart, product);
      }
      console.log(product)
      console.log("Total: ", cart.total());
    })
  }
)
