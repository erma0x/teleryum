# IMPORTANT commands for server

### lunch deamon
```sudo nohup python3 teleryum.py > /path/to/custom.out &```

### find process id
```ps aux | grep teleryum.py```

### kill deamon
```kill -9 <processID>```


# Other commands for server

### Start deamons with nohup

```nohup python3 teleryum.py > /path/to/custom.out &```

```nohup ./mn.sh > myscipt.sh &```

### get process id

```ps aux | grep teleryum.py```

```pgrep -a teleryum.py```


### kill processes

```kill -9 <PID>```

```kill -l```

```kill <PID>```

