Simple HTTP server
==================

A Basic HTTP server to play around with sockets and HTTP in python.

## Done

  * Handles basic HTTP GET requests and responses (200 or 404)
  * Configuration file for port and hostname


## TODO

  * Handle HEAD HTTP requests
  * Handle favicon and keep-alive requests
  * Currently we read the file for each request, use checksum?
  * Currently read size is limited to 4096
  * Multi-threading for multiple clients support
  * Improve the client to support things like redirections, HTTPS, ...
  
  
## Authors

  * Aurelien Legrand