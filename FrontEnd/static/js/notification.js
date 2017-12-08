const applicationServerPublicKey = 'BJZy3aVYrxbEKeEEqRReRPs_239ZUxj5LCm_E-LRiMrz47IA51VmCyC8A4XpvuaoY5hjYhJ8TT5eA5dEq7F0BZ8';
let isSubscribed = false;
let swRegistration = null;
let fcm_token = null;

var token = sessionStorage.tokenid;

var config = {
    apiKey: "AIzaSyB9t-wtDoOVgJpYS4Z0lCYHt-twsLBCVtk",
    authDomain: "daimler-notify.firebaseapp.com",
    databaseURL: "https://daimler-notify.firebaseio.com",
    projectId: "daimler-notify",
    storageBucket: "daimler-notify.appspot.com",
    messagingSenderId: "423946699965"
};


firebase.initializeApp(config);

const messaging = firebase.messaging();

function urlB64ToUint8Array(base64String) {
    const padding = '='.repeat((4 - base64String.length % 4) % 4);
    const base64 = (base64String + padding)
        .replace(/\-/g, '+')
        .replace(/_/g, '/');


    const rawData = window.atob(base64);
    const outputArray = new Uint8Array(rawData.length);

    for (let i = 0; i < rawData.length; ++i) {
        outputArray[i] = rawData.charCodeAt(i);
    }
    return outputArray;
}

function subscribeUser() {
    const applicationServerKey = urlB64ToUint8Array(applicationServerPublicKey);
    swRegistration.pushManager.subscribe({
            userVisibleOnly: true,
            applicationServerKey: applicationServerKey
        })
        .then(function (subscription) {
            console.log('User is subscribed.');
            console.log(subscription);

            //            updateSubscriptionOnServer(subscription);

            isSubscribed = true;

        })
        .catch(function (err) {
            console.log('Failed to subscribe the user: ', err);
        });
}

function unsubscribeUser() {
    swRegistration.pushManager.getSubscription()
        .then(function (subscription) {
            if (subscription) {
                return subscription.unsubscribe();
            }
        })
        .catch(function (error) {
            console.log('Error unsubscribing', error);
        })
        .then(function () {
            //    updateSubscriptionOnServer(null);

            console.log('User is unsubscribed.');
            isSubscribed = false;

        });
}

function initializeNotifications() {

    // Set the initial subscription value
    swRegistration.pushManager.getSubscription()
        .then(function (subscription) {
            isSubscribed = !(subscription === null);

            //    updateSubscriptionOnServer(subscription);

            if (isSubscribed) {
                console.log('User IS subscribed.');
            } else {
                console.log('User is NOT subscribed.');
            }
        });
}


function requestPermission(){
    messaging.requestPermission()
    .then(function() {
        console.log('Notification permission granted.');
        sendFCMToken();
    })
    .catch(function(err) {
        console.log('Unable to get permission to notify.', err);
    });
}

function getFCMToken(onsuccess){
    messaging.getToken().then((res)=>{
        onsuccess(res);
    });
}

function sendFCMToken(){
    const getEndpoint = "https://daimler-backend.herokuapp.com/api/current_user/";
    const postEndpoint = "https://daimler-backend.herokuapp.com/api/device/gcm/";
    let payload = {};

    fetch(getEndpoint, {
        method: "get",
        headers: {
            // 'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Token ' + token
        }
    }).then((res)=>{
        if (res.ok) {
            res.json().then(function (data) {
                // payload.userID = data.id;
                // payload.username = data.username;
                console.log("Getting FCM token...");
                getFCMToken((FCM_token)=>{
                    // payload.registration_id = FCM_token;

                    var formData = new FormData();
                    formData.append('registration_id', FCM_token);
                    formData.append('userID', data.id);
                    formData.append('name', data.username);
                    formData.append('active', true);
                    formData.append('cloud_message_type', 'FCM');

                    var xhr = new XMLHttpRequest();
                    xhr.open('POST', postEndpoint, true);
                    console.log(token);
                    xhr.setRequestHeader('Authorization', 'Token ' + token);
                    xhr.onload = function () {
                        console.log(xhr);
                    };
                    xhr.send(formData);
                })
            });
        } else {
            console.log('Network request failed with res ' + res.status + ': ' + res.statusText);
        }
    });
}



if ('serviceWorker' in navigator && 'PushManager' in window) {
    console.log('Service Worker and Push is supported');

    window.addEventListener('load', function() {
        navigator.serviceWorker.register('firebase-messaging-sw.js')
        .then(function (swReg) {
            console.log('Service Worker is registered', swReg);

            swRegistration = swReg;
            subscribeUser();
            initializeNotifications();
            requestPermission();
        })
        .catch(function (error) {
            console.error('Service Worker Error', error);
        });
    });
} else {
    console.warn('Push messaging is not supported');
    pushButton.textContent = 'Push Not Supported';
}
//PUB:BJZy3aVYrxbEKeEEqRReRPs_239ZUxj5LCm_E-LRiMrz47IA51VmCyC8A4XpvuaoY5hjYhJ8TT5eA5dEq7F0BZ8
//PRIV:5tOi9dKR77pqY0uQ5H2PqQbR6YMG1c75A2XgR7izOcA


if(location.protocol == "http:" && location.href.split(":")[1] != "//localhost"){
    location.protocol = "https:";
}


