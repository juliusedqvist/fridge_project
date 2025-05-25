<template>
  <div class="layout-container">
    <div class="content-wrapper">
      <NuxtPage />
    </div>
  </div>
</template>

<style>
html,
body {
  margin: 0;
  padding: 0;
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
  /* Ensures content stretches full height */
  padding: 1rem;
  box-sizing: border-box;
}

.content-wrapper {
  background: white;
  width: 100%;
  max-width: 900px;
  height: 100%;
  /* <-- Forces full stretch */
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
  border-radius: 12px;
  overflow-y: auto;
  padding: 1rem 1.5rem;
  /* <-- Reduced padding */
  box-sizing: border-box;
}

/* Mobile styles */
@media (max-width: 768px) {
  .layout-container {
    padding: 0.5rem;
  }

  .content-wrapper {
    max-width: 100%;
    border-radius: 6px;
    padding: 0.75rem 1rem;
    height: 100%;
    /* Keep full height on mobile */
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  }
}
</style>
