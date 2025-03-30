<!-- src/routes/details_product/[id]/+page.svelte -->
<script>
    import { page } from '$app/stores';
    import { goto } from '$app/navigation';

    let product = JSON.parse($page.url.searchParams.get('product') || '{}');
    
    let selectedSize = 'M';
    let quantity = 1;
    
    function selectSize(size) {
      selectedSize = size;
    }
    
    function increaseQuantity() {
      quantity += 1;
    }
    
    function decreaseQuantity() {
      if (quantity > 1) {
        quantity -= 1;
      }
    }
    
    function addToCart() {
      if (product) {
        console.log(`Added ${quantity} ${selectedSize} ${product.name} to cart`);
        // Logique pour ajouter au panier
      }
    }
    
    function addToFavorites() {
      if (product) {
        console.log(`Added ${product.name} to favorites`);
        // Logique pour ajouter aux favoris
      }
    }
    
    function goBack() {
      window.history.back();
    }
</script>
  
<svelte:head>
  <title>{product ? `${product.name} | Coffee Shop` : 'Chargement...'}</title>
  <meta name="description" content={product ? product.fullDescription.substring(0, 160) : 'Détails du produit'} />
</svelte:head>
  
<main class="product-detail-container">
    <div class="video-background">
      <video autoplay muted loop playsinline>
        <source src="/videos/details_product.mp4" type="video/mp4">
      </video>
      <div class="overlay"></div>
    </div>

    <div class="product-detail-wrapper">
      <header class="product-header">
        <button class="back-button" on:click={goBack}>
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M19 12H5M5 12L12 19M5 12L12 5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
        <h1>Détails</h1>
        <button class="favorite-button" on:click={addToFavorites}>
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
      </header>
      
      <div class="product-content">
        <div class="product-image-column">
          <div class="product-image-container">
            <img src={product.image} alt={product.name} />
          </div>
        </div>
        
        <div class="product-info-column">
          <div class="product-title-section">
            <h2>{product.name}</h2>
            <p class="product-subtitle">{product.description}</p>
            
            <div class="rating-container">
              <div class="rating">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="#FFD700" xmlns="http://www.w3.org/2000/svg">
                  <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" stroke="#FFD700" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <span>{product.rating} ({product.reviewCount || 0})</span>
              </div>
              
              <div class="product-actions">
                <button class="action-button">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M4 12V20C4 20.5304 4.21071 21.0391 4.58579 21.4142C4.96086 21.7893 5.46957 22 6 22H18C18.5304 22 19.0391 21.7893 19.4142 21.4142C19.7893 21.0391 20 20.5304 20 20V12" stroke="#C87941" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M16 6L12 2L8 6" stroke="#C87941" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M12 2V15" stroke="#C87941" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </button>
                <button class="action-button">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M6 9L12 15L18 9" stroke="#C87941" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </button>
              </div>
            </div>
          </div>
          
          <div class="product-description-section">
            <h3>Description</h3>
            <p>{product.fullDescription || 'Aucune description disponible'}</p>
            <button class="read-more-btn">Lire Plus</button>
          </div>
          
          <div class="product-size-section">
            <h3>Taille</h3>
            <div class="size-options">
              {#each product.sizes || ['S', 'M', 'L'] as size}
                <button 
                  class="size-button {selectedSize === size ? 'selected' : ''}" 
                  on:click={() => selectSize(size)}
                >
                  {size}
                </button>
              {/each}
            </div>
          </div>
          
          <div class="product-price-section">
            <div class="price-quantity">
              <h3>Prix</h3>
              <div class="quantity-selector">
                <button class="quantity-btn" on:click={decreaseQuantity}>-</button>
                <span>{quantity}</span>
                <button class="quantity-btn" on:click={increaseQuantity}>+</button>
              </div>
            </div>
            
            <div class="price-action">
              <div class="price-display">
                <span class="currency">$</span>
                <span class="amount">{product.price.toFixed(2)}</span>
              </div>
              
              <button class="buy-now-btn" on:click={addToCart}>
                Acheter Maintenant
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
</main>
  
<style>
  /* Styles globaux */
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
      Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    background-color: #000;
    color: #333;
    overflow-x: hidden;
    overflow-y: hidden;
  }
  
  .video-background {
    position: fixed;
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
    background: rgba(0, 0, 0, 0.5);
    z-index: 0;
  }
  
  .loading, .error-message {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100vh;
    font-size: 1.5rem;
    color: #666;
  }
  
  .product-detail-container {
    width: 100%;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    padding: 40px 20px;
    box-sizing: border-box;
    position: relative;
    z-index: 2;
  }
  
  .product-detail-wrapper {
    width: 100%;
    max-width: 1200px;
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    position: relative;
    z-index: 3;
  }
  
  /* Header */
  .product-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 20px 30px;
    border-bottom: 1px solid #eee;
  }
  
  .back-button, .favorite-button {
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
  }
  
  .back-button:hover, .favorite-button:hover {
    background-color: #f5f5f5;
  }
  
  .product-header h1 {
    font-size: 24px;
    margin: 0;
    font-weight: 600;
  }
  
  /* Product Content Layout */
  .product-content {
    display: flex;
    padding: 30px;
    gap: 50px;
  }
  
  .product-image-column {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: flex-start;
  }
  
  .product-info-column {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 30px;
  }
  
  /* Image */
  .product-image-container {
    width: 100%;
    height: 0;
    padding-bottom: 75%; /* Pour maintenir le rapport hauteur/largeur */
    position: relative;
    overflow: hidden;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    background-color: #f8f8f8;
  }
  
  .product-image-container img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s;
  }
  
  .product-image-container:hover img {
    transform: scale(1.05);
  }
  
  /* Product Title Section */
  .product-title-section {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  .product-title-section h2 {
    font-size: 28px;
    margin: 0;
    color: #333;
  }
  
  .product-subtitle {
    font-size: 16px;
    color: #666;
    margin: 0;
  }
  
  .rating-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 10px;
  }
  
  .rating {
    display: flex;
    align-items: center;
    gap: 5px;
    color: #666;
    font-size: 14px;
  }
  
  .product-actions {
    display: flex;
    gap: 10px;
  }
  
  .action-button {
    background: none;
    border: 1px solid #eee;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s;
  }
  
  .action-button:hover {
    background-color: #f9f9f9;
    border-color: #ddd;
  }
  
  /* Description */
  .product-description-section h3 {
    font-size: 18px;
    margin: 0 0 10px 0;
    color: #333;
  }
  
  .product-description-section p {
    font-size: 14px;
    line-height: 1.6;
    color: #666;
    margin: 0 0 15px 0;
  }
  
  .read-more-btn {
    background: none;
    border: none;
    color: #C87941;
    font-size: 14px;
    font-weight: 600;
    padding: 0;
    cursor: pointer;
  }
  
  .read-more-btn:hover {
    text-decoration: underline;
  }
  
  /* Size Section */
  .product-size-section h3 {
    font-size: 18px;
    margin: 0 0 15px 0;
    color: #333;
  }
  
  .size-options {
    display: flex;
    gap: 10px;
  }
  
  .size-button {
    width: 40px;
    height: 40px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    background-color: #f5f5f5;
    border: 2px solid transparent;
    color: #333;
  }
  
  .size-button:hover {
    background-color: #eee;
  }
  
  .size-button.selected {
    background-color: #C87941;
    color: white;
    border-color: #C87941;
  }
  
  /* Price Section */
  .product-price-section {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  
  .price-quantity {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .price-quantity h3 {
    font-size: 18px;
    margin: 0;
    color: #333;
  }
  
  .quantity-selector {
    display: flex;
    align-items: center;
    gap: 15px;
    background-color: #f5f5f5;
    padding: 5px 15px;
    border-radius: 10px;
  }
  
  .quantity-btn {
    background: none;
    border: none;
    width: 24px;
    height: 24px;
    font-size: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    color: #666;
    transition: color 0.2s;
  }
  
  .quantity-btn:hover {
    color: #C87941;
  }
  
  .price-action {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .price-display {
    display: flex;
    align-items: baseline;
  }
  
  .currency {
    font-size: 16px;
    color: #C87941;
    font-weight: 600;
  }
  
  .amount {
    font-size: 32px;
    font-weight: 700;
    color: #C87941;
  }
  
  .buy-now-btn {
    background-color: #C87941;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px 25px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .buy-now-btn:hover {
    background-color: #b06a35;
  }
  
  /* Responsive Styles */
  @media (max-width: 992px) {
    .product-content {
      flex-direction: column;
      gap: 30px;
    }
    
    .product-image-container {
      padding-bottom: 60%;
    }
  }
  
  @media (max-width: 768px) {
    .product-detail-container {
      padding: 0;
    }
    
    .product-detail-wrapper {
      border-radius: 0;
    }
    
    .product-header {
      padding: 15px;
    }
    
    .product-content {
      padding: 20px;
    }
    
    .price-action {
      flex-direction: column;
      gap: 15px;
      align-items: stretch;
    }
    
    .buy-now-btn {
      width: 100%;
    }
  }
</style>