<template>
  <div class="layout-container">
    <div class="parallax-side"></div>
    <div class="main-content">
      <NuxtPage />
    </div>
  </div>
</template>

<style scoped>
.layout-container {
  display: flex;
  height: 100vh;
  overflow: hidden;
}

/* Parallax Side */
.parallax-side {
  width: 35%;
  background-image: url('/Images/DSC01042.jpg');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  /* Parallax effect */
}

/* Main Content */
.main-content {
  flex: 1;
  background: white;
  overflow-y: auto;
  padding: 2rem;
}
</style>
