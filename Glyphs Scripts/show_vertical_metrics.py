Glyphs.clearLog()
f = Glyphs.font

for master in f.masters:
    print(master)
    for metric in master.metrics:
        print(f"{metric.name}: {metric.position}")
    print("\n")