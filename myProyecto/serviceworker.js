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


importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var firebaseConfig = {
  apiKey: "AIzaSyDUssE0m_zkQ8RbMyeQAjRPaZkfXIpG8K8",
  authDomain: "floreriapetalos-9d3f1.firebaseapp.com",
  databaseURL: "https://floreriapetalos-9d3f1.firebaseio.com",
  projectId: "floreriapetalos-9d3f1",
  storageBucket: "floreriapetalos-9d3f1.appspot.com",
  messagingSenderId: "836835881577",
  appId: "1:836835881577:web:9e82a61ccb524a1c8128f8"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

let messaging = firebase.messaging(); 

messaging.setBackgroundMessageHandler(function(payload){
  
  let title = 'Titulo de la notificacion';

  let options = {
    body:'este es el mensaje',
    icon:'/static/core/img/logo.png'
  }

  self.registration.showNotification(title, options); 

});


