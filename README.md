# Simple-Server-10000-Request-Problem

## Team Member

Thareq Muhammad Yusuf Hasnul Aziz - 13516004
Wildan Dicky Alnatara - 13516012
Adylan Roaffa Ilmy - 13516016
Putu Gery Wahyu Nugraha - 13516100

## Benchmarking Tools
#### ApacheBench

### Tools Installation
#### Linux Installation
    sudo apt-get install apache2-tools

### How to run test
    ab -n number_of_request -c number_of_concurrent http://yourserver

## Testing Apache Web Server

Using Ubuntu 18.04 and Apache/2.4.29 (Ubuntu)

### Configuration
Move file to /var/www/html

    sudo cp resource/test20kb.html
    sudo cp resource/test500bytes.html

Raise the opened file limit

    sudo cp resource/limits.conf /etc/security/
    ulimit -n 20000

### Result
Command for 20kb html files

    ab -n 10000 -c 10000 http://127.0.0.1/test20kb.html

Benchmark Result

    This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/

    Benchmarking 127.0.0.1 (be patient)
    Completed 1000 requests
    Completed 2000 requests
    Completed 3000 requests
    Completed 4000 requests
    Completed 5000 requests
    Completed 6000 requests
    Completed 7000 requests
    Completed 8000 requests
    Completed 9000 requests
    Completed 10000 requests
    Finished 10000 requests


    Server Software:        Apache/2.4.29
    Server Hostname:        127.0.0.1
    Server Port:            80

    Document Path:          /test20kb.html
    Document Length:        20386 bytes

    Concurrency Level:      10000
    Time taken for tests:   47.800 seconds
    Complete requests:      10000
    Failed requests:        268
    (Connect: 0, Receive: 0, Length: 268, Exceptions: 0)
    Total transferred:      201063120 bytes
    HTML transferred:       198396552 bytes
    Requests per second:    209.21 [#/sec] (mean)
    Time per request:       47799.712 [ms] (mean)
    Time per request:       4.780 [ms] (mean, across all concurrent requests)
    Transfer rate:          4107.78 [Kbytes/sec] received

    Connection Times (ms)
                min  mean[+/-sd] median   max
    Connect:        0   90 280.1      0    1044
    Processing:     2 2457 7613.2     13   47681
    Waiting:        0 1520 5135.0     12   27518
    Total:         10 2548 7777.5     13   47681

    Percentage of the requests served within a certain time (ms)
    50%     13
    66%     14
    75%     14
    80%     15
    90%  14392
    95%  15391
    98%  28506
    99%  43346
    100%  47681 (longest request)

Command for 500bytes html files

    ab -n 10000 -c 10000 http://127.0.0.1/test500bytes.html

Benchmark Result

    This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/

    Benchmarking 127.0.0.1 (be patient)
    Completed 1000 requests
    Completed 2000 requests
    Completed 3000 requests
    Completed 4000 requests
    Completed 5000 requests
    Completed 6000 requests
    Completed 7000 requests
    Completed 8000 requests
    Completed 9000 requests
    Completed 10000 requests
    Finished 10000 requests


    Server Software:        Apache/2.4.29
    Server Hostname:        127.0.0.1
    Server Port:            80

    Document Path:          /test500bytes.html
    Document Length:        290 bytes

    Concurrency Level:      10000
    Time taken for tests:   64.100 seconds
    Complete requests:      10000
    Failed requests:        352
    (Connect: 0, Receive: 0, Length: 352, Exceptions: 0)
    Non-2xx responses:      9659
    Total transferred:      4539730 bytes
    HTML transferred:       2801110 bytes
    Requests per second:    156.01 [#/sec] (mean)
    Time per request:       64100.455 [ms] (mean)
    Time per request:       6.410 [ms] (mean, across all concurrent requests)
    Transfer rate:          69.16 [Kbytes/sec] received

    Connection Times (ms)
                min  mean[+/-sd] median   max
    Connect:        0   95 287.3      3    1050
    Processing:     4 4611 13701.0     13   63738
    Waiting:        0 3234 11741.9     12   63050
    Total:         12 4706 13911.5     15   64060

    Percentage of the requests served within a certain time (ms)
    50%     15
    66%     17
    75%     18
    80%     19
    90%  27999
    95%  30495
    98%  63993
    99%  64053
    100%  64060 (longest request)
    
## Testing Nginx Web Server    

Using Ubuntu 18.04 and nginx/1.14.0 (Ubuntu)

###Configuration
Procced the same step from Apache Web Server Configuration
Move file to /var/www/html

    sudo cp resource/test20kb.html
    sudo cp resource/test500bytes.html

Raise the opened file limit

    sudo cp resource/limits.conf /etc/security/
    ulimit -n 20000

### Result

Command for 20kb html files

    ab -n 10000 -c 10000 http://127.0.0.1/test20kb.html

Benchmark Result

    This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/

    Benchmarking 127.0.0.1 (be patient)
    Completed 1000 requests
    Completed 2000 requests
    Completed 3000 requests
    Completed 4000 requests
    Completed 5000 requests
    Completed 6000 requests
    Completed 7000 requests
    Completed 8000 requests
    Completed 9000 requests
    Completed 10000 requests
    Finished 10000 requests


    Server Software:        
    Server Hostname:        127.0.0.1
    Server Port:            80

    Document Path:          /test20kb.html
    Document Length:        0 bytes

    Concurrency Level:      10000
    Time taken for tests:   0.706 seconds
    Complete requests:      10000
    Failed requests:        10000
    (Connect: 0, Receive: 0, Length: 1744, Exceptions: 8256)
    Total transferred:      35980464 bytes
    HTML transferred:       35553184 bytes
    Requests per second:    14155.32 [#/sec] (mean)
    Time per request:       706.448 [ms] (mean)
    Time per request:       0.071 [ms] (mean, across all concurrent requests)
    Transfer rate:          49737.80 [Kbytes/sec] received

    Connection Times (ms)
                min  mean[+/-sd] median   max
    Connect:      153  263  69.7    257     451
    Processing:    73  113  21.2    112     207
    Waiting:        0   14  30.2      0     141
    Total:        246  376  87.8    365     603

    Percentage of the requests served within a certain time (ms)
    50%    365
    66%    414
    75%    443
    80%    458
    90%    494
    95%    541
    98%    575
    99%    588
    100%    603 (longest request)

Command for 500bytes html files

    ab -n 10000 -c 10000 http://127.0.0.1/test500bytes.html

Benchmark Result

    This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/

    Benchmarking 127.0.0.1 (be patient)
    Completed 1000 requests
    Completed 2000 requests
    Completed 3000 requests
    Completed 4000 requests
    Completed 5000 requests
    Completed 6000 requests
    Completed 7000 requests
    Completed 8000 requests
    Completed 9000 requests
    Completed 10000 requests
    Finished 10000 requests


    Server Software:        
    Server Hostname:        127.0.0.1
    Server Port:            80

    Document Path:          /test500bytes.html
    Document Length:        0 bytes

    Concurrency Level:      10000
    Time taken for tests:   0.686 seconds
    Complete requests:      10000
    Failed requests:        10000
    (Connect: 0, Receive: 0, Length: 1712, Exceptions: 8288)
    Non-2xx responses:      1712
    Total transferred:      576944 bytes
    HTML transferred:       304736 bytes
    Requests per second:    14578.05 [#/sec] (mean)
    Time per request:       685.963 [ms] (mean)
    Time per request:       0.069 [ms] (mean, across all concurrent requests)
    Transfer rate:          821.36 [Kbytes/sec] received

    Connection Times (ms)
                min  mean[+/-sd] median   max
    Connect:      149  265  75.5    258     441
    Processing:    73  109  20.0    107     195
    Waiting:        0   14  31.9      0     139
    Total:        241  374  93.7    362     588

    Percentage of the requests served within a certain time (ms)
    50%    362
    66%    411
    75%    439
    80%    454
    90%    518
    95%    563
    98%    579
    99%    584
    100%    588 (longest request)

## Event-Based Web Server

### Low Level Server

Using Python3 with PyUV version 1.4.0

#### Installation

install PyUV package

    pip install pyuv

#### How to Run

    python src/low_level.py [File Type]

#### Result
Command for 500bytes html files

Run and Benchmark Command

    python src/low_level.py FILE_500_B
    ab -n 10000 -c 10000 http://127.0.0.1:8000/

Benchmark Result

    This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/

    Benchmarking 127.0.0.1 (be patient)
    Completed 1000 requests
    Completed 2000 requests
    Completed 3000 requests
    Completed 4000 requests
    Completed 5000 requests
    Completed 6000 requests
    Completed 7000 requests
    Completed 8000 requests
    Completed 9000 requests
    Completed 10000 requests
    Finished 10000 requests


    Server Software:        Apache/2.2.3
    Server Hostname:        127.0.0.1
    Server Port:            8000

    Document Path:          /
    Document Length:        488 bytes

    Concurrency Level:      10000
    Time taken for tests:   0.768 seconds
    Complete requests:      10000
    Failed requests:        0
    Total transferred:      6690000 bytes
    HTML transferred:       4880000 bytes
    Requests per second:    13014.29 [#/sec] (mean)
    Time per request:       768.386 [ms] (mean)
    Time per request:       0.077 [ms] (mean, across all concurrent requests)
    Transfer rate:          8502.50 [Kbytes/sec] received

    Connection Times (ms)
                min  mean[+/-sd] median   max
    Connect:      150  248  63.7    242     416
    Processing:   169  182  12.7    184     208
    Waiting:      108  158  29.3    164     207
    Total:        358  430  53.0    423     586

    Percentage of the requests served within a certain time (ms)
    50%    423
    66%    440
    75%    456
    80%    466
    90%    510
    95%    547
    98%    570
    99%    577
    100%    586 (longest request)

Command for 20kb html files

Run and Benchmark Command

    python src/low_level.py FILE_20_KB
    ab -n 10000 -c 10000 http://127.0.0.1:8000/

Benchmark Result

    This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/

    Benchmarking 127.0.0.1 (be patient)
    Completed 1000 requests
    Completed 2000 requests
    Completed 3000 requests
    Completed 4000 requests
    Completed 5000 requests
    Completed 6000 requests
    Completed 7000 requests
    Completed 8000 requests
    Completed 9000 requests
    Completed 10000 requests
    Finished 10000 requests


    Server Software:        Apache/2.2.3
    Server Hostname:        127.0.0.1
    Server Port:            8000

    Document Path:          /
    Document Length:        20386 bytes

    Concurrency Level:      10000
    Time taken for tests:   0.952 seconds
    Complete requests:      10000
    Failed requests:        0
    Total transferred:      205690000 bytes
    HTML transferred:       203860000 bytes
    Requests per second:    10500.04 [#/sec] (mean)
    Time per request:       952.377 [ms] (mean)
    Time per request:       0.095 [ms] (mean, across all concurrent requests)
    Transfer rate:          210913.47 [Kbytes/sec] received

    Connection Times (ms)
                min  mean[+/-sd] median   max
    Connect:      152  256  65.5    253     429
    Processing:   188  242  58.6    217     378
    Waiting:      126  220  78.3    205     378
    Total:        461  499  32.0    489     619

    Percentage of the requests served within a certain time (ms)
    50%    489
    66%    504
    75%    512
    80%    518
    90%    536
    95%    573
    98%    600
    99%    609
    100%    619 (longest request)


### High Level Server

Using Tornado version 6.0.3 Package and Python3

#### Installation

install PyUV package

    pip install Tornado

#### How to Run

    python src/Tornado.py [File Type]

#### Result
Command for 500 bytes html files

Run and Benchmark Command

    python src/low_level.py FILE_500_B
    ab -n 10000 -c 10000 http://127.0.0.1:8000/

Benchmark Result

    This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/

    Benchmarking 127.0.0.1 (be patient)
    Completed 1000 requests
    Completed 2000 requests
    Completed 3000 requests
    Completed 4000 requests
    Completed 5000 requests
    apr_pollset_poll: The timeout specified has expired (70007)
    Total of 5433 requests completed
    root@thareq:~# ab -n 10000 -c 10000 -s 1000 http://127.0.0.1:8000/
    This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/

    Benchmarking 127.0.0.1 (be patient)
    Completed 1000 requests
    Completed 2000 requests
    Completed 3000 requests
    Completed 4000 requests
    Completed 5000 requests
    Completed 6000 requests
    Completed 7000 requests
    Completed 8000 requests
    Completed 9000 requests
    apr_socket_recv: Connection reset by peer (104)
    Total of 9687 requests completed

Command for 20 kb html files

Run and Benchmark Command

    python src/low_level.py FILE_20_KB
    ab -n 10000 -c 10000 http://127.0.0.1:8000/

Benchmark Result

    This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/

    Benchmarking 127.0.0.1 (be patient)
    Completed 1000 requests
    Completed 2000 requests
    Completed 3000 requests
    Completed 4000 requests
    Completed 5000 requests
    apr_pollset_poll: The timeout specified has expired (70007)
    Total of 5433 requests completed
    root@thareq:~# ab -n 10000 -c 10000 -s 1000 http://127.0.0.1:8000/
    This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/

    Benchmarking 127.0.0.1 (be patient)
    Completed 1000 requests
    Completed 2000 requests
    Completed 3000 requests
    Completed 4000 requests
    Completed 5000 requests
    Completed 6000 requests
    Completed 7000 requests
    Completed 8000 requests
    Completed 9000 requests
    apr_socket_recv: Connection reset by peer (104)
    Total of 9687 requests completed






