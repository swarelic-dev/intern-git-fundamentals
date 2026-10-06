"""Tiny feature flag helper."""

FLAGS = {"new_dashboard": False, "beta_calls": True}


def is_enabled(name):
    """Return True if the named feature flag is on. Unknown flags are off."""
    return FLAGS.get(name, False)