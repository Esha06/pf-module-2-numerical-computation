"""Turn raw scientific measurements into a readable text report."""
import math


def summarize(values):
    """Return count, mean, min, max and (population) standard deviation."""
    n = len(values)
    if n == 0:
        raise ValueError("no values to summarize")
    mean = sum(values) / n
    variance = sum((x - mean) ** 2 for x in values) / n
    return {
        "n": n,
        "mean": mean,
        "min": min(values),
        "max": max(values),
        "std": math.sqrt(variance),
    }


def format_report(title, datasets, decimals=2):
    """datasets maps a quantity name to {"unit": str, "values": [numbers]}."""
    header = f"{'Quantity':<14}{'Unit':<7}{'n':>3}{'Mean':>10}{'Min':>10}{'Max':>10}{'Std':>8}"
    rule = "-" * len(header)
    lines = [title, "=" * len(title), header, rule]
    for name, data in datasets.items():
        s = summarize(data["values"])
        lines.append(
            f"{name:<14}{data['unit']:<7}{s['n']:>3}"
            f"{s['mean']:>10.{decimals}f}{s['min']:>10.{decimals}f}"
            f"{s['max']:>10.{decimals}f}{s['std']:>8.{decimals}f}"
        )
    total = sum(len(d["values"]) for d in datasets.values())
    lines.append(rule)
    lines.append(f"{len(datasets)} quantities, {total} readings in total.")
    return "\n".join(lines)
