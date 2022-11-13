def zip(ks:list[str], vs: list[str]) -> dict[str, str]:
    """Build a dict from two lists."""
    result: dict[str, str] ={}
    i: int = 0
    assert len(ks) == len(vs)
    while i < len(ks):
        result[ks[i]] = vs[i]
        i += 1
    return result

