turns=[]
for _ in range(15): turns=turns+[1]+[-t for t in reversed(turns)]
x=y=0;dx,dy=1,0;pts=[(0,0)];x,y=1,0;pts.append((1,0))
for t in turns:
    dx,dy=(-dy,dx) if t==1 else (dy,-dx)
    x+=dx;y+=dy;pts.append((x,y))
xs=[p[0] for p in pts];ys=[p[1] for p in pts];x0,y0=min(xs),min(ys);w=max(xs)-x0;h=max(ys)-y0
s='<svg xmlns="http://www.w3.org/2000/svg" viewBox="-5 -5 %d %d"><rect x="-5" y="-5" width="100%%" height="100%%" fill="#1a1020"/>'%(w+10,h+10)
n=len(pts)
for i in range(0,n-1,4):
    seg=pts[i:i+5];s+='<polyline fill="none" stroke="hsl(%d,85%%,60%%)" stroke-width=".35" points="%s"/>'%(300*i//n+20," ".join("%d,%d"%(a-x0,b-y0) for a,b in seg))
open('d.svg','w').write(s+'</svg>')
