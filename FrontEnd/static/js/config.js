var config = {
    apiKey: "AIzaSyB9t-wtDoOVgJpYS4Z0lCYHt-twsLBCVtk",
    authDomain: "daimler-notify.firebaseapp.com",
    databaseURL: "https://daimler-notify.firebaseio.com",
    projectId: "daimler-notify",
    storageBucket: "daimler-notify.appspot.com",
    messagingSenderId: "423946699965"
};


firebase.initializeApp(config);


if ('serviceWorker' in navigator) {
	window.addEventListener('load', function() {
		navigator.serviceWorker.register('../../service-worker.js').then(function(registration) {
			console.log('ServiceWorker registration successful with scope: ', registration.scope);
		}, function(err) {
			console.log('ServiceWorker registration failed: ', err);
		});
	});
}


// function sendRegisToken(){
	const messaging = firebase.messaging();

// }

messaging.requestPermission()
.then(function() {
  console.log('Notification permission granted.');
  // TODO(developer): Retrieve an Instance ID token for use with FCM.
  // ...
})
.catch(function(err) {
  console.log('Unable to get permission to notify.', err);
});