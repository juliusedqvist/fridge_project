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
  align-items: center;
  /* center vertically too */
  padding: 2rem;
  /* background visible on desktop */
  box-sizing: border-box;
}

.content-wrapper {
  background: white;
  width: 100%;
  max-width: 900px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
  border-radius: 12px;
  overflow-y: auto;
  padding: 2rem;
  box-sizing: border-box;
  min-height: 100%;
}

/* Mobile styles */
@media (max-width: 768px) {
  .layout-container {
    padding: 0.5rem;
    /* less background visible on mobile */
  }

  .content-wrapper {
    max-width: 100%;
    border-radius: 6px;
    padding: 1rem;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
    min-height: 100vh;
    /* ensure full height on mobile too */
  }
}
</style>
