<script>
  import { goto } from '$app/navigation';
  
  let isTransitioning = false;
  let transitionType = '';
  let buttonRect = null;
  let transitionOriginX = 0;
  let transitionOriginY = 0;
  let isButtonZooming = false;
  let buttonRef;
  
  function handleGetStarted() {
    isTransitioning = true;
    transitionType = 'get-started';

    setTimeout(() => {
      goto('/get_started');
    }, 1000);
  }
  
  function handleGoToMenu(event) {
    const rect = event.currentTarget.getBoundingClientRect();
    buttonRect = rect;
    transitionOriginX = rect.left + rect.width / 2;
    transitionOriginY = rect.top + rect.height / 2;
    
    isTransitioning = true;
    transitionType = 'menu';
    isButtonZooming = true;

    event.currentTarget.classList.add('menu-btn-expanding');

    setTimeout(() => {
      goto('/menu?from=home', { replaceState: false });
    }, 600);
  }
</script>
  
  <svelte:head>
    <title>Coffee Shop - Bienvenue</title>
    <meta name="description" content="Découvrez notre café d'exception" />
  </svelte:head>
  
  {#if isTransitioning}
    <div 
      class="page-transition {transitionType}" 
      style={transitionType === 'menu' ? 
        `--origin-x: ${transitionOriginX}px; --origin-y: ${transitionOriginY}px;` : 
        ''}
    ></div>
  {/if}
  
  <main class="welcome-screen {isTransitioning ? 'fade-out' : ''}">
    <div class="video-background">
      <video autoplay muted loop playsinline>
        <source src="/videos/coffee_vid.mp4" type="video/mp4">
      </video>
    </div>
    <div class="coffee-content">
      <div class="desktop-layout">
        
        <div class="coffee-text-side">
          <div class="coffee-text">
            <h1>Coffee so good, your taste buds will love it.</h1>
            <p>The best grain, the finest roast, the powerful flavor.</p>
          </div>
          
          <div class="button-container">
            <button class="get-started-btn" on:click={handleGetStarted}>
              Get Started
            </button>
            
            <button class="menu-btn" on:click={handleGoToMenu}>
              Voir le Menu
            </button>
          </div>
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
      color: #fff;
      height: 100vh;
      overflow: hidden;
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
    
    .video-background::after {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: radial-gradient(ellipse at center, rgba(0,0,0,0) 0%, rgba(0,0,0,0) 60%, rgba(0,0,0,0.8) 100%);
      pointer-events: none;
      z-index: 2;
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
    }
    
    .welcome-screen {
      height: 100vh;
      width: 100vw;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background-color: #000;
      position: relative;
      overflow: hidden;
    }
    
    .coffee-content {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100%;
      width: 100%;
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 40px;
      box-sizing: border-box;
      position: relative;
      z-index: 2;
    }
    
    .desktop-layout {
      display: flex;
      flex-direction: row;
      width: 100%;
      height: 100%;
      align-items: center;
    }
    
    .coffee-image-side {
      flex: 1;
      position: relative;
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    
    .coffee-text-side {
      flex: 1;
      padding-left: 0;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
    }

    .coffee-beans-bg {
      position: absolute;
      top: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 100%;
      height: 100%;
      background-image: url('/images/coffee-beans.png');
      background-size: cover;
      background-position: center;
      opacity: 1;
    }

    
    
    @keyframes steam {
      0% {
        opacity: 0.3;
        transform: translateX(-50%) translateY(0px) scale(1);
      }
      50% {
        opacity: 0.6;
        transform: translateX(-50%) translateY(-25px) scale(1.3);
      }
      100% {
        opacity: 0.3;
        transform: translateX(-50%) translateY(-50px) scale(0.8);
      }
    }
    
    .coffee-text {
      margin-bottom: 40px;
      max-width: 500px;
      color: #ffffff;
      text-align: center;
    }
    
    h1 {
      font-size: 3.5rem;
      font-weight: 700;
      margin-bottom: 20px;
      line-height: 1.2;
      text-align: center;
    }
    
    p {
      font-size: 1.2rem;
      font-weight: 400;
      color: rgba(255, 255, 255, 0.8);
      margin-bottom: 40px;
      line-height: 1.6;
      text-align: center;
    }
    
    .button-container {
      display: flex;
      gap: 20px;
      margin: 0 auto;
    }
    
    .get-started-btn, .menu-btn {
      background-color: #c87941;
      color: white;
      border: none;
      padding: 18px 40px;
      border-radius: 8px;
      font-size: 1.2rem;
      font-weight: 600;
      cursor: pointer;
      transition: background-color 0.3s, transform 0.2s;
      width: auto;
      display: flex;
      justify-content: center;
      align-items: center;
      min-width: 180px;
    }
    
    .menu-btn {
      background-color: transparent;
      border: 2px solid #c87941;
    }
    
    .get-started-btn:hover, .menu-btn:hover {
      background-color: #a35e2c;
      transform: translateY(-3px);
      box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
    }
    
    .menu-btn:hover {
      background-color: rgba(163, 94, 44, 0.3);
    }
    
    .get-started-btn:active, .menu-btn:active {
      transform: translateY(-1px);
    }

    @media (max-width: 992px) {
      .desktop-layout {
        flex-direction: column;
      }
      
      .coffee-image-side {
        height: 40vh;
        width: 100%;
        margin-bottom: 30px;
      }
      
      .coffee-text-side {
        padding-left: 0;
        align-items: center;
        text-align: center;
      }
      
      h1 {
        font-size: 2.8rem;
      }
      
      .coffee-cup {
        width: 150px;
        height: 150px;
      }
    }
    
    @media (max-width: 576px) {
      h1 {
        font-size: 2.2rem;
      }
      
      p {
        font-size: 1rem;
      }
      
      .coffee-content {
        padding: 0 20px;
      }
      
      .coffee-cup {
        width: 120px;
        height: 120px;
      }
      
      .get-started-btn {
        padding: 16px 32px;
        font-size: 1rem;
      }
    }

    .page-transition {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background-color: #c87941;
      transform-origin: var(--origin-x, 50%) var(--origin-y, 50%);
      clip-path: circle(0% at var(--origin-x, 50%) var(--origin-y, 50%));
      animation: page-expand 0.6s cubic-bezier(0.165, 0.84, 0.44, 1) forwards;
      z-index: 999;
    }
    
    .page-transition.get-started {
      background-color: #000;
      animation: transition-in 1s ease-in-out forwards;
    }
    
    .page-transition.menu {
      background-color: #c87941;
      clip-path: circle(0% at var(--origin-x) var(--origin-y));
      animation: menu-circle-expand 0.5s cubic-bezier(0.645, 0.045, 0.355, 1.000) forwards;
    }
    
    @keyframes menu-circle-expand {
      0% {
        clip-path: circle(0% at var(--origin-x) var(--origin-y));
      }
      100% {
        clip-path: circle(150% at var(--origin-x) var(--origin-y));
      }
    }
    
    .menu-btn-expanding {
      animation: button-zoom 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
      z-index: 10000;
      position: relative;
    }
    
    @keyframes button-zoom {
      0% {
        transform: scale(1);
        opacity: 1;
      }
      40% {
        transform: scale(1.8);
        opacity: 1;
      }
      100% {
        transform: scale(25);
        opacity: 0;
      }
    }
    
    @keyframes transition-in {
      0% {
        opacity: 0;
        transform: scale(0.95);
      }
      100% {
        opacity: 1;
        transform: scale(1);
      }
    }
    
    .fade-out {
      animation: fade-out 1s ease-in-out forwards;
    }
    
    @keyframes fade-out {
      0% {
        opacity: 1;
      }
      100% {
        opacity: 0;
      }
    }
    
    .menu-button.zooming::after {
      content: '';
      position: absolute;
      inset: 0;
      background-color: #c87941;
      border-radius: inherit;
      z-index: -1;
      transform-origin: center;
      animation: circle-expand 0.4s cubic-bezier(0.165, 0.84, 0.44, 1) forwards;
    }
    
    @keyframes circle-expand {
      0% {
        transform: scale(1);
        opacity: 1;
      }
      100% {
        transform: scale(25);
        opacity: 1;
      }
    }
    
    .menu-button.zooming {
      animation: button-zoom 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
      position: relative;
      z-index: 1000;
    }
    
    @keyframes button-zoom {
      0% {
        transform: scale(1);
      }
      30% {
        transform: scale(1.1);
      }
      100% {
        transform: scale(0.8);
      }
    }
  </style>