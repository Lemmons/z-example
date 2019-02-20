import cowsay

from my_module.sub_module import hello

def whatup(name):
    hello.say_hello(name)
    cowsay.tux('yo! whatup?')
