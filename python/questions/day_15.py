"""
Whats is the python GIL?

GIL stands for global interpreter lock. This is a feature of python that do not allow threads
to run concurrently. This happens because multiple threads can only access one interpreter at a
time and when one of those threads is accessing it, it locks making the other threads having to 
stop.
"""