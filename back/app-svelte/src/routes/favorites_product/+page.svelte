<!-- src/routes/favorites/+page.svelte -->
<script>
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    import { 
      getFavorites, 
      removeFromFavorites, 
      clearFavorites,
      addToShoppingBag,
    } from '$lib/products';
    
    let favorites = [];
    let isLoading = true;
    let showClearConfirm = false;
    
    let searchQuery = '';
    let sortOption = 'name-asc';
    
    onMount(() => {
      loadFavorites();
    });
    
    function loadFavorites() {
      isLoading = true;
      favorites = getFavorites();
      isLoading = false;
    }
    
    function handleRemoveFromFavorites(product) {
      removeFromFavorites(product);
      loadFavorites();
    }
    
    function handleClearAll() {
      showClearConfirm = true;
    }
    
    function confirmClearAll() {
      clearFavorites();
      loadFavorites();
      showClearConfirm = false;
    }
    
    function cancelClearAll() {
      showClearConfirm = false;
    }
    
    function goToProductDetail(product) {
      goto(`/product/${product.id}`);
    }
    
    function handleAddToCart(product, event) {
      event.stopPropagation();
      addToShoppingBag(product);
    }
    
    function goBack() {
      window.history.back();
    }
    
    function goToShop() {
      goto('/menu');
    }
    
    $: filteredFavorites = favorites
      .filter(item => {
        if (!searchQuery) return true;
        const query = searchQuery.toLowerCase();
        return (
          item.name.toLowerCase().includes(query) || 
          item.description.toLowerCase().includes(query)
        );
      })
      .sort((a, b) => {
        switch (sortOption) {
          case 'name-asc':
            return a.name.localeCompare(b.name);
          case 'name-desc':
            return b.name.localeCompare(a.name);
          case 'price-asc':
            return a.price - b.price;
          case 'price-desc':
            return b.price - a.price;
          case 'rating-desc':
            return b.rating - a.rating;
          default:
            return 0;
        }
      });
  </script>
  
  <svelte:head>
    <title>My Favorites | Coffee Shop</title>
    <meta name="description" content="View and manage your favorite coffee products" />
  </svelte:head>
  
  <main class="favorites-container">
    <header class="favorites-header">
      <div class="header-left">
        <button class="back-button" on:click={goBack}>
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M19 12H5M5 12L12 19M5 12L12 5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
        <h1>My Favorites</h1>
      </div>
      
      <div class="header-right">
        {#if favorites.length > 0}
          <button class="clear-all-button" on:click={handleClearAll}>
            Clear All
          </button>
        {/if}
      </div>
    </header>
    
    <div class="favorites-content">
      <div class="filters-bar">
        <div class="search-box">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M11 19C15.4183 19 19 15.4183 19 11C19 6.58172 15.4183 3 11 3C6.58172 3 3 6.58172 3 11C3 15.4183 6.58172 19 11 19Z" stroke="#888" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M21 21L16.65 16.65" stroke="#888" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <input 
            type="text" 
            placeholder="Search favorites..." 
            bind:value={searchQuery}
          />
          {#if searchQuery}
            <button class="clear-search" on:click={() => searchQuery = ''}>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M18 6L6 18M6 6l12 12" stroke="#aaa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>
          {/if}
        </div>
        
        <div class="sort-dropdown">
          <label for="sort">Sort by:</label>
          <select id="sort" bind:value={sortOption}>
            <option value="name-asc">Name (A-Z)</option>
            <option value="name-desc">Name (Z-A)</option>
            <option value="price-asc">Price (Low to High)</option>
            <option value="price-desc">Price (High to Low)</option>
            <option value="rating-desc">Rating (Highest)</option>
          </select>
        </div>
      </div>
      
      <div class="favorites-list">
        {#if isLoading}
          <div class="loading-state">
            <div class="spinner"></div>
            <p>Loading your favorites...</p>
          </div>
        {:else if filteredFavorites.length === 0}
          <div class="empty-state">
            {#if searchQuery}
              <div class="empty-message">
                <svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M11 19C15.4183 19 19 15.4183 19 11C19 6.58172 15.4183 3 11 3C6.58172 3 3 6.58172 3 11C3 15.4183 6.58172 19 11 19Z" stroke="#aaa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M21 21L16.65 16.65" stroke="#aaa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <h3>No matches found</h3>
                <p>We couldn't find any favorites matching "{searchQuery}"</p>
                <button class="action-button" on:click={() => searchQuery = ''}>
                  Clear search
                </button>
              </div>
            {:else}
              <div class="empty-message">
                <svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke="#aaa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <h3>Your favorites list is empty</h3>
                <p>Start adding items to your favorites while you browse our coffee selection</p>
                <button class="action-button" on:click={goToShop}>
                  Browse coffee
                </button>
              </div>
            {/if}
          </div>
        {:else}
          <div class="favorites-grid">
            {#each filteredFavorites as item (item.id)}
              <div class="favorite-card" on:click={() => goToProductDetail(item)}>
                <button 
                  class="remove-favorite" 
                  on:click={(e) => {
                    e.stopPropagation();
                    handleRemoveFromFavorites(item);
                  }}
                  title="Remove from favorites"
                >
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M18 6L6 18M6 6l12 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </button>
                
                <div class="favorite-image">
                  <img src={item.image} alt={item.name} />
                  <div class="rating">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" fill="#FFD700" stroke="#FFD700" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <span>{item.rating}</span>
                  </div>
                </div>
                
                <div class="favorite-info">
                  <h3>{item.name}</h3>
                  <p>{item.description}</p>
                  
                  <div class="price-action">
                    <span class="price">${item.price.toFixed(2)}</span>
                    <button 
                      class="add-to-cart" 
                      on:click={(e) => handleAddToCart(item, e)}
                      title="Add to cart"
                    >
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M9 22C9.55228 22 10 21.5523 10 21C10 20.4477 9.55228 20 9 20C8.44772 20 8 20.4477 8 21C8 21.5523 8.44772 22 9 22Z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M20 22C20.5523 22 21 21.5523 21 21C21 20.4477 20.5523 20 20 20C19.4477 20 19 20.4477 19 21C19 21.5523 19.4477 22 20 22Z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M1 1H5L7.68 14.39C7.77144 14.8504 8.02191 15.264 8.38755 15.5583C8.75318 15.8526 9.2107 16.009 9.68 16H19.4C19.8693 16.009 20.3268 15.8526 20.6925 15.5583C21.0581 15.264 21.3086 14.8504 21.4 14.39L23 6H6" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                      </svg>
                    </button>
                  </div>
                </div>
              </div>
            {/each}
          </div>
        {/if}
      </div>
    </div>
    
    {#if showClearConfirm}
      <div class="modal-overlay">
        <div class="modal-content">
          <h2>Clear All Favorites?</h2>
          <p>Are you sure you want to remove all items from your favorites? This action cannot be undone.</p>
          <div class="modal-actions">
            <button class="cancel-button" on:click={cancelClearAll}>Cancel</button>
            <button class="confirm-button" on:click={confirmClearAll}>Clear All</button>
          </div>
        </div>
      </div>
    {/if}
  </main>
  
  <style>
    :global(body) {
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
        Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
      background-color: #f5f5f5;
    }
    
    .favorites-container {
      width: 100%;
      max-width: 1200px;
      margin: 0 auto;
      padding: 30px;
      box-sizing: border-box;
      min-height: 100vh;
      position: relative;
    }
    
    .favorites-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 30px;
    }
    
    .header-left {
      display: flex;
      align-items: center;
      gap: 15px;
    }
    
    .back-button {
      background: none;
      border: none;
      cursor: pointer;
      width: 40px;
      height: 40px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      transition: background-color 0.2s;
      color: #333;
    }
    
    .back-button:hover {
      background-color: #eee;
    }
    
    .favorites-header h1 {
      font-size: 28px;
      margin: 0;
      color: #333;
    }
    
    .clear-all-button {
      background: none;
      border: none;
      color: #c87941;
      font-size: 16px;
      font-weight: 500;
      cursor: pointer;
      padding: 8px 16px;
      border-radius: 8px;
      transition: all 0.2s;
    }
    
    .clear-all-button:hover {
      background-color: rgba(200, 121, 65, 0.1);
    }
    
    .filters-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 30px;
      gap: 20px;
    }
    
    .search-box {
      position: relative;
      flex: 1;
      max-width: 500px;
      display: flex;
      align-items: center;
      background-color: #fff;
      border-radius: 10px;
      padding: 0 15px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }
    
    .search-box svg {
      color: #888;
    }
    
    .search-box input {
      flex: 1;
      border: none;
      padding: 14px 10px;
      font-size: 16px;
      outline: none;
      background: transparent;
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
      color: #aaa;
    }
    
    .sort-dropdown {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    
    .sort-dropdown label {
      font-size: 14px;
      color: #666;
    }
    
    .sort-dropdown select {
      padding: 10px 15px;
      border-radius: 8px;
      border: 1px solid #ddd;
      background-color: #fff;
      font-size: 14px;
      cursor: pointer;
      outline: none;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }

    .favorites-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 30px;
    }
    
    .favorite-card {
      background-color: #fff;
      border-radius: 15px;
      overflow: hidden;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
      transition: all 0.3s;
      position: relative;
      cursor: pointer;
    }
    
    .favorite-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
    }
    
    .remove-favorite {
      position: absolute;
      top: 10px;
      right: 10px;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background-color: rgba(255, 255, 255, 0.8);
      display: flex;
      align-items: center;
      justify-content: center;
      border: none;
      cursor: pointer;
      z-index: 2;
      transition: all 0.2s;
      color: #333;
    }
    
    .remove-favorite:hover {
      background-color: #fff;
      transform: scale(1.1);
    }
    
    .favorite-image {
      position: relative;
      height: 180px;
    }
    
    .favorite-image img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.3s;
    }
    
    .favorite-card:hover .favorite-image img {
      transform: scale(1.05);
    }
    
    .rating {
      position: absolute;
      bottom: 10px;
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
    
    .favorite-info {
      padding: 15px;
    }
    
    .favorite-info h3 {
      margin: 0 0 5px 0;
      font-size: 18px;
      color: #333;
    }
    
    .favorite-info p {
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
      width: 36px;
      height: 36px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: background-color 0.2s;
      color: white;
    }
    
    .add-to-cart:hover {
      background-color: #a35e2c;
    }
    
    /* Loading state */
    .loading-state {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 80px 0;
      color: #666;
    }
    
    .spinner {
      width: 40px;
      height: 40px;
      border: 4px solid rgba(200, 121, 65, 0.3);
      border-radius: 50%;
      border-top-color: #c87941;
      animation: spin 1s ease-in-out infinite;
      margin-bottom: 20px;
    }
    
    @keyframes spin {
      to { transform: rotate(360deg); }
    }

    .empty-state {
      padding: 60px 0;
    }
    
    .empty-message {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      max-width: 400px;
      margin: 0 auto;
    }
    
    .empty-message svg {
      color: #aaa;
      margin-bottom: 20px;
    }
    
    .empty-message h3 {
      font-size: 22px;
      margin: 0 0 10px 0;
      color: #333;
    }
    
    .empty-message p {
      color: #777;
      margin: 0 0 25px 0;
      line-height: 1.5;
    }
    
    .action-button {
      background-color: #c87941;
      color: white;
      border: none;
      padding: 12px 24px;
      border-radius: 8px;
      font-size: 16px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.3s;
    }
    
    .action-button:hover {
      background-color: #a35e2c;
      transform: translateY(-2px);
    }

    .modal-overlay {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-color: rgba(0, 0, 0, 0.6);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 1000;
    }
    
    .modal-content {
      background-color: #fff;
      border-radius: 15px;
      padding: 30px;
      width: 90%;
      max-width: 450px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }
    
    .modal-content h2 {
      margin: 0 0 15px 0;
      font-size: 24px;
      color: #333;
    }
    
    .modal-content p {
      margin: 0 0 25px 0;
      color: #666;
      line-height: 1.5;
    }
    
    .modal-actions {
      display: flex;
      justify-content: flex-end;
      gap: 15px;
    }
    
    .cancel-button {
      background-color: #f5f5f5;
      color: #333;
      border: none;
      padding: 12px 24px;
      border-radius: 8px;
      font-size: 16px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s;
    }
    
    .cancel-button:hover {
      background-color: #eee;
    }
    
    .confirm-button {
      background-color: #c87941;
      color: white;
      border: none;
      padding: 12px 24px;
      border-radius: 8px;
      font-size: 16px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s;
    }
    
    .confirm-button:hover {
      background-color: #a35e2c;
    }
    
    @media (max-width: 768px) {
      .favorites-container {
        padding: 20px;
      }
      
      .filters-bar {
        flex-direction: column;
        align-items: stretch;
      }
      
      .search-box {
        max-width: none;
      }
      
      .favorites-grid {
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        gap: 20px;
      }
    }
</style>