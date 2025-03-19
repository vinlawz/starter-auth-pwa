self.addEventListener("install", (event) => {
    console.log("✅ Service Worker installed");
    event.waitUntil(
        caches.open("static-cache").then((cache) => {
            return cache.addAll([
                "/",
                "/static/css/output.css",
                "/static/css/public/custom.css",
                "/static/branding/1.png",
            ]);
        })
    );
});

self.addEventListener("activate", (event) => {
    console.log("✅ Service Worker activated");
});

self.addEventListener("fetch", (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            return response || fetch(event.request);
        })
    );
});
