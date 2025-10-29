import subprocess
import psutil
import time

# Left-hand side: ROB, IQ, LSQ
lhs = [
    "16,11,5",
    "32,21,11",
    "64,43,21",
    "128,85,43",
    "256,171,85",
    "512,341,171"
]

# Right-hand side: Local, Global, BTB, RAS
rhs = [
    "64,128,128,16",
    "128,256,128,16",
    "256,512,256,16",
    "512,1024,512,32",
    "1024,2048,1024,32",
    "2048,4096,2048,64",
    "4096,8192,4096,128",
    "8192,16384,8192,256"
]

#sizes = [2**i for i in range(4,10)] #16..512
#mininum_phys_reg_size = 49 #as informed by simulate.py

for i, window_size in enumerate(lhs):
    for branch_pred_size in rhs:
        name = f"window_size_{window_size}_branch_pred_size_{branch_pred_size}"

        #load balancer if running jobs in parallel. runs will crash if cpu usage gets too high.
        #while psutil.cpu_percent() > 70: time.sleep(30)
        #.run won't return until the program finishes. using .Popen returns immediately, meaning all runs execute in parallel (be mindful of your machine's resources though!). however, it has fewer features like capturing program output.
        subprocess.run("python /homes/lp721/aca-gem5/simulate.py --window_size "+str(window_size)+" --branch-pred-size "+str(branch_pred_size)+" --name "+name, shell=True)
