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
  align-items: flex-start;
  padding: 2rem;
}

/* Content wrapper - mobile: white background, full height */
.content-wrapper {
  width: 100%;
  max-width: 800px;
  padding: 2rem;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  border-radius: 8px;

  /* On desktop, no background, no height restriction */
  background: transparent;
  min-height: auto;
  box-shadow: none;
  border-radius: 0;
}

/* Mobile styles */
@media (max-width: 768px) {
  .content-wrapper {
    background: white;
    min-height: 100vh;
    /* full viewport height */
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
  }
}
</style>
