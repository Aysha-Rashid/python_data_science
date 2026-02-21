import time as t

TimePassedSinceEpoch = t.time()

Epoch_Unix = t.strftime("%B %-d, %Y", t.gmtime(0))

print(
    f"Seconds since {Epoch_Unix}: {TimePassedSinceEpoch:,.4f} or"
    f" {TimePassedSinceEpoch:.2e} in scientific notation"
)

current_time = t.gmtime()
print(t.strftime("%b %d %Y", current_time))
