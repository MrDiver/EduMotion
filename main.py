import statistics
from signal import Signal
from time import sleep
import tween
import tqdm
import time

from tween import FPS
from tween import easeInQuad
from tween import easeInOutCubic

from animatable import Animatable

def benchmark_fanout(num_computed, iterations):
    """
    Create one base signal and `num_computed` dependent Signals.
    Then update the base signal and measure how long the update takes.
    """
    times = []
    for _ in range(iterations):
        base = Signal(lambda: 0, name="Base")
        computed_list = [Signal(lambda base=base: base(), name=f"Comp{i}") for i in range(num_computed)]
        _ = computed_list[-1]()  # Warm-up
        start = time.time()
        base.set(1)  # Trigger all computations
        end = time.time()
        times.append(end - start)
    return statistics.median(times)

def benchmark_chain(chain_length, iterations):
    """
    Create a chain of Signals where each depends on the previous one.
    Then update the base signal and measure the propagation time.
    """
    times = []
    for _ in range(iterations):
        base = Signal(lambda: 0, name="Base")
        prev = base
        chain = []
        for i in range(chain_length):
            comp = Signal(lambda prev=prev: prev(), name=f"Chain{i}")
            chain.append(comp)
            prev = comp
        _ = chain[-1]()  # Warm-up
        start = time.time()
        base.set(1)  # Trigger the full recomputation chain
        end = time.time()
        times.append(end - start)
    return statistics.median(times)

if __name__ == "__main__":
    print("Benchmarking chain propagation time...")
    fancy_chain_length = 1000
    fancy_fanout = 1000
    iterations = 10
    propagation_time = benchmark_chain(fancy_chain_length, iterations)
    print(f"Median propagation time for chain of length {fancy_chain_length}: {propagation_time:.6f} s")

    fanout_time = benchmark_fanout(fancy_fanout, iterations)
    print(f"Median propagation time for fanout of size {fancy_fanout}: {fanout_time:.6f} s")

    # anim = Animatable()
    # anim2 = Animatable()
    # tqdm.tqdm.write("Tweening")
    # for tweenVal in tween.tween(1, lambda x: A(x), mapping=easeInOutCubic):
    #     # Print blocks interpolated by result of C() as int 
    #     print(f"\r{anim2.position.x():3.3f}", end="")
    #     sleep(1/FPS)
