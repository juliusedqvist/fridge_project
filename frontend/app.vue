<template>
  <div class="layout-container">
    <div class="content-wrapper">
      <NuxtPage />
    </div>
  </div>
</template>

<style scoped>
html,
body {
  margin: 0;
  height: 100%;
  background-color: black;
  /* fallback */
}

.layout-container {
  min-height: 100vh;
  width: 100vw;
  background-image: url('/Images/DSC01042.jpg');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;

  display: flex;
  justify-content: center;
  align-items: stretch;
  padding: 0;
  /* no padding */
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
    padding: 1rem 1.5rem;
    border-radius: 4px;
  }

  .layout-container {
    padding: 0;
    /* remove mobile padding */
  }
}
</style>
