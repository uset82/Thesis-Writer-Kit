from dataclasses import dataclass

@dataclass
class ConcurrencyConfig:
    scout_parallel_workers: int = 4
    scout_batch_size: int = 5
    scout_batch_delay: int = 2
    rate_limit_delay: float = 1.0

def get_concurrency_config(verbose: bool = False) -> ConcurrencyConfig:
    return ConcurrencyConfig()

