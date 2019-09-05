# Simple-Server-10000-Request-Problem

## Benchmarking Tools
#### ApacheBench

### Tools Installation
#### Linux Installation
    sudo apt-get install apache2-tools

### How to run test
    ab -n number_of_request -c number_of_concurrent http://yourserver

## Testing Apache Web Server

Using Ubuntu 18.04

### Configuration
Move file to /var/www/html

    sudo cp resource/test20kb.html
    sudo cp resource/test500bytes.html

Raise the opened file limit

    sudo cp resource/limit.conf /etc/security/

### Result
Commmand

    ab -n 10000 -c 10000 http://127.0.0.1/test20kb.html


    

## Event-Based Web Server

### Low Level Server

#### Installation

#### Result

### High Level Server

#### Installation

#### Result



