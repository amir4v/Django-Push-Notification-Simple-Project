self.addEventListener('push', function(event) {
    var data = event.data.json();
    var options = {
        body: data.body,
        icon: data.icon,
        data: {
            url: data.url
        }
    };
    event.waitUntil(
        self.registration.showNotification(data.title, options)
    );
});