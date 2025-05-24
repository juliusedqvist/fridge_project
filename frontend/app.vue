<template>
  <div class="layout-container">
    <div class="content-wrapper">
      <NuxtPage />
    </div>
  </div>
</template>

<style scoped>
.layout-container {
  /* Full viewport height */
  min-height: 100vh;

  /* Full width and fixed background image */
  background-image: url('/Images/DSC01042.jpg');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;

  /* Center content horizontally and vertically */
  display: flex;
  justify-content: center;
  align-items: flex-start;
  /* or center if you want vertically centered */

  padding: 2rem;
  /* spacing from edges */
}

/* White box in the center */
.content-wrapper {
  background: white;
  max-width: 800px;
  /* or whatever width you want */
  width: 100%;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  padding: 2rem;
  border-radius: 8px;
}
</style>
