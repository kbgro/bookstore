class Cart {
  #orders = []
  #amount = 0

  constructor() {
    if (!Cart.instance) {
      Cart.instance = this;
      // this.orders = [];
    }
    // Initialize object
    return Cart.instance
  }

  // Properties & Methods
  add(product) {
    if (this.#orders.filter(e => e.id === product.id).length > 0)
      return false;
    this.#orders.push(product)
    this.#amount += product.price;
    this.#amount = this.roundAmount(this.#amount);
    return true;
  }

  remove(product) {
    this.#orders = this.#orders.filter(((value) => value.id !== product.id))
    this.#amount -= product.price;
    this.#amount = this.roundAmount(this.#amount);
  }

  roundAmount(amount) {
    return Math.round((amount + Number.EPSILON) * 100) / 100;
  }

  total() {
    return this.#amount;
  }

  clear() {
    this.#orders = [];
    this.#amount = 0;
  }

  length() {
    return this.#orders.length;
  }

  /**
   * Returns cart items array
   * @returns {*[]}
   */
  items() {
    return this.#orders;
  }
}

const instance = new Cart()
Object.freeze(instance)

export default instance
