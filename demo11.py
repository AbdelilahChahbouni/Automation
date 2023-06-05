import time

def word_count_in_minute():
    start_time = time.time()
    words = 0
    
    print("Type your words. Press Enter to finish.")
    
    while True:
        user_input = input()
        if user_input == "":
            break
        words += len(user_input.split())
    
    end_time = time.time()
    time_used = end_time - start_time
    words_per_minute = words / (time_used / 60)
    
    print("Word count:", words)
    print("words per seconds :", time_used)
    print("Words per minute:", words_per_minute)

word_count_in_minute()





