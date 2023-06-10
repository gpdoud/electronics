# Conversions

elist = [(18,'E'), (15,'P'), (12,'T'), (9,'G'), (6,'M'), (3,'k'), 
         (0,''), (-3,'m'), (-6,'u'), (-9,'n'), (-12,'p'), (-15,'f')]

def convert(nbr, *, type="", dec=3):
        for el in elist:
            e, r = el
            mag = 1 * 10 ** e
            if nbr >= mag:
                return f"{nbr / mag:.{dec}f} {r}{type}"
        else:
            return "Out of range!"
        
        
if __name__ == "__main__":
    exponents = range(-15,16)
    for exp in exponents:
        value = 1.234 * 10 ** exp
        converted = convert(value, type="A")
        print(f"{value:,e} converted is {converted}")


"""
Name	Symbol	Value	Name	Symbol	Value
quetta	Q	    10e30	quecto	q	    10e-30
ronna	R	    10e27	ronto	r	    10e-27
yotta	Y	    10e23	yocto	y	    10e-24
zetta	Z	    10e21	zepto	z	    10e-21
exa	    E	    10e18	atto	a	    10e-18
peta	P	    10e15	femto	f	    10e-15
tera	T	    10e12	pico	p	    10e-12
giga	G	    10e9    nano	n	    10e-9
mega	M	    10e6    micro	μ	    10e-6
kilo	k	    10e3    milli	m	    10e-3
hecto	h	    10e2    centi	c	    10e-2
deca	d	    10e1    deci	d	    10e-1
"""