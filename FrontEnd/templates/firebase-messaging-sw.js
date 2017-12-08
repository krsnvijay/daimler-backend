self.addEventListener('install', function (event) {
    event.waitUntil(
        caches.open('app').then(function (cache) {
            return cache.addAll(
        [
            //HTML
            '/',
            'index.html',
            'critical-list.html',
            'critical-list-detail.html',
            'critical-list-detailed-table.html',
            'notifications.html',
            'part-detail.html',
            'select.html',
            'sos-dashboard.html',
            'sos-messages.html',
            'sos-upload.html',
            'table.html',

         //CSS,IMAGES
          'resources/css/style.css',
          'resources/images/background.png',
          'resources/images/user.png',
          'resources/images/star2.png',
          'resources/images/filled_star.png',
        //JS
          'resources/js/index.js',
         'resources/js/navbar.js',
         'resources/js/notification.js',
         'resources/js/checktoken.js',
         'resources/js/config.js',
         'resources/js/critical-list.js',
         'resources/js/notifications.js',
         'resources/js/parts.js',
         'resources/js/parts-detail.js',
         'resources/js/sos-dashboard.js',
         'resources/js/sos-messages.js',
         'resources/js/sos-upload.js',
        //LIB/EXTERNAL DEPENDENCIES
//         'https://www.gstatic.com/firebasejs/4.6.2/firebase.js',
"https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js",
            'https://code.jquery.com/jquery-3.2.1.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js',
            'https://fonts.googleapis.com/icon?family=Material+Icons'

        ]
            );
        })
    );
});
self.addEventListener('activate', event => {
    event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request, {
            ignoreSearch: true
        }).then(response => {
            return fetch(event.request) || response;
        })
    );
});
