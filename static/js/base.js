import cart from "./spa.js";
import {placeOrder} from "./api.js";


function process_product_form(productForm) {
  return {
    id: productForm.currentTarget[0].value,
    price: Number(productForm.currentTarget[1].value),
    title: productForm.currentTarget[2].value,
  };
}

function process_cart_product_form(productForm) {
  return {
    id: productForm.currentTarget[0].value,
    price: productForm.currentTarget[1].value
  };
}

function truncateChars(value, length) {
  return value.substring(0, length) + "...";
}

function addToCart(cart, product) {
  let pc = $("<div>", {"class": "d-flex justify-content-between align-items-center mb-1 dropdown-item dropdown-cart-item"})

  // let removeProductCartForm = $("<form>", {"class": "remove-product-cart-form form-inline", "method": "post"})
  // let col2_rm_btn = $("<button>", {"type": "submit", "class": "remove-product-cart-btn btn btn-primary btn-sm btn-danger mx-1"});
  // col2_rm_btn.append($("<i>", {"class": "fas fa-trash-alt"}))
  // removeProductCartForm.append($("<input>", {"type": "hidden", "name": "id", "value": product.id}))
  // removeProductCartForm.append($("<input>", {"type": "hidden", "name": "price", "value": product.price}))
  // removeProductCartForm.append(col2_rm_btn)

  let col1 = $("<div>", {"class": "cart-col"});
  col1.html(truncateChars(product.title, 19));
  let col2 = $("<div>", {"class": "cart-col d-flex justify-content-around"});
  let col2_btn = $("<button>", {"class": "btn btn-primary btn-sm btn-product"});
  // let col2_rm_btn = $("<button>", {"class": "btn btn-primary btn-sm btn-danger mx-1"});
  // col2_rm_btn.append($("<i>", {"class": "fas fa-trash-alt"}))
  col2_btn.html(`$ ${product.price}`);
  col2.append(col2_btn);
  // col2.append(removeProductCartForm);

  pc.append(col1);
  pc.append(col2);

  $("#cart-total-amount").html(`$ ${cart.total()}`);

  $("#cart-dropdown-items").append(pc);
}

/**
 *
 * @param cart
 * @param product
 */
function removeFromCart(cart, product) {

}

$(function () {
    let form_class = ".product-book-add-cart-form";
    let cart_product_form_class = ".remove-product-cart-btn";
    let clear_cart_btn = "#clear-cart-btn";
    let drop_down_items = "#cart-dropdown-items";
    let place_order_form = "#place-order-form";

    // add item to cart
    $(form_class).click(function (e) {
      e.preventDefault();
      let product = process_product_form(e);
      let added = cart.add(product)
      if (added) {
        $("#cart-items").html(cart.length())
        addToCart(cart, product);
      }
      console.log(product)
      console.log("Total: ", cart.total());
    })

    $(clear_cart_btn).click(function (e) {
      cart.clear();
      $(drop_down_items).empty();
      $("#cart-items").html(cart.length())
      $("#cart-total-amount").html(`$ ${cart.total()}`);
      console.log("Total: ", cart.total());
    })

    $(place_order_form).click(function (e) {
      e.preventDefault();
      let token = $(this).find('input[name=csrfmiddlewaretoken]:eq(0)').val();
      console.log(token, cart.items());
      placeOrder(cart, token);
    })
  }
)
