<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  
  let pageLoaded = false;
  
  onMount(() => {
    setTimeout(() => {
      pageLoaded = true;
    }, 100);
  });

  function handleMenuClick() {
    document.body.style.overflow = 'auto';
    goto('/menu');
  }
</script>

<svelte:head>
  <title>Coffee Shop - Get Started</title>
  <meta name="description" content="Commencez votre aventure de café" />
</svelte:head>

<main class="get-started-container {pageLoaded ? 'fade-in' : ''}">
  <div class="video-background">
    <video autoplay muted loop playsinline>
      <source src="/videos/beans_drop.mp4" type="video/mp4">
    </video>
  </div>
  <div class="content-wrapper">
    <h1 class="animate-item">Bienvenue dans notre aventure café</h1>
    
    <div class="content-section animate-item">
      <h2>Découvrez nos variétés de café</h2>
      <p>
        Nous offrons une sélection de cafés premium provenant des meilleurs producteurs du monde entier.
        Chaque grain est soigneusement sélectionné et torréfié pour vous offrir une expérience incomparable.
      </p>
    </div>
    
    <div class="content-section animate-item">
      <h2>Comment commencer</h2>
      <ol>
        <li>Choisissez votre café préféré</li>
        <li>Sélectionnez votre méthode de préparation</li>
        <li>Profitez d'une tasse parfaite à chaque fois</li>
      </ol>
    </div>
    
    <div class="buttons-container animate-item">
      <a href="/" class="btn menu-btn">Retour à l'accueil</a>
      <a href="/menu" class="btn menu-btn" on:click={handleMenuClick}>Voir le menu</a>
    </div>
  </div>
</main>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
      Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    background-color: #121212;
    color: #fff;
    height: 100vh;
    overflow: hidden;
    width: 100vw;
    max-width: 100%;
    box-sizing: border-box;
  }
  
  .get-started-container {
    position: relative;
    width: 100%;
    height: 100vh;
    overflow: hidden;
    max-width: 100vw;
    box-sizing: border-box;
  }
  
  .content-wrapper {
    position: relative;
    max-width: 800px;
    margin: 0 auto;
    padding: 0px 20px;
    opacity: 0;
    z-index: 3;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    overflow: hidden;
    box-sizing: border-box;
  }
  
  .fade-in .content-wrapper {
    animation: fade-in 1.2s ease-out forwards;
  }
  
  @keyframes fade-in {
    0% {
      opacity: 0;
      transform: translateY(20px);
    }
    100% {
      opacity: 1;
      transform: translateY(0);
    }
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
  
  .video-background::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(to bottom, rgba(18,18,18,0.7) 0%, rgba(18,18,18,0.5) 100%);
    pointer-events: none;
    z-index: 2;
  }
  
  .fade-in.get-started-container .video-background::after {
    animation: darken-bg 1.5s ease-out forwards;
  }
  
  @keyframes darken-bg {
    0% {
      background: linear-gradient(to bottom, rgba(18,18,18,0.7) 0%, rgba(18,18,18,0.5) 100%);
    }
    100% {
      background: linear-gradient(to bottom, rgba(18,18,18,0.8) 0%, rgba(18,18,18,0.7) 100%);
    }
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
  
  .animate-item {
    opacity: 0;
    transform: translateY(30px);
  }
  
  .fade-in .animate-item {
    animation: item-fade-in 0.8s ease-out forwards;
  }
  
  .fade-in .animate-item:nth-child(1) {
    animation-delay: 0.3s;
  }
  
  .fade-in .animate-item:nth-child(2) {
    animation-delay: 0.6s;
  }
  
  .fade-in .animate-item:nth-child(3) {
    animation-delay: 0.9s;
  }
  
  .fade-in .animate-item:nth-child(4) {
    animation-delay: 1.2s;
  }
  
  @keyframes item-fade-in {
    0% {
      opacity: 0;
      transform: translateY(30px);
    }
    100% {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  h1 {
    font-size: 2.2rem;
    margin-bottom: 20px;
    text-align: center;
    color: #c87941;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
  }
  
  .content-section {
    background-color: rgba(200, 121, 65, 0.1);
    border-radius: 8px;
    padding: 15px 20px;
    margin-bottom: 15px;
    backdrop-filter: blur(5px);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    transition: background-color 0.5s ease, box-shadow 0.5s ease;
  }
  
  .fade-in .content-section {
    background-color: rgba(200, 121, 65, 0.3);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
  }
  
  h2 {
    color: #c87941;
    font-size: 1.6rem;
    margin-top: 0;
    margin-bottom: 10px;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
  }
  
  p, ol {
    font-size: 1rem;
    line-height: 1.5;
    color: rgba(255, 255, 255, 0.9);
    font-weight: 400;
  }
  
  .fade-in p, .fade-in ol {
    color: rgba(255, 255, 255, 1);
    text-shadow: 0 1px 1px rgba(0, 0, 0, 0.2);
  }
  
  ol {
    padding-left: 20px;
    margin: 10px 0;
  }
  
  li {
    margin-bottom: 5px;
  }
  
  .buttons-container {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 15px;
  }
  
  .btn {
    display: inline-block;
    background-color: #c87941;
    color: white;
    border: none;
    padding: 15px 30px;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    text-decoration: none;
    transition: background-color 0.3s, transform 0.2s;
  }
  
  .back-btn {
    background-color: rgba(200, 121, 65, 0.8);
  }
  
  .menu-btn {
    background-color: #c87941;
  }
  
  .btn:hover {
    background-color: #a35e2c;
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  }
  
  .btn:active {
    transform: translateY(-1px);
  }
  
  @media (max-width: 576px) {
    h1 {
      font-size: 2rem;
    }
    
    h2 {
      font-size: 1.5rem;
    }
    
    p, ol {
      font-size: 1rem;
    }
    
    .content-section {
      padding: 20px;
    }
  }
</style> 