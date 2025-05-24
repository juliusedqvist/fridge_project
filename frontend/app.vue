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

  /* background image for desktop */
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

/* White content box */
.content-wrapper {
  background: white;
  width: 100%;
  max-width: 900px;
  /* controls how wide the white content is on desktop */
  min-height: 100vh;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  overflow-y: auto;
  padding: 2rem;
}

/* Mobile styles: white background full width, hide background image sides */
@media (max-width: 768px) {
  .layout-container {
    background: none;
    /* remove background image */
  }

  .content-wrapper {
    max-width: 100%;
    border-radius: 0;
    padding: 1.5rem;
  }
}
</style>
