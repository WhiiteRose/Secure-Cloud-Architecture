import type { Product } from '$lib/types.js';

/** @type {import('./$types').PageServerLoad} */
export async function load({
  fetch,
  request
}): Promise<{
  products: Product[],
  categories: string[]
}> {
  try {
    const [productsResponse, categoriesResponse] = await Promise.all([
      fetch('http://localhost:5000/api/shop/products'),
      fetch('http://localhost:5000/api/shop/categories')
    ]);

    const products: Product[] = await productsResponse.json();
    const categories: string[] = await categoriesResponse.json();

    return {
      products: products,
      categories: categories
    };
  } catch (error) {
    console.error('Erreur lors du chargement des produits:', error);
    return {
      products: [],
      categories: []
    };
  }
}

