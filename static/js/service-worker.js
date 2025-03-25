self.addEventListener("install", (event) => {
  console.log("Service Worker installing...");
  event.waitUntil(
      caches.open("static-v1").then((cache) => {
          return cache.addAll([
              "/",  // Cache homepage
              "/static/css/tailwind.css",  // Cache CSS
              "/static/js/app.js",  // Cache main JS
              "/static/images/logo.png",  // Cache logo
          ]);
      })
  );
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
      caches.match(event.request).then((response) => {
          return response || fetch(event.request);
      })
  );
});

self.addEventListener("activate", (event) => {
  console.log("Service Worker activated...");
});
