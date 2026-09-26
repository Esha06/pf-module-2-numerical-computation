# Module 2 - Part 11: Automated report generation
import report

raw_data = {
    "Temperature": {"unit": "C", "values": [21.43, 21.97, 22.61, 23.08, 22.40]},
    "Pressure": {"unit": "kPa", "values": [101.3, 101.1, 100.9, 101.4, 101.2]},
    "Flow rate": {"unit": "L/min", "values": [12.5, 12.9, 13.4, 12.2, 12.8]},
}

text = report.format_report("Cooling Loop Test - Run 7", raw_data)
print(text)

temps = raw_data["Temperature"]["values"]
s = report.summarize(temps)
conclusion = (
    f"Temperature averaged {s['mean']:.1f} C (range {s['min']:.1f}-{s['max']:.1f} C) "
    f"and rose by {temps[-1] - temps[0]:+.2f} C over the run."
)
print()
print(conclusion)

with open("report.txt", "w") as f:
    f.write(text + "\n\n" + conclusion + "\n")
print("Saved report.txt")
