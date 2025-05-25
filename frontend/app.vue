<template>
  <div class="layout-container">
    <div class="content-wrapper">
      <div class="content-inner">
        <div class="content-wrapper2">
          <NuxtPage />
        </div>
      </div>
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
  padding: 2rem;
  box-sizing: border-box;
}

.content-wrapper {
  background: white;
  width: 100%;
  max-width: 900px;
  height: 100%;
  /* Shadow and border-radius here */
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
  border-radius: 12px;
  overflow-y: auto;
  box-sizing: border-box;
  /* Removed padding from here */
}

.content-wrapper2 {
  max-width: 900px;
  margin: 0 auto;
  padding: 1rem;
  box-sizing: border-box;
  overflow-x: hidden;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.content-inner {
  padding: 1rem 0.5rem;
  height: 100%;
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
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
    height: 100%;
    /* no padding here */
  }

  .content-inner {
    padding: 1rem 0.5rem;
    height: 100%;
    box-sizing: border-box;
  }
}
</style>
