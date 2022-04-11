# get process id
ps aux | grep teleryum.py

pgrep -a teleryum.py

kill -9 <number>

fg

bg

ps -f

jobs

# nohup
sudo nohup python3 teleryum.py > /path/to/custom.out &
sudo nohup ./mn.sh > myscipt.sh &
nohup ./mn.sh > myscipt.sh &
./mn.sh > myscipt.sh &

kill -l

kill <PID>