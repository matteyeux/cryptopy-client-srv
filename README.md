# cryptopy-client-srv
school project we made in an hour and with few improvments when at home <br>
simple poc don't use in production :P <br>

# usage 
### Server
First, start server, it will listen on port `2345`
### Tree
```
├── client
│   ├── a.txt
│   ├── client.py
│   └── send_file.py
├── example.png
├── GUI
│   ├── client_gui.py
│   └── server_gui.py
├── gui-example.png
├── README.md
└── server
    ├── cesar.py
    ├── receive_file.py
    └── server.py
```
### Client
```
./client.py
usage: ./client.py [message] <key>
```

Make sure you are in the client directory or you'll get an error like that :
```
$ ./client/client.py
Traceback (most recent call last):
  File "./client/client.py", line 8, in <module>
    import cesar
ImportError: No module named 'cesar'
```
Then run client : 
`$ ./client.py bonjour 123`.
Default key is 4<br>

![client-srv-ex](example.png)

I also added a GUI <br>
![client-srv-gui](gui-example.png) 
# credits
- [_thomas](https://twitter.com/0512thomas)
- [eehp](https://twitter.com/eehp205)
- [matteyeux](https://twitter.com/matteyeux)
