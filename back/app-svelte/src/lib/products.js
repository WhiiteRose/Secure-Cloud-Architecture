export const categories = ['Cappuccino', 'Machiatto', 'Latte', 'Americano', "Expresso", "Mocha"];

export let shoppingBag = [];

export function addToShoppingBag(product) {
  shoppingBag.push(product);
}

export function removeFromShoppingBag(product) {
  shoppingBag = shoppingBag.filter(item => item.id !== product.id);
}

export function clearShoppingBag() {
  shoppingBag = [];
}

export function getShoppingBag() {
  return shoppingBag;
}

export function getShoppingBagTotal() {
  return shoppingBag.reduce((total, item) => total + item.price, 0);
}

export function getShoppingBagTotalQuantity() {
  return shoppingBag.reduce((total, item) => total + item.quantity, 0);
}

export let favorites = [];

export function addToFavorites(product) {
  favorites.push(product);
} 

export function removeFromFavorites(product) {
  favorites = favorites.filter(item => item.id !== product.id);
}

export function getFavorites() {
  return favorites;
} 

export function clearFavorites() {
  favorites = [];
}

export function favoritesExists(product) {
  return favorites.some(item => item.id === product.id);
}

export function getFavoritesCount() {
  return favorites.length;
}

export let codePromo = [
  {
    id: 1,
    name: 'EBQEUD5559',
    discount: 10,
  },
  {
    id: 2,
    name: 'NATHANESTTROPFORTENSVELTE45',
    discount: 9999999,
  }
];
