# Fingerprint API

Expose your browser fingerprint by making a GET request. This shows all information made available by the [Fingerprint.js](https://github.com/fingerprintjs/fingerprintjs) library.
This is done by going to the root of the site, which allows the Javascript to run on your browser. After that you're redirected to the `/results/{id}` page which shows your
fingerprint in JSON form.

## Development

Use docker-compose to get a dev stack running:
```
docker-compose up -d
```
