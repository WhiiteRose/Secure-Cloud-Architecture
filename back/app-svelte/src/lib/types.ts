export interface Product {
  id: number;
  name: string;
  description: string;
  price: number;
  rating: number;
  image: string;
  fullDescription: string;
  sizes: string[];
}

export interface PageData {
  products: Product[];
} 