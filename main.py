import debugpy
import statistics
from reactsignal import Signal
from logger_config import logger
import time

import logging


def benchmark_fanout(num_computed: int, iterations: int):
    """
    Create one base signal and `num_computed` dependent Signals.
    Then update the base signal and measure how long the update takes.
    """
    creation_times = []
    times = []
    for _ in range(iterations):
        start_reation = time.time()
        base = Signal(lambda: 0, name="Base")
        computed_list = [
            Signal(lambda base=base: base() + 1, name=f"Comp{i}", sources=[base])
            for i in range(num_computed)
        ]
        final = Signal(lambda: sum([s() for s in computed_list]), name="Final")
        end_reation = time.time()
        creation_times.append(end_reation - start_reation)
        start = time.time()
        base.set(1)  # Trigger all computations
        result = final()  # Warm-up
        end = time.time()
        times.append(end - start)
        logger.info(f"{result=}")
    return statistics.median(times), statistics.median(times)


def benchmark_chain(chain_length, iterations):
    """
    Create a chain of Signals where each depends on the previous one.
    Then update the base signal and measure the propagation time.
    """
    creation_times = []
    times = []
    for _ in range(iterations):
        start_reation = time.time()
        base = Signal(0, name="Base")
        prev = base
        chain = []
        for i in range(chain_length):
            comp = Signal(lambda a=prev: a() + 1, name="Chain")
            chain.append(comp)
            prev = comp
        end_reation = time.time()
        creation_times.append(end_reation - start_reation)

        start = time.time()
        _ = chain[-1]()  # Warm-up
        base.set(1)  # Trigger the full recomputation chain
        result = chain[-1]()
        end = time.time()
        logger.info(f"{result=}")
        times.append(end - start)
    return statistics.median(creation_times), statistics.median(times)


if __name__ == "__main__":
    # debugpy.listen(("localhost", 5678))
    # debugpy.wait_for_client()
    logger.setLevel(logging.INFO)
    print("Benchmarking chain propagation time...")
    fancy_chain_length = 100_000
    fancy_fanout = 3
    iterations = 1
    creation, propagation_time = benchmark_chain(fancy_chain_length, iterations)
    logger.info(
        f"Chain {fancy_chain_length}: Creation: {creation:.2f}s Prop: {propagation_time:.2f}s"
    )

    # creation, fanout_time = benchmark_fanout(fancy_fanout, iterations)
    # logger.info(
    #     f"Fanout {fancy_fanout}: Creation: {creation:.2f}s Prop: {fanout_time:.2f}s"
    # )

    # anim = Animatable()
    # anim2 = Animatable()
    # tqdm.tqdm.write("Tweening")
    # for tweenVal in tween.tween(1, lambda x: A(x), mapping=easeInOutCubic):
    #     # Print blocks interpolated by result of C() as int
    #     print(f"\r{anim2.position.x():3.3f}", end="")
    #     sleep(1/FPS)
