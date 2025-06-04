"""
What is the difference between a Container and an Image?

A container is the environment in which the image will run, it stores environment
variables, has it's own endpoint and data.
"""

"""
What are the differences between Docker and VM?

The main difference is that Docker runs on top of the host kernel — this means 
Docker shares the same kernel as the host. On the other hand, a virtual machine 
emulates an entire operating system, which requires booting up a full OS and 
results in a slower startup process.

VMs are useful when you need full isolation between environments. A great 
example would be running untrusted applications, where strong separation from 
the host is critical.
"""