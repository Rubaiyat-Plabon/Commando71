import time
import os

def start_receiver():
    print("বেস স্টেশন সক্রিয়...")
    while True:
        # এটি সিমুলেশন ডেটা
        data = "System Online - Ready" 
        with open("logs.txt", "w") as f:
            f.write(data)
        time.sleep(2)

if __name__ == "__main__":
    start_receiver()