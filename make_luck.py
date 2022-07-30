import math as maths

MAX_LUCK = 12

HEAD_TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" width="480" height="750" viewBox="0 0 160 250">
    <defs>
        <radialGradient id="orb">
            <stop stop-color="#fff" stop-opacity="0.25" offset="0%" />
            <stop stop-color="#fff" stop-opacity="0" offset="100%" />
        </radialGradient>
    </defs>
    <!-- background -->
    <rect x="0" y="0" width="160" height="125" fill="#bfb" />
    <rect x="0" y="125" width="160" height="125" fill="{red_color}" />
    """

# For the highest card (12)
TOP_TEMPLATE = """
    <g font-family="Ubuntu Mono" text-anchor="middle" fill="#333" font-size="16">
        <text x="80" y="36" font-size="28" font-weight="bold" font-family="Ubuntu">Brilliance</text>
        <text x="80" y="227">Reclaim your</text>
        <text x="80" y="242">played Action!</text>
    </g>"""

TAIL_TEMPLATE = """
    <g transform="translate(80 125) rotate(90)" fill="none" stroke="#000" stroke-width="6" opacity="0.075" stroke-linejoin="round" stroke-linecap="round">
<path d="M-32.9,-101.2 L-29.4,-104.8 L-25.4,-108.4 L-20.9,-111.8 L-15.8,-114.9 L-10.2,-117.8 L-4.1,-120.2 L2.5,-122.1 L9.5,-123.3 L16.8,-123.9 L24.2,-123.6 L31.8,-122.5 L39.2,-120.5 L46.3,-117.8 L53,-114.2 L59.2,-110.1 L64.8,-105.3 L69.8,-100.2 L74,-94.8 L77.5,-89.3 L80.4,-83.7 L82.6,-78.1 L84.2,-72.7 L85.4,-67.5 L86.1,-62.6" />
<path d="M86.1,-62.6 L35.2,-25.6" />
<path d="M35.2,-25.6 L35.4,-21.9 L35.3,-18.2 L34.9,-14.6 L34.2,-11.1 L33.3,-7.9 L32.2,-5 L31,-2.3 L29.8,-0" />
<path d="M35.2,-25.6 L31.8,-26.9 L28.2,-28 L24.7,-28.7 L21.2,-29.1 L17.8,-29.2 L14.7,-29.1 L11.8,-28.8 L9.2,-28.3" />
<path d="M29.8,-0 L12.2,-0" />
<path d="M3.8,-11.6 L6,-8.9 L8.3,-6 L10.4,-3 L12.2,-0" />
<path d="M86.1,-62.6 L90.6,-60.3 L95.2,-57.6 L99.8,-54.4 L104.4,-50.6 L108.9,-46.1 L113,-41.1 L116.9,-35.4 L120.2,-29.1 L123,-22.3 L125,-15.1 L126.3,-7.6 L126.7,-0 L126.3,7.6 L125,15.1 L123,22.3 L120.2,29.1 L116.9,35.4 L113,41.1 L108.9,46.1 L104.4,50.6 L99.8,54.4 L95.2,57.6 L90.6,60.3 L86.1,62.6" />
<path d="M86.1,62.6 L35.2,25.6" />
<path d="M35.2,25.6 L31.8,26.9 L28.2,28 L24.7,28.7 L21.2,29.1 L17.8,29.2 L14.7,29.1 L11.8,28.8 L9.2,28.3" />
<path d="M35.2,25.6 L35.4,21.9 L35.3,18.2 L34.9,14.6 L34.2,11.1 L33.3,7.9 L32.2,5 L31,2.3 L29.8,-0" />
<path d="M9.2,28.3 L3.8,11.6" />
<path d="M12.2,-0 L10.4,3 L8.3,6 L6,8.9 L3.8,11.6" />
<path d="M86.1,62.6 L85.4,67.5 L84.2,72.7 L82.6,78.1 L80.4,83.7 L77.5,89.3 L74,94.8 L69.8,100.2 L64.8,105.3 L59.2,110.1 L53,114.2 L46.3,117.8 L39.2,120.5 L31.8,122.5 L24.2,123.6 L16.8,123.9 L9.5,123.3 L2.5,122.1 L-4.1,120.2 L-10.2,117.8 L-15.8,114.9 L-20.9,111.8 L-25.4,108.4 L-29.4,104.8 L-32.9,101.2" />
<path d="M-32.9,101.2 L-13.5,41.4" />
<path d="M-13.5,41.4 L-15.8,38.5 L-17.9,35.5 L-19.7,32.3 L-21.2,29.1 L-22.3,26 L-23.1,23 L-23.7,20.1 L-24.1,17.5" />
<path d="M-13.5,41.4 L-9.9,40.5 L-6.4,39.2 L-3.1,37.7 L0,36 L2.8,34.1 L5.2,32.2 L7.4,30.2 L9.2,28.3" />
<path d="M-24.1,17.5 L-9.9,7.2" />
<path d="M3.8,11.6 L0.4,10.8 L-3.2,9.7 L-6.6,8.5 L-9.9,7.2" />
<path d="M-32.9,101.2 L-37.8,102.1 L-43.1,102.6 L-48.8,102.7 L-54.7,102.3 L-60.9,101.3 L-67.3,99.7 L-73.8,97.3 L-80.2,94.2 L-86.4,90.4 L-92.3,85.7 L-97.7,80.4 L-102.5,74.5 L-106.7,68 L-110.1,61.2 L-112.6,54.2 L-114.4,47.1 L-115.4,40.1 L-115.6,33.2 L-115.2,26.7 L-114.2,20.5 L-112.7,14.7 L-110.9,9.3 L-108.8,4.4 L-106.4,0" />
<path d="M-106.4,0 L-43.5,0" />
<path d="M-43.5,0 L-41.5,-3.1 L-39.3,-6.1 L-36.8,-8.7 L-34.2,-11.1 L-31.6,-13.2 L-29,-14.9 L-26.5,-16.3 L-24.1,-17.5" />
<path d="M-43.5,0 L-41.5,3.1 L-39.3,6.1 L-36.8,8.7 L-34.2,11.1 L-31.6,13.2 L-29,14.9 L-26.5,16.3 L-24.1,17.5" />
<path d="M-24.1,-17.5 L-9.9,-7.2" />
<path d="M-9.9,7.2 L-10.1,3.7 L-10.2,0 L-10.1,-3.7 L-9.9,-7.2" />
<path d="M-106.4,0 L-108.8,-4.4 L-110.9,-9.3 L-112.7,-14.7 L-114.2,-20.5 L-115.2,-26.7 L-115.6,-33.2 L-115.4,-40.1 L-114.4,-47.1 L-112.6,-54.2 L-110.1,-61.2 L-106.7,-68 L-102.5,-74.5 L-97.7,-80.4 L-92.3,-85.7 L-86.4,-90.4 L-80.2,-94.2 L-73.8,-97.3 L-67.3,-99.7 L-60.9,-101.3 L-54.7,-102.3 L-48.8,-102.7 L-43.1,-102.6 L-37.8,-102.1 L-32.9,-101.2" />
<path d="M-32.9,-101.2 L-13.5,-41.4" />
<path d="M-13.5,-41.4 L-9.9,-40.5 L-6.4,-39.2 L-3.1,-37.7 L-0,-36 L2.8,-34.1 L5.2,-32.2 L7.4,-30.2 L9.2,-28.3" />
<path d="M-13.5,-41.4 L-15.8,-38.5 L-17.9,-35.5 L-19.7,-32.3 L-21.2,-29.1 L-22.3,-26 L-23.1,-23 L-23.7,-20.1 L-24.1,-17.5" />
<path d="M9.2,-28.3 L3.8,-11.6" />
<path d="M-9.9,-7.2 L-6.6,-8.5 L-3.2,-9.7 L0.4,-10.8 L3.8,-11.6" />
    </g>
