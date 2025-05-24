<template>
  <div class="layout-container">
    <div class="content-wrapper">
      <NuxtPage />
    </div>
  </div>
</template>

<style scoped>
.layout-container {
  min-height: 100vh;
  background-image: url('/Images/DSC01042.jpg');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;

  display: flex;
  justify-content: center;
  align-items: stretch;
  /* full height */
  padding: 2rem;
}

.content-wrapper {
  background: white;
  width: 100%;
  max-width: 900px;
  min-height: 100vh;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  overflow-y: auto;
  padding: 2rem;
}

/* Mobile styles */
@media (max-width: 768px) {
  .content-wrapper {
    max-width: 95%;
    /* allow it to almost fill the screen */
    padding: 1rem 1.5rem;
    /* less padding horizontally */
    border-radius: 4px;
    /* smaller radius or remove */
  }

  .layout-container {
    padding: 1rem;
    /* reduce overall padding on mobile */
  }
}
</style>
