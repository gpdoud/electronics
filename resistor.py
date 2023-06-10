# Displays reistance in color bands

bands = dict(
    black=0, brown=1, red=2, orange=3, yellow=4,
    green=5, blue=6, violet=7, grey=8, white=9
)
tolerance = dict(
    brown=0.01, red=0.02, gold=0.05, silver=0.1
)

def four_color_bands(b1, b2, b3, t):
    b1, b2, b3, t = b1.lower(), b2.lower(), b3.lower(), t.lower()
    ohms = (bands[b1]*10 + bands[b2]) * 10**bands[b3]
    _format_range(ohms, t)
    # tol = tolerance[t]*100
    # range = f"[{ohms * (1 - tolerance[t]):.0f} <= T <= {ohms * (1 + tolerance[t]):.0f}]"
    # print(f"{ohms:,d} ohms; {tol}% tolerance; {range} range ")

def five_color_bands(b1, b2, b3, b4, t):
    b1, b2, b3, b4, t = b1.lower(), b2.lower(), b3.lower(), b4.lower(), t.lower()
    ohms = (bands[b1]*100 + bands[b2]*10 + bands[b3]) * 10**bands[b4]
    _format_range(ohms, t)
    # tol = tolerance[t]*100
    # range = f"[{ohms * (1 - tolerance[t]):,.0f} <= T <= {ohms * (1 + tolerance[t]):,.0f}]"
    # print(f"{ohms:,d} ohms; {tol}% tolerance; {range} range ")

def _format_range(ohms, t):
    tol = tolerance[t]*100
    range = f"[{ohms * (1 - tolerance[t]):,.0f} <= T <= {ohms * (1 + tolerance[t]):,.0f}]"
    print(f"{ohms:,d} ohms; {tol}% tolerance; {range} range ")

if __name__ == "__main__":
    # four bands
    four_color_bands("yellow", 'violet', 'brown', 'silver') #
