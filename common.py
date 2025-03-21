def format_duration(duration: float) -> str:
    """
    Format a duration (in seconds) into a human-readable string with an appropriate unit.

    If duration is:
      - < 1e-6 seconds, use nanoseconds (ns)
      - < 1e-3 seconds, use microseconds (µs)
      - < 1 second, use milliseconds (ms)
      - otherwise, use seconds (s)
    """
    if duration < 1e-6:
        # Convert to nanoseconds
        return f"{duration * 1e9:.2f} ns"
    elif duration < 1e-3:
        # Convert to microseconds
        return f"{duration * 1e6:.2f} µs"
    elif duration < 1:
        # Convert to milliseconds
        return f"{duration * 1e3:.2f} ms"
    else:
        # Use seconds
        return f"{duration:.2f} s"
