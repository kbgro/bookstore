
/**
 * Place cart orders
 *
 * @param {Cart} cart Shopping cart
 * @param {String} token csrf token
 */
export function placeOrder(cart, token) {
  $.ajax({
    type: "POST",
    url: '/orders/',
    data: {
      "items": JSON.stringify(cart.items().map(value => value.id)),
      "total":cart.total(),
      "csrfmiddlewaretoken": token
    },
    success: function () {
      console.log("placed order");
    }
  });
}
