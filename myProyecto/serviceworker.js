var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/core/css/estilo.css',
    '/galeria/',
    '/login/',
    '/quienes_somos/',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(

    fetch(event.request)
    .then((result)=>{
      return caches.open(CACHE_NAME)
      .then(function(c) {
        c.put(event.request.url, result.clone())
        return result;
      })
      
    })
    .catch(function(e){
        return caches.match(event.request)
    })


   
  );
});


//codigo para notificaciones push
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var firebaseConfig = {
  apiKey: "AIzaSyAN57s1katQ0g2qsgzsBZkrs3cu7V6ZRCI",
  authDomain: "floreriapetalos-8f372.firebaseapp.com",
  databaseURL: "https://floreriapetalos-8f372.firebaseio.com",
  projectId: "floreriapetalos-8f372",
  storageBucket: "floreriapetalos-8f372.appspot.com",
  messagingSenderId: "1054508423292",
  appId: "1:1054508423292:web:de3870d695b5d1e25f51f9"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

let messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function (payload) {

  let title = 'titulo de la notificacion';

  let options = {
    body: 'este es el mensaje',
    icon: '/static/core/img/logo.png'
  }

  self.registration.showNotification(title, options);

});


