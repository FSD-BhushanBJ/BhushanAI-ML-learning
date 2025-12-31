#Heads and tails game using random funcions

import random 

coin_toss = random.randint(0,1)

if coin_toss == 1: {
    print("Heads",coin_toss)
}
else:{
    print("Tails",coin_toss)
}