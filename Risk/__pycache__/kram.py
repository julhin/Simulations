import random as rnd

def run():
    histogram ={}
    for i in range(0,100):
        roll = rnd.randint(1,6)
        if roll in histogram:
            histogram[roll] = histogram[roll] + 1
        else:
            histogram[roll] = 0   
    print(histogram)
if __name__ == "__main__":
    run()