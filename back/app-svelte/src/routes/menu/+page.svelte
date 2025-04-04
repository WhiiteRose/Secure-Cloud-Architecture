<!-- src/routes/shop/+page.svelte -->
<script lang="ts">
  import { onMount } from 'svelte';
  import { fade } from 'svelte/transition';
  import { elasticOut, cubicOut } from 'svelte/easing';
  import { page } from '$app/stores';
  import { goto } from '$app/navigation';
  import type { Product, PageData } from '$lib/types';

  import {
    getFavoritesCount,
    shoppingBag,
    getShoppingBag,
    addToShoppingBag,
  } from '$lib/products';
  
  export let data: PageData;
  let coffeeProducts: Product[] = data.products || [];
  let categories: string[] = data.categories || [];
  let selectedCategory = 'Cappuccino';
  let searchQuery = '';
  let showScrollTop = false;
  let isLoaded = false;
  let comingFromHome = false;
  let cartCount = 0;
  
  function filterByCategory(category: string): void {
    selectedCategory = category;
  }
  
  function addToCart(product: Product): void {
    console.log(product);
    addToShoppingBag(product);
    cartCount = getShoppingBag().length;
  }
  
  function handleSearch(event: KeyboardEvent): void {
    if (event.key === 'Enter') {
      console.log(`Recherche: ${searchQuery}`);
    }
  }
  
  function scrollToTop(): void {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
  
  onMount(() => {
    window.addEventListener('scroll', () => {
      showScrollTop = window.scrollY > 200;
    });

    comingFromHome = $page.url.searchParams.has('from') && 
                  $page.url.searchParams.get('from') === 'home';

    const currentUrl = window.location.href;
    const visitedUrls = JSON.parse(sessionStorage.getItem('visitedUrls') || '[]');
    const hasVisitedBefore = visitedUrls.includes(currentUrl);

    comingFromHome = comingFromHome && !hasVisitedBefore;

    if (!hasVisitedBefore) {
      visitedUrls.push(currentUrl);
      sessionStorage.setItem('visitedUrls', JSON.stringify(visitedUrls));
    }

    if (comingFromHome) {
      document.body.style.overflow = 'hidden';
    
      setTimeout(() => {
        isLoaded = true;
        setTimeout(() => {
          document.body.style.overflow = 'auto';
        }, 800);
      }, 100);
    } else {
      isLoaded = true;
      document.body.style.overflow = 'auto';
    }

    cartCount = getShoppingBag().length;

    return () => {
      window.removeEventListener('scroll', () => {});
    };
  });
  
  $: filteredProducts = coffeeProducts.filter((p: Product) => {
    const matchesCategory = p.name === selectedCategory || selectedCategory === 'All';
    const matchesSearch = searchQuery === '' || 
                         p.name.toLowerCase().includes(searchQuery.toLowerCase()) || 
                         p.description.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesCategory && matchesSearch;
  });

  function handleProductClick(product: Product): void {
    console.log(product);
    goto(`/details_product?product=${JSON.stringify(product)}`);
  }
</script>

<svelte:head>
  <title>Coffee Shop</title>
  <meta name="description" content="Explore our coffee selection" />
</svelte:head>

<main class="shop-container">
  <div class="video-background">
    <video autoplay muted loop playsinline>
      <source src="/videos/beans.mp4" type="video/mp4">
    </video>
    <div class="overlay"></div>
  </div>
  
  {#if comingFromHome}
    <div class="page-entrance-animation" class:active={isLoaded} class:from-home={comingFromHome}></div>
  {/if}

  {#if isLoaded}
    <header class="shop-header" 
      in:fade={{ duration: 800, delay: 200, easing: cubicOut }}>
      <div class="location-container">
        <div class="location-info">
          <span class="location-label">Location</span>
          <div class="location-value">
            <span>Montpellier, France</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M6 9L12 15L18 9" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <div class="user-profile">
              <img src="/images/avatar.png" alt="User profile" />
            </div>
          </div>
        </div>
      </div>
      
      <div class="search-container">
        <div class="search-box">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M11 19C15.4183 19 19 15.4183 19 11C19 6.58172 15.4183 3 11 3C6.58172 3 3 6.58172 3 11C3 15.4183 6.58172 19 11 19Z" stroke="#888" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M21 21L16.65 16.65" stroke="#888" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <input 
            type="text" 
            placeholder="Rechercher un café..." 
            bind:value={searchQuery}
            on:keydown={handleSearch}
          />
          {#if searchQuery}
            <button class="clear-search" on:click={() => searchQuery = ''}>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M18 6L6 18M6 6l12 12" stroke="#aaa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>
          {/if}
        </div>
        
        <button class="filter-button">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M4 21V14M4 10V3M12 21V12M12 8V3M20 21V16M20 12V3M1 14H7M9 8H15M17 16H23" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
      </div>
    </header>
    
    <section class="content-area">
      <div class="left-panel">
        <div class="promo-banner">
          <div class="promo-tag">Promo</div>
          <h2>Buy one get<br />one FREE</h2>
          <img src="/images/coffee-promo.png" alt="Coffee promotion" />
        </div>
        
        <div class="category-filter">
          <h3>Categories</h3>
          <ul class="category-list">
            {#each categories as category}
              <li 
                class={selectedCategory === category ? 'active' : 'no-active'}
                on:click={() => filterByCategory(category)}
              >
                {category}
              </li>
            {/each}
          </ul>
        </div>
      </div>
      
      <div class="right-panel">
        <h2>Our Selection</h2>
        
        <div class="coffee-grid">
          {#each filteredProducts as product}
            <div class="coffee-card" on:click={() => handleProductClick(product)}>
              <div class="coffee-image">
                <img src={product.image} alt={product.name} />
                <div class="rating">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" fill="#FFD700" stroke="#FFD700" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <span>{product.rating}</span>
                </div>
              </div>
              
              <div class="coffee-info">
                <h3>{product.name}</h3>
                <p>{product.description}</p>
                
                <div class="price-action">
                  <span class="price">${product.price.toFixed(2)}</span>
                  <button class="add-to-cart" on:click={(event) => {
                    event.stopPropagation();
                    addToCart(product);
                  }}>
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M12 5V19M5 12H19" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                  </button>
                </div>
              </div>
            </div>
          {/each}
        </div>
      </div>
    </section>
    
    <footer class="bottom-nav">
      <div class="nav-item active">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M3 9L12 2L21 9V20C21 20.5304 20.7893 21.0391 20.4142 21.4142C20.0391 21.7893 19.5304 22 19 22H5C4.46957 22 3.96086 21.7893 3.58579 21.4142C3.21071 21.0391 3 20.5304 3 20V9Z" stroke="#C87941" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span>Home</span>
      </div>
      <div class="nav-item" on:click={() => goto('/favorites_product')}>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke="#888" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span>Favorites ({getFavoritesCount()})</span>
      </div>
      <div class="nav-item" on:click={() => goto('/shopping_bag')}>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M9 22C9.55228 22 10 21.5523 10 21C10 20.4477 9.55228 20 9 20C8.44772 20 8 20.4477 8 21C8 21.5523 8.44772 22 9 22Z" stroke="#888" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M20 22C20.5523 22 21 21.5523 21 21C21 20.4477 20.5523 20 20 20C19.4477 20 19 20.4477 19 21C19 21.5523 19.4477 22 20 22Z" stroke="#888" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M1 1H5L7.68 14.39C7.77144 14.8504 8.02191 15.264 8.38755 15.5583C8.75318 15.8526 9.2107 16.009 9.68 16H19.4C19.8693 16.009 20.3268 15.8526 20.6925 15.5583C21.0581 15.264 21.3086 14.8504 21.4 14.39L23 6H6" stroke="#888" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span>Cart ({cartCount})</span>
      </div>
      <div class="nav-item" on:click={() => goto('/profile')}>
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M20 21V19C20 17.9391 19.5786 16.9217 18.8284 16.1716C18.0783 15.4214 17.0609 15 16 15H8C6.93913 15 5.92172 15.4214 5.17157 16.1716C4.42143 16.9217 4 17.9391 4 19V21" stroke="#888" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M12 11C14.2091 11 16 9.20914 16 7C16 4.79086 14.2091 3 12 3C9.79086 3 8 4.79086 8 7C8 9.20914 9.79086 11 12 11Z" stroke="#888" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span>Profile</span>
      </div>
    </footer>
  {/if}
  
  {#if showScrollTop}
    <button class="scroll-top-btn" on:click={scrollToTop}>
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M18 15L12 9L6 15" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </button>
  {/if}
</main>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
      Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    background-color: #000;
    color: #333;
    overflow-x: hidden;
    width: 100vw;
    max-width: 100%;
  }
  
  .video-background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
    overflow: hidden;
  }

  .video-background video {
    position: absolute;
    top: 50%;
    left: 50%;
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    transform: translateX(-50%) translateY(-50%);
    object-fit: cover;
    opacity: 0.8;
  }
  
  .overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0.2);
    z-index: 0;
  }

  .shop-container {
    width: 100%;
    max-width: 100%;
    margin: 0 auto;
    min-height: 100vh;
    background-color: rgba(0, 0, 0, 0.2);
    display: flex;
    flex-direction: column;
    position: relative;
    z-index: 2;
    box-shadow: 0 0 30px rgba(0, 0, 0, 0.5);
    overflow-x: hidden;
  }

  .shop-header {
    background-color: rgba(255, 255, 255, 0.9);
    color: #333;
    padding: 20px 30px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }
  
  .location-container {
    display: flex;
    align-items: center;
    gap: 20px;
  }
  
  .location-info {
    display: flex;
    flex-direction: column;
  }
  
  .location-label {
    font-size: 12px;
    color: #777;
  }
  
  .location-value {
    display: flex;
    align-items: center;
    gap: 5px;
    font-weight: 500;
    color: #333;
  }
  
  .location-value svg path {
    stroke: #333;
  }
  
  .user-profile img {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    object-fit: cover;
  }
  
  .search-container {
    display: flex;
    gap: 10px;
    width: 40%;
  }
  
  .search-box {
    display: flex;
    align-items: center;
    background-color: #f5f5f5;
    border-radius: 10px;
    padding: 0 15px;
    flex: 1;
    position: relative;
    transition: box-shadow 0.3s;
  }
  
  .search-box:focus-within {
    box-shadow: 0 0 0 2px #c87941;
  }
  
  .search-box input {
    background: none;
    border: none;
    color: #333;
    padding: 12px 10px;
    width: 100%;
    outline: none;
    font-size: 14px;
    transition: all 0.3s;
  }
  
  .search-box input::placeholder {
    color: #888;
    transition: color 0.3s;
  }
  
  .search-box input:focus::placeholder {
    color: #aaa;
  }
  
  .clear-search {
    background: none;
    border: none;
    padding: 0;
    margin: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: transform 0.2s;
  }
  
  .clear-search:hover {
    transform: scale(1.2);
  }
  
  .filter-button {
    background-color: #c87941;
    border: none;
    border-radius: 10px;
    width: 50px;
    height: 46px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: background-color 0.2s;
  }
  
  .filter-button:hover {
    background-color: #b06a35;
  }
  
  /* Content area */
  .content-area {
    display: flex;
    flex: 1;
    padding: 30px;
    gap: 30px;
    position: relative;
    z-index: 10;
    overflow-x: hidden;
    width: 100%;
    max-width: 100%;
    box-sizing: border-box;
  }
  
  /* Left panel */
  .left-panel {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 0;
    overflow-x: hidden;
  }
  
  /* Right panel */
  .right-panel {
    flex: 3;
    background-color: rgba(255, 255, 255, 1);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    overflow-x: hidden;
    width: 100%;
  }
  
  .coffee-card {
    background-color: #ffffff;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    transition: all 0.3s;
  }
  
  .coffee-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
  }
  
  .coffee-image {
    position: relative;
    height: 180px;
  }
  
  .coffee-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  .rating {
    position: absolute;
    top: 10px;
    left: 10px;
    background-color: rgba(0, 0, 0, 0.7);
    color: white;
    border-radius: 5px;
    padding: 4px 8px;
    font-size: 12px;
    display: flex;
    align-items: center;
    gap: 5px;
  }
  
  .coffee-info {
    padding: 15px;
  }
  
  .coffee-info h3 {
    margin: 0 0 5px 0;
    font-size: 18px;
    color: #333;
  }
  
  .coffee-info p {
    margin: 0 0 15px 0;
    color: #777;
    font-size: 14px;
  }
  
  .price-action {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .price {
    font-size: 18px;
    font-weight: 700;
    color: #333;
  }
  
  .add-to-cart {
    background-color: #c87941;
    border: none;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: background-color 0.2s;
  }
  
  .add-to-cart:hover {
    background-color: #b06a35;
  }
  
  /* Footer navigation */
  .bottom-nav {
    display: flex;
    justify-content: space-between;
    padding: 15px 100px;
    background-color: rgba(255, 255, 255, 0.9);
    border-top: 1px solid #eee;
    position: relative;
    z-index: 10;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
  }
  
  .nav-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 5px;
    cursor: pointer;
    padding: 10px 20px;
    border-radius: 10px;
    transition: all 0.2s;
  }
  
  .nav-item:hover {
    background-color: #f5f5f5;
  }
  
  .nav-item span {
    font-size: 12px;
    color: #555;
  }
  
  .nav-item.active span {
    color: #c87941;
    font-weight: 500;
  }
  
  .nav-item svg path {
    stroke: #555;
  }
  
  .nav-item.active svg path {
    stroke: #c87941;
  }
  
  /* Category filter adjustments */
  .category-filter {
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    margin-top: 25px;
    position: relative;
    z-index: 2;
  }
  
  /* Promo banner adjustments */
  .promo-banner {
    background: linear-gradient(45deg, rgba(200, 121, 65, 0.9), rgba(163, 94, 44, 0.9));
    color: white;
    border-radius: 15px;
    overflow: hidden;
    position: relative;
    height: 220px;
    display: flex;
    align-items: center;
    padding-left: 30px;
    margin-bottom: 30px;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
  }
  
  .promo-tag {
    position: absolute;
    top: 15px;
    left: 15px;
    background-color: #c87941;
    color: white;
    font-size: 12px;
    font-weight: bold;
    padding: 5px 10px;
    border-radius: 5px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
    z-index: 3;
  }
  
  .promo-banner h2 {
    font-size: 32px;
    font-weight: 700;
    z-index: 2;
    margin-right: 40%;
    line-height: 1.3;
    position: relative;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
  }
  
  .promo-banner h2::after {
    content: '';
    position: absolute;
    bottom: -8px;
    left: 0;
    width: 100%;
    height: 8px;
    background-color: #000;
    z-index: -1;
    border-radius: 4px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.8);
    opacity: 0.9;
  }
  
  .promo-banner img {
    position: absolute;
    right: 0;
    bottom: 0;
    height: 100%;
    object-fit: cover;
    opacity: 0.9;
    z-index: 1;
  }
  
  .category-filter h3 {
    margin-top: 0;
    margin-bottom: 15px;
    font-size: 18px;
    color: #333;
  }
  
  .category-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  .category-list li {
    padding: 12px 15px;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.2s;
    font-weight: 500;
  }
  
  .category-list li:hover {
    background-color: #f5f5f5;
  }
  
  .category-list li.active {
    background-color: #c87941;
    color: black;
  }

  .category-list li.no-active {
    color: black;
  }
  
  .coffee-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 25px;
    overflow-x: hidden;
  }
  
  .right-panel h2 {
    margin-top: 0;
    margin-bottom: 20px;
    font-size: 24px;
    color: #333;
  }
  
  /* Responsive design */
  @media (max-width: 992px) {
    .content-area {
      flex-direction: column;
      width: 100%;
      padding: 20px;
    }
    
    .search-container {
      width: 60%;
    }
    
    .promo-banner h2 {
      margin-right: 30%;
      font-size: 28px;
    }
    
    .bottom-nav {
      padding: 15px 50px;
    }
    
    .coffee-grid {
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    }
  }
  
  @media (max-width: 768px) {
    .shop-header {
      flex-direction: column;
      align-items: stretch;
      gap: 15px;
      padding: 15px;
    }
    
    .location-container {
      justify-content: space-between;
    }
    
    .search-container {
      width: 100%;
    }
    
    .coffee-grid {
      grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
      gap: 15px;
    }
    
    .bottom-nav {
      padding: 15px 20px;
    }
    
    .content-area {
      padding: 15px;
      gap: 15px;
    }
  }
  
  .scroll-top-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: #c87941;
    display: flex;
    align-items: center;
    justify-content: center;
    border: none;
    cursor: pointer;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    z-index: 99;
    transition: all 0.3s;
  }
  
  .scroll-top-btn:hover {
    background-color: #a35e2c;
    transform: translateY(-3px);
  }
  
  .page-entrance-animation {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: #c87941;
    z-index: 9999;
    pointer-events: none;
  }
  
  .page-entrance-animation.active {
    animation: entrance 1.5s cubic-bezier(0.86, 0, 0.07, 1) forwards;
  }
  
  .page-entrance-animation.from-home {
    transform-origin: center;
    animation: dezoom-entrance 1.5s cubic-bezier(0.22, 0.61, 0.36, 1) forwards;
  }
  
  @keyframes entrance {
    0% {
      transform: scaleY(1);
      opacity: 1;
    }
    95% {
      transform: scaleY(0);
      opacity: 1;
    }
    100% {
      transform: scaleY(0);
      opacity: 0;
      display: none;
    }
  }
  
  @keyframes dezoom-entrance {
    0% {
      transform: scale(5);
      opacity: 1;
      clip-path: circle(150% at 50% 50%);
      background: #c87941;
    }
    40% {
      transform: scale(1.5);
      opacity: 1;
      clip-path: circle(150% at 50% 50%);
    }
    80% {
      transform: scale(1);
      opacity: 0.6;
    }
    100% {
      transform: scale(1);
      opacity: 0;
      display: none;
    }
  }
</style>