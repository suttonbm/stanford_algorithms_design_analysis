import cProfile
from p6 import run2sat

def run():
    run2sat('2sat1.txt')
# END run

cProfile.run('run()')
