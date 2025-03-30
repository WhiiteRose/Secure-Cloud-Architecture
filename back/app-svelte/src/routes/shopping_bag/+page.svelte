<!-- src/routes/checkout/+page.svelte -->
<script>
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    import { 
      getShoppingBag, 
      removeFromShoppingBag, 
      clearShoppingBag,
      getShoppingBagTotal
    } from '$lib/products';
    
    // États
    let shoppingBag = [];
    let isLoading = true;
    let deliveryMethod = 'deliver';
    let note = '';
    let showAddNote = false;
    let deliveryFee = 1.0;
    let discountApplied = true;
    let discountAmount = 1.0;
    let paymentMethod = 'card';
    
    let deliveryAddress = {
      street: 'Jl. Kpg Sutoyo',
      details: 'Kpg. Sutoyo No. 620, Bilzen, Tanjungbalai',
      notes: ''
    };
    
    onMount(() => {
      setTimeout(() => {
        loadShoppingBag();
        isLoading = false;
      }, 500);
    });
    
    function loadShoppingBag() {
      shoppingBag = getShoppingBag();

      shoppingBag = shoppingBag.map(item => {
        if (!item.quantity) {
          return { ...item, quantity: 1 };
        }
        return item;
      });
    }
    
    function updateQuantity(index, change) {
      const newQuantity = shoppingBag[index].quantity + change;
      if (newQuantity > 0) {
        shoppingBag[index].quantity = newQuantity;
        shoppingBag = [...shoppingBag];
      } else {
        removeFromShoppingBag(shoppingBag[index]);
        loadShoppingBag();
      }
    }
    
    function handleRemoveItem(item) {
      removeFromShoppingBag(item);
      loadShoppingBag();
    }
    
    function emptyCart() {
      clearShoppingBag();
      loadShoppingBag();
    }
    
    function toggleAddNote() {
      showAddNote = !showAddNote;
    }
    
    function saveNote() {
      showAddNote = false;
    }
    
    function setDeliveryMethod(method) {
      deliveryMethod = method;
    }
    
    function setPaymentMethod(method) {
      paymentMethod = method;
    }
    
    function placeOrder() {
      console.log('Commande passée !');
      console.log('Méthode de livraison:', deliveryMethod);
      console.log('Adresse:', deliveryAddress);
      console.log('Note:', note);
      console.log('Méthode de paiement:', paymentMethod);
      console.log('Produits:', shoppingBag);

      alert('Votre commande a été passée avec succès !');
      clearShoppingBag();
      loadShoppingBag();
    }
    
    function goBack() {
      window.history.back();
    }
    
    function formatPrice(price) {
      return price.toFixed(2);
    }

    $: subtotal = shoppingBag.reduce((total, item) => {
      return total + (item.price * item.quantity);
    }, 0);
    
    $: total = subtotal + (deliveryMethod === 'deliver' ? deliveryFee : 0) - (discountApplied ? discountAmount : 0);
  </script>
  
  <svelte:head>
    <title>Checkout | Coffee Shop</title>
    <meta name="description" content="Complete your coffee order" />
  </svelte:head>
  
  <main class="checkout-container">
    <div class="video-background">
      <video autoplay muted loop playsinline>
        <source src="/videos/beans_commande.mp4" type="video/mp4">
      </video>
      <div class="overlay"></div>
    </div>

    <div class="checkout-wrapper">
      <header class="checkout-header">
        <button class="back-button" on:click={goBack}>
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M19 12H5M5 12L12 19M5 12L12 5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
        <h1>Order</h1>
        <div class="spacer"></div>
      </header>
      
      <div class="checkout-content">
        <div class="left-column">
          <section class="delivery-section">
            <div class="delivery-options">
              <button 
                class={`delivery-option ${deliveryMethod === 'deliver' ? 'active' : ''}`}
                on:click={() => setDeliveryMethod('deliver')}
              >
                Deliver
              </button>
              <button 
                class={`delivery-option ${deliveryMethod === 'pickup' ? 'active' : ''}`}
                on:click={() => setDeliveryMethod('pickup')}
              >
                Pick Up
              </button>
            </div>
            
            {#if deliveryMethod === 'deliver'}
              <div class="delivery-address">
                <h3>Delivery Address</h3>
                <div class="address-details">
                  <p class="street">{deliveryAddress.street}</p>
                  <p class="details">{deliveryAddress.details}</p>
                </div>
                <div class="address-actions">
                  <button class="address-action">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                      <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    Edit Address
                  </button>
                  <button class="address-action" on:click={toggleAddNote}>
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M12 20h9" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                      <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    Add Note
                  </button>
                </div>
                
                {#if showAddNote}
                  <div class="add-note-section">
                    <textarea 
                      bind:value={note}
                      placeholder="Add delivery instructions..."
                      rows="3"
                    ></textarea>
                    <button class="save-note-btn" on:click={saveNote}>Save Note</button>
                  </div>
                {/if}
              </div>
            {:else}
              <div class="pickup-info">
                <h3>Pick Up Information</h3>
                <p>Please pick up your order at our store:</p>
                <p class="store-address">Coffee Shop Main Branch<br>123 Coffee Street, Downtown</p>
                <p class="pickup-time">Your order will be ready in approximately 15-20 minutes.</p>
              </div>
            {/if}
          </section>
          
          <section class="order-items-section">
            <h3>Order Items</h3>
            
            {#if isLoading}
              <div class="loading-state">
                <div class="spinner"></div>
                <p>Loading your order...</p>
              </div>
            {:else if shoppingBag.length === 0}
              <div class="empty-cart">
                <svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M9 22C9.55228 22 10 21.5523 10 21C10 20.4477 9.55228 20 9 20C8.44772 20 8 20.4477 8 21C8 21.5523 8.44772 22 9 22Z" stroke="#aaa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M20 22C20.5523 22 21 21.5523 21 21C21 20.4477 20.5523 20 20 20C19.4477 20 19 20.4477 19 21C19 21.5523 19.4477 22 20 22Z" stroke="#aaa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M1 1H5L7.68 14.39C7.77144 14.8504 8.02191 15.264 8.38755 15.5583C8.75318 15.8526 9.2107 16.009 9.68 16H19.4C19.8693 16.009 20.3268 15.8526 20.6925 15.5583C21.0581 15.264 21.3086 14.8504 21.4 14.39L23 6H6" stroke="#aaa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <h4>Your cart is empty</h4>
                <p>Looks like you haven't added any items to your cart yet.</p>
                <button class="continue-shopping-btn" on:click={goBack}>
                  Continue Shopping
                </button>
              </div>
            {:else}
              <div class="cart-items">
                {#each shoppingBag as item, index}
                  <div class="cart-item">
                    <div class="item-image">
                      <img src={item.image} alt={item.name} />
                      {#if item.rating}
                        <div class="item-rating">
                          <svg width="14" height="14" viewBox="0 0 24 24" fill="#FFD700" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z" stroke="#FFD700" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"/>
                          </svg>
                          <span>{item.rating}</span>
                        </div>
                      {/if}
                    </div>
                    
                    <div class="item-details">
                      <div class="item-header">
                        <div class="item-title-row">
                          <h4>{item.name}</h4>
                          <div class="item-badges">
                            {#if item.size}
                              <span class="item-size">Taille: {item.size}</span>
                            {/if}
                            {#if item.reviewCount}
                              <span class="review-count">{item.reviewCount} avis</span>
                            {/if}
                          </div>
                        </div>
                        <p class="item-description">{item.description}</p>
                        
                        {#if item.fullDescription}
                          <div class="full-description">
                            <h5>Description complète:</h5>
                            <p>{item.fullDescription}</p>
                          </div>
                        {/if}
                      </div>
                      
                      <div class="item-controls">
                        <div class="price-info">
                          <div class="price-per-unit">
                            <span class="price-label">Prix unitaire:</span>
                            <span class="item-price">${formatPrice(item.price)}</span>
                          </div>
                          <div class="total-price">
                            <span class="price-label">Prix total:</span>
                            <span class="price-value">${formatPrice(item.price * item.quantity)}</span>
                          </div>
                        </div>
                        
                        <div class="quantity-options">
                          <div class="quantity-controls">
                            <button 
                              class="quantity-btn" 
                              on:click={() => updateQuantity(index, -1)}
                              aria-label="Diminuer la quantité"
                            >
                              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M5 12H19" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                              </svg>
                            </button>
                            <span class="quantity">{item.quantity}</span>
                            <button 
                              class="quantity-btn" 
                              on:click={() => updateQuantity(index, 1)}
                              aria-label="Augmenter la quantité"
                            >
                              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M12 5V19" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                <path d="M5 12H19" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                              </svg>
                            </button>
                          </div>
                          
                          {#if item.sizes && item.sizes.length > 0}
                            <div class="size-selector">
                              <span class="size-label">Changer la taille:</span>
                              <div class="size-options">
                                {#each item.sizes as size}
                                  <button 
                                    class="size-button {item.size === size ? 'selected' : ''}"
                                    on:click={() => {
                                      // @ts-ignore
                                      item.size = size;
                                      shoppingBag = [...shoppingBag]; 
                                    }}
                                  >
                                    {size}
                                  </button>
                                {/each}
                              </div>
                            </div>
                          {/if}
                        </div>
                      </div>
                    </div>
                    
                    <button 
                      class="remove-item-btn" 
                      on:click={() => handleRemoveItem(item)}
                      title="Supprimer"
                    >
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M18 6L6 18M6 6l12 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                      </svg>
                    </button>
                  </div>
                {/each}
                
                {#if shoppingBag.length > 0}
                  <div class="cart-actions">
                    <button class="empty-cart-btn" on:click={emptyCart}>
                      Vider le panier
                    </button>
                  </div>
                {/if}
              </div>
            {/if}
          </section>
        </div>
        
        <div class="right-column">
          <section class="payment-section">
            <h3>Payment Summary</h3>
            
            {#if discountApplied}
              <div class="discount-info">
                <div class="discount-badge">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z" fill="currentColor"/>
                    <circle cx="7" cy="7" r="2" fill="white"/>
                  </svg>
                  <span>1 Discount is applied</span>
                </div>
                <button class="view-details-btn">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M9 18l6-6-6-6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </button>
              </div>
            {/if}
            
            <div class="payment-details">
              <div class="payment-row">
                <span>Price</span>
                <span>${formatPrice(subtotal)}</span>
              </div>
              {#if deliveryMethod === 'deliver'}
                <div class="payment-row">
                  <span>Delivery Fee</span>
                  <div class="fee-with-discount">
                    <span class="original-fee">${formatPrice(deliveryFee + 1.0)}</span>
                    <span>${formatPrice(deliveryFee)}</span>
                  </div>
                </div>
              {/if}
              {#if discountApplied}
                <div class="payment-row discount-row">
                  <span>Discount</span>
                  <span>-${formatPrice(discountAmount)}</span>
                </div>
              {/if}
              <div class="payment-row total-row">
                <span>Total Payment</span>
                <span>${formatPrice(total)}</span>
              </div>
            </div>
            
            <div class="payment-methods">
              <h4>Payment Method</h4>
              <div class="payment-options">
                <button 
                  class={`payment-option ${paymentMethod === 'card' ? 'active' : ''}`} 
                  on:click={() => setPaymentMethod('card')}
                >
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect x="2" y="5" width="20" height="14" rx="2" stroke="currentColor" stroke-width="2"/>
                    <line x1="2" y1="10" x2="22" y2="10" stroke="currentColor" stroke-width="2"/>
                  </svg>
                  <span>Card</span>
                </button>
                
                <button 
                  class={`payment-option ${paymentMethod === 'wallet' ? 'active' : ''}`} 
                  on:click={() => setPaymentMethod('wallet')}
                >
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M19 5H5a2 2 0 00-2 2v10a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M22 12H17V8h5v4z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <span>Wallet</span>
                </button>
                
                <button 
                  class={`payment-option ${paymentMethod === 'cash' ? 'active' : ''}`} 
                  on:click={() => setPaymentMethod('cash')}
                >
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect x="2" y="6" width="20" height="12" rx="2" stroke="currentColor" stroke-width="2"/>
                    <circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="2"/>
                  </svg>
                  <span>Cash</span>
                </button>
              </div>
            </div>
            
            <button 
              class="order-btn" 
              on:click={placeOrder} 
              disabled={shoppingBag.length === 0}
            >
              Order
            </button>
          </section>
        </div>
      </div>
    </div>
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
    }
    
    .video-background {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: -1;
      overflow: hidden;
    }
    
    .video-background video {
      position: absolute;
      top: 50%;
      left: 50%;
      min-width: 100%;
      min-height: 100%;
      transform: translateX(-50%) translateY(-50%);
      object-fit: contain;
      opacity: 1;
    }
    
    .overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.5);
      z-index: 1;
    }
    
    .checkout-container {
      width: 100%;
      max-width: 1200px;
      margin: 0 auto;
      padding: 30px;
      box-sizing: border-box;
      min-height: 100vh;
      position: relative;
      z-index: 10;
    }
    
    .checkout-wrapper {
      display: flex;
      flex-direction: column;
      background-color: rgba(255, 255, 255, 0.95);
      border-radius: 20px;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }
    
    .checkout-header {
      display: flex;
      align-items: center;
      padding: 20px 30px;
      border-bottom: 1px solid #eee;
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
      background-color: #f5f5f5;
    }
    
    .checkout-header h1 {
      flex: 1;
      margin: 0;
      font-size: 24px;
      text-align: center;
    }
    
    .spacer {
      width: 40px;
    }
    
    .checkout-content {
      display: flex;
      padding: 30px;
      gap: 30px;
    }
    
    .left-column {
      flex: 3;
      display: flex;
      flex-direction: column;
      gap: 30px;
    }
    
    .right-column {
      flex: 2;
      display: flex;
      flex-direction: column;
      gap: 30px;
      align-self: flex-start;
      position: sticky;
      top: 30px;
    }
    
    .delivery-section {
      background-color: #fff;
      border-radius: 15px;
      overflow: hidden;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
      padding: 20px;
    }
    
    .delivery-options {
      display: flex;
      background-color: #f5f5f5;
      border-radius: 15px;
      padding: 5px;
      margin-bottom: 20px;
    }
    
    .delivery-option {
      flex: 1;
      background: none;
      border: none;
      padding: 15px;
      border-radius: 10px;
      font-size: 16px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s;
    }
    
    .delivery-option.active {
      background-color: #c87941;
      color: white;
    }
    
    .delivery-address h3, 
    .pickup-info h3, 
    .order-items-section h3,
    .payment-section h3 {
      margin: 0 0 15px 0;
      font-size: 18px;
      color: #333;
    }
    
    .address-details {
      margin-bottom: 15px;
    }
    
    .address-details p {
      margin: 0 0 5px 0;
    }
    
    .street {
      font-weight: 500;
    }
    
    .details {
      color: #666;
      font-size: 14px;
    }
    
    .address-actions {
      display: flex;
      gap: 15px;
    }
    
    .address-action {
      display: flex;
      align-items: center;
      gap: 5px;
      background: none;
      border: none;
      color: #c87941;
      font-size: 14px;
      font-weight: 500;
      cursor: pointer;
      padding: 5px 0;
    }
    
    .address-action:hover {
      text-decoration: underline;
    }
    
    .add-note-section {
      margin-top: 15px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    
    .add-note-section textarea {
      padding: 12px;
      border-radius: 10px;
      border: 1px solid #ddd;
      font-family: inherit;
      font-size: 14px;
      resize: vertical;
      min-height: 80px;
    }
    
    .save-note-btn {
      align-self: flex-end;
      background-color: #c87941;
      color: white;
      border: none;
      padding: 8px 15px;
      border-radius: 8px;
      font-size: 14px;
      font-weight: 500;
      cursor: pointer;
      transition: background-color 0.2s;
    }
    
    .save-note-btn:hover {
      background-color: #a35e2c;
    }
    
    /* Section panier */
    .order-items-section {
      background-color: #fff;
      border-radius: 15px;
      overflow: hidden;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
      padding: 20px;
    }
    
    .loading-state {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 40px 0;
    }
    
    .spinner {
      width: 40px;
      height: 40px;
      border: 4px solid rgba(200, 121, 65, 0.3);
      border-radius: 50%;
      border-top-color: #c87941;
      animation: spin 1s ease-in-out infinite;
      margin-bottom: 15px;
    }
    
    @keyframes spin {
      to { transform: rotate(360deg); }
    }
    
    .empty-cart {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 40px 0;
      text-align: center;
    }
    
    .empty-cart svg {
      color: #aaa;
      margin-bottom: 15px;
    }
    
    .empty-cart h4 {
      margin: 0 0 10px 0;
      font-size: 18px;
      color: #333;
    }
    
    .empty-cart p {
      margin: 0 0 20px 0;
      color: #666;
    }
    
    .continue-shopping-btn {
      background-color: #c87941;
      color: white;
      border: none;
      padding: 12px 20px;
      border-radius: 10px;
      font-size: 16px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s;
    }
    
    .continue-shopping-btn:hover {
      background-color: #a35e2c;
    }
    
    .cart-items {
      display: flex;
      flex-direction: column;
      gap: 15px;
    }
    
    .cart-item {
      display: flex;
      padding: 20px;
      background-color: #ffffff;
      border-radius: 16px;
      margin-bottom: 20px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
      position: relative;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      border-left: 4px solid #C87941;
    }
    
    .cart-item:hover {
      transform: translateY(-3px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    }
    
    .item-image {
      width: 120px;
      height: 120px;
      margin-right: 20px;
      border-radius: 12px;
      overflow: hidden;
      flex-shrink: 0;
      position: relative;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    
    .item-image img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.3s ease;
    }
    
    .cart-item:hover .item-image img {
      transform: scale(1.08);
    }
    
    .item-rating {
      position: absolute;
      bottom: 8px;
      left: 8px;
      background-color: rgba(0, 0, 0, 0.6);
      color: white;
      display: flex;
      align-items: center;
      gap: 4px;
      font-size: 12px;
      padding: 3px 8px;
      border-radius: 20px;
    }
    
    .item-details {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    
    .item-header {
      margin-bottom: 10px;
    }
    
    .item-title-row {
      display: flex;
      flex-direction: column;
      margin-bottom: 8px;
    }
    
    .item-badges {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 6px;
    }
    
    .item-info h4 {
      font-size: 18px;
      font-weight: 700;
      margin: 0 0 6px 0;
      color: #1a1a1a;
    }
    
    .item-size {
      font-size: 13px;
      font-weight: 500;
      color: #C87941;
      background-color: rgba(200, 121, 65, 0.1);
      padding: 4px 10px;
      border-radius: 20px;
    }
    
    .review-count {
      font-size: 13px;
      color: #666;
      background-color: #f0f0f0;
      padding: 4px 10px;
      border-radius: 20px;
    }
    
    .item-description {
      font-size: 14px;
      color: #555;
      margin: 6px 0;
      line-height: 1.5;
    }
    
    .full-description {
      margin-top: 10px;
      background-color: #f9f9f9;
      padding: 10px;
      border-radius: 8px;
      border-left: 3px solid #C87941;
    }
    
    .full-description h5 {
      margin: 0 0 5px 0;
      font-size: 14px;
      color: #444;
    }
    
    .full-description p {
      font-size: 13px;
      color: #666;
      margin: 0;
      line-height: 1.5;
    }
    
    .item-controls {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-top: 10px;
    }
    
    .price-info {
      display: flex;
      flex-direction: column;
      gap: 5px;
    }
    
    .price-per-unit {
      display: flex;
      flex-direction: column;
    }
    
    .price-label {
      font-size: 12px;
      color: #777;
    }
    
    .item-price {
      font-size: 16px;
      font-weight: 600;
      color: #C87941;
    }
    
    .total-price {
      display: flex;
      flex-direction: column;
    }
    
    .price-value {
      font-size: 18px;
      font-weight: 700;
      color: #1a1a1a;
    }
    
    .quantity-options {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 10px;
    }
    
    .quantity-controls {
      display: flex;
      align-items: center;
      background-color: #f5f5f5;
      border-radius: 30px;
      padding: 5px 12px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .quantity-btn {
      width: 30px;
      height: 30px;
      border: none;
      background: none;
      color: #444;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      border-radius: 50%;
      transition: all 0.2s;
    }
    
    .quantity-btn:hover {
      background-color: rgba(200, 121, 65, 0.15);
      color: #C87941;
      transform: scale(1.1);
    }
    
    .quantity {
      margin: 0 12px;
      font-weight: 600;
      font-size: 16px;
      min-width: 24px;
      text-align: center;
    }
    
    .size-selector {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 5px;
    }
    
    .size-label {
      font-size: 12px;
      color: #777;
    }
    
    .size-options {
      display: flex;
      gap: 5px;
    }
    
    .size-button {
      width: 30px;
      height: 30px;
      border-radius: 8px;
      border: 1px solid #e0e0e0;
      background-color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-weight: 600;
      font-size: 13px;
      color: #444;
      transition: all 0.2s;
    }
    
    .size-button:hover {
      border-color: #C87941;
      background-color: rgba(200, 121, 65, 0.05);
    }
    
    .size-button.selected {
      background-color: #C87941;
      color: white;
      border-color: #C87941;
    }
    
    .remove-item-btn {
      position: absolute;
      top: 15px;
      right: 15px;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      border: none;
      background-color: #f5f5f5;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.3s;
      color: #777;
    }
    
    .remove-item-btn:hover {
      background-color: #ffeeee;
      color: #e74c3c;
      transform: rotate(90deg) scale(1.1);
      box-shadow: 0 2px 6px rgba(231, 76, 60, 0.2);
    }
    
    .empty-cart-btn {
      background: none;
      border: 1px solid #C87941;
      color: #C87941;
      font-size: 14px;
      font-weight: 500;
      cursor: pointer;
      padding: 8px 16px;
      border-radius: 8px;
      transition: all 0.2s;
    }
    
    .empty-cart-btn:hover {
      background-color: rgba(200, 121, 65, 0.1);
      transform: translateY(-2px);
    }
    
    /* Section paiement */
    .payment-section {
      background-color: #fff;
      border-radius: 15px;
      overflow: hidden;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
      padding: 20px;
    }
    
    .discount-info {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background-color: #f9f4f0;
      padding: 12px 15px;
      border-radius: 10px;
      margin-bottom: 20px;
    }
    
    .discount-badge {
      display: flex;
      align-items: center;
      gap: 10px;
      color: #c87941;
    }
    
    .discount-badge svg {
      color: #c87941;
    }
    
    .view-details-btn {
      background: none;
      border: none;
      color: #333;
      cursor: pointer;
    }
    
    .payment-details {
      display: flex;
      flex-direction: column;
      gap: 15px;
      margin-bottom: 25px;
    }
    
    .payment-row {
      display: flex;
      justify-content: space-between;
      font-size: 16px;
    }
    
    .fee-with-discount {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
    }
    
    .original-fee {
      font-size: 14px;
      text-decoration: line-through;
    }
    
    .payment-row.discount-row {
      color: #c87941;
    }
    
</style>