from sig.reactsignal import Signal
import pytest


def benchmark_fanout(num_computed: int):
    """
    Create one base signal and `num_computed` dependent Signals.
    Then update the base signal and measure how long the update takes.
    """
    base = Signal(0, name="Base")
    computed_list = [
        Signal(lambda base=base: base() + 1, name=f"Comp{i}")
        for i in range(num_computed)
    ]
    final = Signal(lambda cl=computed_list: sum([s() for s in cl]), name="Final")
    base.set(0)  # Trigger all computations
    result = final()  # Warm-up
    assert result == num_computed


@pytest.mark.parametrize("num_computed", [100, 1000, 10_000])
def test_fanout(benchmark, num_computed):
    benchmark(benchmark_fanout, num_computed)


def benchmark_set(num_nodes: int, num_computed: int):
    """
    Create one base signal and `num_computed` dependent Signals.
    Then update the base signal and measure how long the update takes.
    """
    base = Signal(0, name="Base")
    computed_list = [
        Signal(lambda base=base: base() + 1, name=f"Comp{i}") for i in range(num_nodes)
    ]
    final = Signal(lambda cl=computed_list: sum([s() for s in cl]), name="Final")
    for i in range(num_computed):
        base.set(i)
        _ = computed_list[i % num_nodes]()  # Warm-up
    base.set(0)  # Trigger all computations
    result = final()  # Warm-up
    assert result == num_nodes


@pytest.mark.parametrize("num_computed", [100, 1000, 10_000])
def test_set(benchmark, num_computed):
    benchmark(benchmark_set, 10, num_computed)


def benchmark_grid(num_nodes: int):
    """
    Create a grid of signals and update all of them.
    """
    grid = [
        [Signal(0, name=f"Node{i}_{j}") for j in range(num_nodes)]
        for i in range(num_nodes)
    ]
    for i in range(num_nodes):
        for j in range(num_nodes):
            grid[i][j].set(i + j)
    result = sum([sum([s() for s in row]) for row in grid])


@pytest.mark.parametrize("num_nodes", [5, 10, 100])
def test_grid(benchmark, num_nodes):
    benchmark(benchmark_grid, num_nodes)
