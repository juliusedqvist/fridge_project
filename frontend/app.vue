<template>
  <div class="layout-container">
    <div class="parallax-side left"></div>
    <div class="main-content">
      <NuxtPage />
    </div>
    <div class="parallax-side right"></div>
  </div>
</template>

<style scoped>
.layout-container {
  display: flex;
  height: 100vh;
  overflow: hidden;
}

/* Parallax sides */
.parallax-side {
  width: 25%;
  background-image: url('/Images/DSC01042.jpg');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

/* If you want to mirror the right side image */
.parallax-side.right {
  transform: scaleX(-1);
}

/* Main content in the center */
.main-content {
  flex: 1;
  background: white;
  overflow-y: auto;
  padding: 2rem;
}
</style>
