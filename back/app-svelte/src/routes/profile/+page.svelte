<!-- src/routes/profile/+page.svelte -->
<script>
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    
    // État utilisateur
    let user = {
      name: 'Alex Martin',
      email: 'alex.martin@example.com',
      phone: '+33 6 12 34 56 78',
      profileImage: '/images/avatar.png',
      memberSince: 'December 2023',
      loyaltyPoints: 245,
      preferences: [
        { id: 1, name: 'Cappuccino', quantity: 12 },
        { id: 2, name: 'Latte', quantity: 8 },
        { id: 3, name: 'Americano', quantity: 5 }
      ]
    };
    
    // Historique des commandes
    let orders = [
      {
        id: 'ORD-7829',
        date: '28 March 2025',
        items: [
          { name: 'Cappuccino', size: 'M', quantity: 2 },
          { name: 'Croissant', quantity: 1 }
        ],
        total: 12.50,
        status: 'Delivered'
      },
      {
        id: 'ORD-6542',
        date: '15 March 2025',
        items: [
          { name: 'Americano', size: 'L', quantity: 1 },
          { name: 'Latte', size: 'M', quantity: 1 }
        ],
        total: 9.75,
        status: 'Delivered'
      },
      {
        id: 'ORD-5421',
        date: '2 March 2025',
        items: [
          { name: 'Cappuccino', size: 'M', quantity: 1 },
          { name: 'Machiatto', size: 'S', quantity: 1 },
          { name: 'Chocolate Muffin', quantity: 2 }
        ],
        total: 15.20,
        status: 'Delivered'
      }
    ];
    
    // Adresses de livraison
    let addresses = [
      {
        id: 1,
        title: 'Home',
        street: 'Jl. Kpg Sutoyo',
        details: 'Kpg. Sutoyo No. 620, Bilzen, Tanjungbalai',
        isDefault: true
      },
      {
        id: 2,
        title: 'Office',
        street: 'Avenue des Champs-Élysées',
        details: '123 Avenue des Champs-Élysées, 75008 Paris',
        isDefault: false
      }
    ];
    
    // Méthodes de paiement
    let paymentMethods = [
      {
        id: 1,
        type: 'card',
        title: 'Visa ending in 4242',
        icon: 'visa',
        expiry: '05/27',
        isDefault: true
      },
      {
        id: 2,
        type: 'wallet',
        title: 'Apple Pay',
        icon: 'apple',
        isDefault: false
      }
    ];
    
    // État actif
    let activeTab = 'profile';
    let editMode = false;
    let editableUser = { ...user };
    
    function setActiveTab(tab) {
      activeTab = tab;
    }
    
    function toggleEditMode() {
      editMode = !editMode;
      if (editMode) {
        editableUser = { ...user };
      } else {
        // Annuler les modifications
        editableUser = { ...user };
      }
    }
    
    function saveProfile() {
      user = { ...editableUser };
      editMode = false;
      // Afficher une notification de succès
      alert('Profile updated successfully!');
    }
    
    function logout() {
      // Logique de déconnexion
      goto('/');
    }
    
    function goBack() {
      window.history.back();
    }
    
    function viewOrderDetails(orderId) {
      // Rediriger vers la page de détails de commande
      console.log(`View order ${orderId}`);
    }
    
    function editAddress(addressId) {
      // Ouvrir modal d'édition d'adresse
      console.log(`Edit address ${addressId}`);
    }
    
    function deleteAddress(addressId) {
      // Supprimer une adresse
      addresses = addresses.filter(addr => addr.id !== addressId);
    }
    
    function addNewAddress() {
      // Ouvrir modal pour ajouter une adresse
      console.log('Add new address');
    }
    
    function editPaymentMethod(paymentId) {
      // Ouvrir modal d'édition de méthode de paiement
      console.log(`Edit payment method ${paymentId}`);
    }
    
    function deletePaymentMethod(paymentId) {
      // Supprimer une méthode de paiement
      paymentMethods = paymentMethods.filter(method => method.id !== paymentId);
    }
    
    function addNewPaymentMethod() {
      // Ouvrir modal pour ajouter une méthode de paiement
      console.log('Add new payment method');
    }
    
    function formatPrice(price) {
      return price.toFixed(2);
    }
  </script>
  
  <svelte:head>
    <title>My Profile | Coffee Shop</title>
    <meta name="description" content="Manage your coffee shop profile" />
  </svelte:head>
  
  <main class="profile-container">
    <div class="video-background">
      <video autoplay muted loop playsinline>
        <source src="/videos/beans.mp4" type="video/mp4">
      </video>
      <div class="overlay"></div>
    </div>
  
    <div class="profile-wrapper">
      <header class="profile-header">
        <button class="back-button" on:click={goBack}>
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M19 12H5M5 12L12 19M5 12L12 5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
        <h1>My Profile</h1>
        <button class="logout-button" on:click={logout}>
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M9 21H5a2 2 0 01-2-2V5a2 2 0 012-2h4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M16 17l5-5-5-5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M21 12H9" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          <span>Logout</span>
        </button>
      </header>
      
      <div class="profile-content">
        <div class="profile-sidebar">
          <div class="user-card">
            <div class="user-avatar-container">
              <img src={user.profileImage} alt={user.name} class="user-avatar" />
              <button class="edit-avatar-btn">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
            </div>
            
            <div class="user-info">
              <h2>{user.name}</h2>
              <p>Member since {user.memberSince}</p>
              <div class="loyalty-badge">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M12 15a3 3 0 100-6 3 3 0 000 6z" fill="currentColor"/>
                  <path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <span>{user.loyaltyPoints} points</span>
              </div>
            </div>
          </div>
          
          <nav class="profile-nav">
            <button 
              class={`nav-item ${activeTab === 'profile' ? 'active' : ''}`}
              on:click={() => setActiveTab('profile')}
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <circle cx="12" cy="7" r="4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span>My Profile</span>
            </button>
            
            <button 
              class={`nav-item ${activeTab === 'orders' ? 'active' : ''}`}
              on:click={() => setActiveTab('orders')}
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 8v4l3 3M21 12a9 9 0 11-18 0 9 9 0 0118 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span>Order History</span>
            </button>
            
            <button 
              class={`nav-item ${activeTab === 'addresses' ? 'active' : ''}`}
              on:click={() => setActiveTab('addresses')}
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <circle cx="12" cy="10" r="3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span>My Addresses</span>
            </button>
            
            <button 
              class={`nav-item ${activeTab === 'payment' ? 'active' : ''}`}
              on:click={() => setActiveTab('payment')}
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="2" y="5" width="20" height="14" rx="2" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M2 10h20" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span>Payment Methods</span>
            </button>
            
            <button 
              class={`nav-item ${activeTab === 'preferences' ? 'active' : ''}`}
              on:click={() => setActiveTab('preferences')}
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M4 21c0-3 2-4 2-4h12s2 1 2 4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M12 15c3.314 0 6-2.686 6-6s-2.686-6-6-6-6 2.686-6 6 2.686 6 6 6z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M12 9V6M9 9h6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <span>My Preferences</span>
            </button>
          </nav>
        </div>
        
        <div class="profile-main">
          {#if activeTab === 'profile'}
            <section class="tab-content">
              <div class="section-header">
                <h2>Personal Information</h2>
                <button class="edit-button" on:click={toggleEditMode}>
                  {#if !editMode}
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                      <path d="M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <span>Edit</span>
                  {:else}
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M18 6L6 18M6 6l12 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <span>Cancel</span>
                  {/if}
                </button>
              </div>
              
              <div class="card">
                {#if !editMode}
                  <div class="info-grid">
                    <div class="info-item">
                      <span class="info-label">Full Name</span>
                      <span class="info-value">{user.name}</span>
                    </div>
                    <div class="info-item">
                      <span class="info-label">Email</span>
                      <span class="info-value">{user.email}</span>
                    </div>
                    <div class="info-item">
                      <span class="info-label">Phone Number</span>
                      <span class="info-value">{user.phone}</span>
                    </div>
                    <div class="info-item">
                      <span class="info-label">Member Since</span>
                      <span class="info-value">{user.memberSince}</span>
                    </div>
                  </div>
                {:else}
                  <form class="edit-form">
                    <div class="form-group">
                      <label for="name">Full Name</label>
                      <input 
                        type="text" 
                        id="name" 
                        bind:value={editableUser.name} 
                        placeholder="Enter your full name"
                      />
                    </div>
                    <div class="form-group">
                      <label for="email">Email</label>
                      <input 
                        type="email" 
                        id="email" 
                        bind:value={editableUser.email} 
                        placeholder="Enter your email"
                      />
                    </div>
                    <div class="form-group">
                      <label for="phone">Phone Number</label>
                      <input 
                        type="tel" 
                        id="phone" 
                        bind:value={editableUser.phone} 
                        placeholder="Enter your phone number"
                      />
                    </div>
                    <div class="form-actions">
                      <button type="button" class="cancel-btn" on:click={toggleEditMode}>Cancel</button>
                      <button type="button" class="save-btn" on:click={saveProfile}>Save Changes</button>
                    </div>
                  </form>
                {/if}
              </div>
              
              <div class="section-header">
                <h2>Notification Settings</h2>
              </div>
              
              <div class="card">
                <div class="toggle-list">
                  <div class="toggle-item">
                    <div class="toggle-info">
                      <h3>Order Status</h3>
                      <p>Receive updates about your orders</p>
                    </div>
                    <label class="toggle-switch">
                      <input type="checkbox" checked>
                      <span class="toggle-slider"></span>
                    </label>
                  </div>
                  
                  <div class="toggle-item">
                    <div class="toggle-info">
                      <h3>Promotions</h3>
                      <p>Receive offers and discounts</p>
                    </div>
                    <label class="toggle-switch">
                      <input type="checkbox" checked>
                      <span class="toggle-slider"></span>
                    </label>
                  </div>
                  
                  <div class="toggle-item">
                    <div class="toggle-info">
                      <h3>Newsletter</h3>
                      <p>Receive our monthly coffee letter</p>
                    </div>
                    <label class="toggle-switch">
                      <input type="checkbox">
                      <span class="toggle-slider"></span>
                    </label>
                  </div>
                </div>
              </div>
            </section>
          {:else if activeTab === 'orders'}
            <section class="tab-content">
              <div class="section-header">
                <h2>Order History</h2>
              </div>
              
              {#if orders.length === 0}
                <div class="empty-state">
                  <svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M22 12H2M16 6l6 6-6 6" stroke="#aaa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <h3>No orders yet</h3>
                  <p>You haven't placed any orders yet. Start browsing our coffee selection.</p>
                  <button class="action-button" on:click={() => goto('/')}>Browse Coffee</button>
                </div>
              {:else}
                <div class="orders-list">
                  {#each orders as order}
                    <div class="order-card" on:click={() => viewOrderDetails(order.id)}>
                      <div class="order-header">
                        <div class="order-id">
                          <span class="label">Order ID</span>
                          <span class="value">{order.id}</span>
                        </div>
                        <div class="order-date">
                          <span class="label">Date</span>
                          <span class="value">{order.date}</span>
                        </div>
                        <div class="order-status">
                          <span class={`status-badge ${order.status.toLowerCase()}`}>
                            {order.status}
                          </span>
                        </div>
                      </div>
                      
                      <div class="order-items">
                        {#each order.items as item}
                          <div class="order-item">
                            <div class="item-name">
                              {item.name} {item.size ? `(${item.size})` : ''}
                            </div>
                            <div class="item-quantity">x{item.quantity}</div>
                          </div>
                        {/each}
                      </div>
                      
                      <div class="order-footer">
                        <div class="order-total">
                          <span class="label">Total</span>
                          <span class="value">${formatPrice(order.total)}</span>
                        </div>
                        <button class="details-btn">
                          View Details
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M9 18l6-6-6-6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                          </svg>
                        </button>
                      </div>
                    </div>
                  {/each}
                </div>
              {/if}
            </section>
          {:else if activeTab === 'addresses'}
            <section class="tab-content">
              <div class="section-header">
                <h2>My Addresses</h2>
                <button class="add-button" on:click={addNewAddress}>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <span>Add New</span>
                </button>
              </div>
              
              {#if addresses.length === 0}
                <div class="empty-state">
                  <svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z" stroke="#aaa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <circle cx="12" cy="10" r="3" stroke="#aaa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <h3>No addresses yet</h3>
                  <p>You haven't added any delivery addresses yet.</p>
                  <button class="action-button" on:click={addNewAddress}>Add New Address</button>
                </div>
              {:else}
                <div class="address-list">
                  {#each addresses as address}
                    <div class="address-card">
                      {#if address.isDefault}
                        <div class="default-badge">Default</div>
                      {/if}
                      
                      <div class="address-header">
                        <h3>{address.title}</h3>
                        <div class="address-actions">
                          <button 
                            class="address-action-btn" 
                            on:click|stopPropagation={() => editAddress(address.id)}
                          >
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <path d="M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                              <path d="M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                          </button>
                          <button 
                            class="address-action-btn delete" 
                            on:click|stopPropagation={() => deleteAddress(address.id)}
                          >
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <path d="M3 6h18M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2M10 11v6M14 11v6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                          </button>
                        </div>
                      </div>
                      
                      <div class="address-details">
                        <p class="street">{address.street}</p>
                        <p class="details">{address.details}</p>
                      </div>
                      
                      {#if !address.isDefault}
                        <button class="set-default-btn">
                          Set as Default
                        </button>
                      {/if}
                    </div>
                  {/each}
                </div>
              {/if}
            </section>
          {:else if activeTab === 'payment'}
            <section class="tab-content">
              <div class="section-header">
                <h2>Payment Methods</h2>
                <button class="add-button" on:click={addNewPaymentMethod}>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <span>Add New</span>
                </button>
              </div>
              
              {#if paymentMethods.length === 0}
                <div class="empty-state">
                  <svg width="64" height="64" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect x="2" y="5" width="20" height="14" rx="2" stroke="#aaa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M2 10h20" stroke="#aaa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <h3>No payment methods</h3>
                  <p>You haven't added any payment methods yet.</p>
                  <button class="action-button" on:click={addNewPaymentMethod}>Add Payment Method</button>
                </div>
              {:else}
                <div class="payment-list">
                  {#each paymentMethods as method}
                    <div class="payment-card">
                      {#if method.isDefault}
                        <div class="default-badge">Default</div>
                      {/if}
                      
                      <div class="payment-header">
                        <div class="payment-icon {method.icon}">
                          {#if method.type === 'card'}
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <rect x="2" y="5" width="20" height="14" rx="2" fill="#1A1F71"/>
                              <path d="M2 10h20" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                          {:else if method.type === 'wallet'}
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <path d="M19 5H5a2 2 0 00-2 2v10a2 2 0 002 2h14a2 2 0 002-2V7a2 2 0 00-2-2z" fill="#000"/>
                              <path d="M22 12H17V8h5v4z" fill="#222"/>
                            </svg>
                          {/if}
                        </div>
                        <div class="payment-info">
                          <h3>{method.title}</h3>
                          {#if method.expiry}
                            <p>Expires {method.expiry}</p>
                          {/if}
                        </div>
                        <div class="payment-actions">
                          <button 
                            class="payment-action-btn" 
                            on:click|stopPropagation={() => editPaymentMethod(method.id)}
                          >
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <path d="M11 4H4a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2v-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                              <path d="M18.5 2.5a2.121 2.121 0 013 3L12 15l-4 1 1-4 9.5-9.5z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                          </button>
                          <button 
                            class="payment-action-btn delete" 
                            on:click|stopPropagation={() => deletePaymentMethod(method.id)}
                          >
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <path d="M3 6h18M19 6v14a2 2 0 01-2 2H7a2 2 0 01-2-2V6m3 0V4a2 2 0 012-2h4a2 2 0 012 2v2M10 11v6M14 11v6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                          </button>
                        </div>
                      </div>
                      
                      {#if !method.isDefault}
                        <button class="set-default-btn">
                          Set as Default
                        </button>
                      {/if}
                    </div>
                  {/each}
                </div>
              {/if}
            </section>
          {:else if activeTab === 'preferences'}
            <section class="tab-content">
              <div class="section-header">
                <h2>My Coffee Preferences</h2>
              </div>
              
              <div class="card">
                <h3 class="preferences-title">Your Favorite Coffees</h3>
                
                {#if user.preferences.length === 0}
                  <div class="empty-preference">
                    <p>You haven't ordered any coffee yet. Start browsing our selection.</p>
                    <button class="action-button" on:click={() => goto('/')}>Browse Coffee</button>
                  </div>
                {:else}
                  <div class="preferences-chart">
                    <div class="chart-container">
                      <div class="chart-bars">
                        {#each user.preferences as pref}
                          <div class="chart-bar-container">
                            <div class="chart-label">{pref.name}</div>
                            <div class="chart-bar">
                              <div class="chart-bar-fill" style={`width: ${(pref.quantity / Math.max(...user.preferences.map(p => p.quantity))) * 100}%`}>
                                <span class="chart-value">{pref.quantity}</span>
                              </div>
                            </div>
                          </div>
                        {/each}
                      </div>
                    </div>
                    
                    <div class="preferences-list">
                      <h4>Based on your preferences, you might like:</h4>
                      <ul class="recommendation-list">
                        <li class="recommendation-item">
                          <span class="recommendation-name">Mocha</span>
                          <button class="try-button">Try it</button>
                        </li>
                        <li class="recommendation-item">
                          <span class="recommendation-name">Espresso</span>
                          <button class="try-button">Try it</button>
                        </li>
                        <li class="recommendation-item">
                          <span class="recommendation-name">Flat White</span>
                          <button class="try-button">Try it</button>
                        </li>
                      </ul>
                    </div>
                  </div>
                {/if}
              </div>
              
              <div class="card">
                <h3 class="preferences-title">Dietary Preferences</h3>
                
                <div class="dietary-preferences">
                  <div class="preference-option">
                    <label class="checkbox-container">
                      <input type="checkbox" checked>
                      <span class="checkmark"></span>
                      <span>Low Sugar</span>
                    </label>
                  </div>
                  
                  <div class="preference-option">
                    <label class="checkbox-container">
                      <input type="checkbox">
                      <span class="checkmark"></span>
                      <span>Lactose Free</span>
                    </label>
                  </div>
                  
                  <div class="preference-option">
                    <label class="checkbox-container">
                      <input type="checkbox" checked>
                      <span class="checkmark"></span>
                      <span>Gluten Free</span>
                    </label>
                  </div>
                  
                  <div class="preference-option">
                    <label class="checkbox-container">
                      <input type="checkbox" checked>
                      <span class="checkmark"></span>
                      <span>Vegan Options</span>
                    </label>
                  </div>
                </div>
              </div>
            </section>
          {/if}
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
    
    .profile-container {
      width: 100%;
      max-width: 1200px;
      margin: 0 auto;
      padding: 30px;
      box-sizing: border-box;
      min-height: 100vh;
      position: relative;
      z-index: 2;
    }
    
    .profile-wrapper {
      display: flex;
      flex-direction: column;
      background-color: rgba(255, 255, 255, 0.95);
      border-radius: 20px;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }
    
    /* Header */
    .profile-header {
      display: flex;
      align-items: center;
      padding: 20px 30px;
      border-bottom: 1px solid #eee;
      background-color: white;
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
    
    .profile-header h1 {
      flex: 1;
      margin: 0;
      font-size: 24px;
      text-align: center;
    }
    
    .logout-button {
      display: flex;
      align-items: center;
      gap: 8px;
      background: none;
      border: none;
      color: #c87941;
      font-size: 16px;
      font-weight: 500;
      cursor: pointer;
      padding: 8px 12px;
      border-radius: 8px;
      transition: all 0.2s;
    }
    
    .logout-button:hover {
      background-color: rgba(200, 121, 65, 0.1);
    }
    
    /* Profile Content Layout */
    .profile-content {
      display: flex;
      padding: 30px;
      gap: 30px;
    }
    
    .profile-sidebar {
      flex: 1;
      max-width: 300px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
    
    .profile-main {
      flex: 3;
    }
    
    /* User Card */
    .user-card {
      background-color: #fff;
      border-radius: 15px;
      padding: 20px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }
    
    .user-avatar-container {
      position: relative;
      margin-bottom: 15px;
    }
    
    .user-avatar {
      width: 120px;
      height: 120px;
      border-radius: 50%;
      object-fit: cover;
      border: 4px solid white;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .edit-avatar-btn {
      position: absolute;
      bottom: 5px;
      right: 5px;
      background-color: #fff;
      border: none;
      width: 30px;
      height: 30px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
      cursor: pointer;
      transition: all 0.2s;
      color: #c87941;
    }
    
    .edit-avatar-btn:hover {
      transform: scale(1.1);
    }
    
    .user-info h2 {
      margin: 0 0 5px 0;
      font-size: 22px;
      color: #333;
    }
    
    .user-info p {
      margin: 0 0 10px 0;
      color: #666;
      font-size: 14px;
    }
    
    .loyalty-badge {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background-color: #c87941;
      color: white;
      padding: 5px 10px;
      border-radius: 20px;
      font-size: 14px;
      font-weight: 500;
    }
    
    /* Profile Navigation */
    .profile-nav {
      background-color: #fff;
      border-radius: 15px;
      overflow: hidden;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
      display: flex;
      flex-direction: column;
    }
    
    .nav-item {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 15px 20px;
      border: none;
      background: none;
      text-align: left;
      font-size: 16px;
      cursor: pointer;
      transition: all 0.2s;
      border-left: 3px solid transparent;
      color: #555;
    }
    
    .nav-item:hover {
      background-color: #f9f9f9;
    }
    
    .nav-item.active {
      background-color: rgba(200, 121, 65, 0.1);
      color: #c87941;
      border-left-color: #c87941;
    }
    
    .nav-item.active svg {
      color: #c87941;
    }
    
    /* Tab Content */
    .tab-content {
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
    
    .section-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }
    
    .section-header h2 {
      margin: 0;
      font-size: 20px;
      color: #333;
    }
    
    .edit-button, .add-button {
      display: flex;
      align-items: center;
      gap: 5px;
      background: none;
      border: none;
      color: #c87941;
      font-size: 14px;
      font-weight: 500;
      cursor: pointer;
      padding: 8px 12px;
      border-radius: 8px;
      transition: all 0.2s;
    }
    
    .edit-button:hover, .add-button:hover {
      background-color: rgba(200, 121, 65, 0.1);
    }
    
    .card {
      background-color: #fff;
      border-radius: 15px;
      padding: 20px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Info Grid */
    .info-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
      gap: 20px;
    }
    
    .info-item {
      display: flex;
      flex-direction: column;
      gap: 5px;
    }
    
    .info-label {
      font-size: 14px;
      color: #666;
    }
    
    .info-value {
      font-size: 16px;
      font-weight: 500;
      color: #333;
    }
    
    /* Edit Form */
    .edit-form {
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
    
    .form-group {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    
    .form-group label {
      font-size: 14px;
      color: #666;
    }
    
    .form-group input {
      padding: 12px 15px;
      border-radius: 10px;
      border: 1px solid #ddd;
      font-size: 16px;
      transition: all 0.2s;
    }
    
    .form-group input:focus {
      border-color: #c87941;
      outline: none;
      box-shadow: 0 0 0 2px rgba(200, 121, 65, 0.2);
    }
    
    .form-actions {
      display: flex;
      justify-content: flex-end;
      gap: 10px;
      margin-top: 10px;
    }
    
    .cancel-btn {
      padding: 10px 20px;
      border-radius: 10px;
      border: none;
      background-color: #f5f5f5;
      color: #333;
      font-size: 16px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s;
    }
    
    .cancel-btn:hover {
      background-color: #eee;
    }
    
    .save-btn {
      padding: 10px 20px;
      border-radius: 10px;
      border: none;
      background-color: #c87941;
      color: white;
      font-size: 16px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s;
    }
    
    .save-btn:hover {
      background-color: #a35e2c;
    }
    
    /* Toggle List */
    .toggle-list {
      display: flex;
      flex-direction: column;
      gap: 15px;
    }
    
    .toggle-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 0;
    }
    
    .toggle-info h3 {
      margin: 0 0 5px 0;
      font-size: 16px;
      color: #333;
    }
    
    .toggle-info p {
      margin: 0;
      font-size: 14px;
      color: #666;
    }
    
    /* Toggle Switch */
    .toggle-switch {
      position: relative;
      display: inline-block;
      width: 48px;
      height: 24px;
    }
    
    .toggle-switch input {
      opacity: 0;
      width: 0;
      height: 0;
    }
    
    .toggle-slider {
      position: absolute;
      cursor: pointer;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-color: #ddd;
      transition: .4s;
      border-radius: 24px;
    }
    
    .toggle-slider:before {
      position: absolute;
      content: "";
      height: 18px;
      width: 18px;
      left: 3px;
      bottom: 3px;
      background-color: white;
      transition: .4s;
      border-radius: 50%;
    }
    
    input:checked + .toggle-slider {
      background-color: #c87941;
    }
    
    input:checked + .toggle-slider:before {
      transform: translateX(24px);
    }
    
    /* Empty State */
    .empty-state {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background-color: #fff;
      border-radius: 15px;
      padding: 40px 20px;
      text-align: center;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .empty-state svg {
      color: #aaa;
      margin-bottom: 20px;
    }
    
    .empty-state h3 {
      margin: 0 0 10px 0;
      font-size: 20px;
      color: #333;
    }
    
    .empty-state p {
      margin: 0 0 20px 0;
      color: #666;
      font-size: 16px;
      max-width: 300px;
    }
    
    .action-button {
      background-color: #c87941;
      color: white;
      border: none;
      padding: 12px 24px;
      border-radius: 10px;
      font-size: 16px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.3s;
    }
    
    .action-button:hover {
      background-color: #a35e2c;
      transform: translateY(-2px);
    }
    
    /* Orders List */
    .orders-list {
      display: flex;
      flex-direction: column;
      gap: 15px;
    }
    
    .order-card {
      background-color: #fff;
      border-radius: 15px;
      padding: 20px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
      cursor: pointer;
      transition: all 0.2s;
    }
    
    .order-card:hover {
      transform: translateY(-3px);
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
    }
    
    .order-header {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      margin-bottom: 15px;
    }
    
    .order-id, .order-date {
      display: flex;
      flex-direction: column;
      gap: 5px;
    }
    
    .label {
      font-size: 12px;
      color: #666;
    }
    
    .value {
      font-size: 16px;
      font-weight: 500;
      color: #333;
    }
    
    .order-status {
      display: flex;
      justify-content: flex-end;
      align-items: center;
    }
    
    .status-badge {
      display: inline-block;
      padding: 5px 10px;
      border-radius: 15px;
      font-size: 12px;
      font-weight: 600;
    }
    
    .status-badge.delivered {
      background-color: #e6f7ee;
      color: #22c55e;
    }
    
    .status-badge.processing {
      background-color: #fef3c7;
      color: #f59e0b;
    }
    
    .status-badge.pending {
      background-color: #e0f2fe;
      color: #0284c7;
    }
    
    .order-items {
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-bottom: 15px;
      padding-bottom: 15px;
      border-bottom: 1px solid #eee;
    }
    
    .order-item {
      display: flex;
      justify-content: space-between;
      font-size: 14px;
      color: #333;
    }
    
    .order-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    
    .order-total {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    
    .order-total .value {
      font-size: 18px;
      font-weight: 600;
      color: #c87941;
    }
    
    .details-btn {
      display: flex;
      align-items: center;
      gap: 5px;
      background: none;
      border: none;
      color: #c87941;
      font-size: 14px;
      font-weight: 500;
      cursor: pointer;
    }
    
    /* Address List */
    .address-list {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 20px;
    }
    
    .address-card {
      background-color: #fff;
      border-radius: 15px;
      padding: 20px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
      position: relative;
      transition: all 0.2s;
    }
    
    .address-card:hover {
      transform: translateY(-3px);
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
    }
    
    .default-badge {
      position: absolute;
      top: 15px;
      right: 15px;
      background-color: #e6f7ee;
      color: #22c55e;
      padding: 4px 10px;
      border-radius: 15px;
      font-size: 12px;
      font-weight: 600;
    }
    
    .address-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 15px;
    }
    
    .address-header h3 {
      margin: 0;
      font-size: 18px;
      color: #333;
    }
    
    .address-actions {
      display: flex;
      gap: 10px;
    }
    
    .address-action-btn, .payment-action-btn {
      background: none;
      border: none;
      width: 30px;
      height: 30px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #555;
      cursor: pointer;
      transition: all 0.2s;
    }
    
    .address-action-btn:hover, .payment-action-btn:hover {
      background-color: #f5f5f5;
      color: #333;
    }
    
    .address-action-btn.delete, .payment-action-btn.delete {
      color: #e74c3c;
    }
    
    .address-action-btn.delete:hover, .payment-action-btn.delete:hover {
      background-color: #fdedeb;
    }
    
    .address-details {
      margin-bottom: 20px;
    }
    
    .address-details p {
      margin: 0 0 5px 0;
      color: #666;
      font-size: 14px;
    }
    
    .address-details .street {
      color: #333;
      font-weight: 500;
    }
    
    .set-default-btn {
      width: 100%;
      padding: 10px;
      background: none;
      border: 1px solid #c87941;
      border-radius: 10px;
      color: #c87941;
      font-size: 14px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s;
    }
    
    .set-default-btn:hover {
      background-color: rgba(200, 121, 65, 0.1);
    }
    
    /* Payment List */
    .payment-list {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 20px;
    }
    
    .payment-card {
      background-color: #fff;
      border-radius: 15px;
      padding: 20px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
      position: relative;
      transition: all 0.2s;
    }
    
    .payment-card:hover {
      transform: translateY(-3px);
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
    }
    
    .payment-header {
      display: flex;
      align-items: center;
      gap: 15px;
      margin-bottom: 20px;
    }
    
    .payment-icon {
      width: 40px;
      height: 40px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 5px;
      background-color: #f5f5f5;
    }
    
    .payment-info {
      flex: 1;
    }
    
    .payment-info h3 {
      margin: 0 0 5px 0;
      font-size: 16px;
      color: #333;
    }
    
    .payment-info p {
      margin: 0;
      font-size: 14px;
      color: #666;
    }
    
    /* Preferences */
    .preferences-title {
      margin: 0 0 20px 0;
      font-size: 18px;
      color: #333;
    }
    
    .empty-preference {
      text-align: center;
      padding: 20px 0;
    }
    
    .empty-preference p {
      margin: 0 0 15px 0;
      color: #666;
    }
    
    .preferences-chart {
      display: flex;
      flex-direction: column;
      gap: 30px;
    }
    
    .chart-container {
      padding: 10px 0;
    }
    
    .chart-bars {
      display: flex;
      flex-direction: column;
      gap: 15px;
    }
    
    .chart-bar-container {
      display: flex;
      align-items: center;
      gap: 15px;
    }
    
    .chart-label {
      min-width: 80px;
      font-size: 14px;
      font-weight: 500;
      color: #333;
    }
    
    .chart-bar {
      flex: 1;
      height: 20px;
      background-color: #f5f5f5;
      border-radius: 10px;
      overflow: hidden;
    }
    
    .chart-bar-fill {
      height: 100%;
      background-color: #c87941;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: flex-end;
      padding: 0 10px;
      box-sizing: border-box;
      transition: width 0.5s ease-in-out;
    }
    
    .chart-value {
      color: white;
      font-size: 12px;
      font-weight: 600;
    }
    
    .preferences-list h4 {
      margin: 0 0 15px 0;
      font-size: 16px;
      color: #333;
    }
    
    .recommendation-list {
      list-style: none;
      padding: 0;
      margin: 0;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    
    .recommendation-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 15px;
      background-color: #f9f9f9;
      border-radius: 10px;
    }
    
    .recommendation-name {
      font-weight: 500;
      color: #333;
    }
    
    .try-button {
      background-color: #c87941;
      color: white;
      border: none;
      padding: 5px 10px;
      border-radius: 5px;
      font-size: 14px;
      cursor: pointer;
      transition: all 0.2s;
    }
    
    .try-button:hover {
      background-color: #a35e2c;
    }
    
    /* Dietary Preferences */
    .dietary-preferences {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 15px;
    }
    
    .preference-option {
      display: flex;
      align-items: center;
    }
    
    /* Checkbox Container */
    .checkbox-container {
      display: flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      font-size: 16px;
      user-select: none;
    }
    
    .checkbox-container input {
      position: absolute;
      opacity: 0;
      cursor: pointer;
      height: 0;
      width: 0;
    }
    
    .checkmark {
      position: relative;
      height: 20px;
      width: 20px;
      background-color: #f5f5f5;
      border-radius: 4px;
      transition: all 0.2s;
    }
    
    .checkbox-container:hover input ~ .checkmark {
      background-color: #eee;
    }
    
    .checkbox-container input:checked ~ .checkmark {
      background-color: #c87941;
    }
    
    .checkmark:after {
      content: "";
      position: absolute;
      display: none;
    }
    
    .checkbox-container input:checked ~ .checkmark:after {
      display: block;
    }
    
    .checkbox-container .checkmark:after {
      left: 6px;
      top: 2px;
      width: 5px;
      height: 10px;
      border: solid white;
      border-width: 0 2px 2px 0;
      transform: rotate(45deg);
    }
    
    /* Responsive Design */
    @media (max-width: 992px) {
      .profile-content {
        flex-direction: column;
      }
      
      .profile-sidebar {
        max-width: none;
      }
      
      .user-card {
        flex-direction: row;
        text-align: left;
        align-items: flex-start;
        gap: 20px;
      }
      
      .profile-nav {
        flex-direction: row;
        flex-wrap: wrap;
      }
      
      .nav-item {
        flex: 1 0 auto;
        border-left: none;
        border-bottom: 3px solid transparent;
        justify-content: center;
      }
      
      .nav-item.active {
        border-left-color: transparent;
        border-bottom-color: #c87941;
      }
    }
    
    @media (max-width: 768px) {
      .profile-container {
        padding: 15px;
      }
      
      .profile-content {
        padding: 15px;
      }
      
      .user-card {
        flex-direction: column;
        text-align: center;
        align-items: center;
      }
      
      .order-header {
        grid-template-columns: 1fr;
        gap: 10px;
      }
      
      .order-status, .order-date {
        justify-content: flex-start;
      }
      
      .address-list, .payment-list {
        grid-template-columns: 1fr;
      }
      
      .dietary-preferences {
        grid-template-columns: 1fr;
      }
    }
  </style>