</svg>"""


BAD = (0xcc, 0x33, 0x33)
GOOD = (0xaa, 0xff, 0xaa)
def make_luck(n):
    r = 70
    t = ((n-1) / (MAX_LUCK-1)) ** 0.67
    color = tuple(round(maths.sqrt(t * GOOD[i]**2 + (1-t) * BAD[i]**2)) for i in range(3))
    return HEAD_TEMPLATE.format(red_color = "#bfb" if n == MAX_LUCK else "#fbb") + (
    """<g transform="translate(80 125)">
        <circle cx="0" cy="0" r="{r}" fill="{color}" stroke="#555" stroke-width="8" />
        <circle cx="0" cy="0" r="{r}" fill="url(#orb)" stroke="#555" stroke-width="8" />""" +
        ("""<path d="M0,-{r} A{r},{r},0,{b},1,{arcX:.3f},{arcY:.3f}" """ if n < 20 else """<circle cx="0" cy="0" r="70" """) + """fill="none" stroke="#ccc" stroke-width="4" />
        <g font-family="Ubuntu" font-weight="bold" font-size="96" text-anchor="middle">
            <text x="0" y="30" stroke="#333" stroke-width="8" stroke-linejoin="round">{n}</text>
            <text x="0" y="30" fill="{color}">{n}</text>
        </g>
    </g>\n""").format(
        r=r,
        arcX = r * maths.sin(n*2*maths.pi/MAX_LUCK),
        arcY = r * -maths.cos(n*2*maths.pi/MAX_LUCK),
        color="white" if n == MAX_LUCK else ("rgb" + str(color)),
        n = n,
        a = 1 if n < MAX_LUCK/2 else 0,
        b = 1 if n >= MAX_LUCK/2 else 0,
    ) + (TOP_TEMPLATE if n == MAX_LUCK else "") + TAIL_TEMPLATE



for i in range(1,MAX_LUCK + 1):
    f = open("luck_{}.svg".format(i), "w")
    f.write(make_luck(i))
    f.close()


