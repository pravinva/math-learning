// Shared canvas plotting helper for DPEN21 practice exams.
// Each <canvas data-plot='{...}'> is rendered on DOMContentLoaded.
function drawPlot(canvas){
  const cfg = JSON.parse(canvas.getAttribute('data-plot'));
  const W = canvas.width = 380, H = canvas.height = 260;
  const ctx = canvas.getContext('2d');
  const {xmin,xmax,ymin,ymax} = cfg;
  const X = x => (x-xmin)/(xmax-xmin)*W;
  const Y = y => H-(y-ymin)/(ymax-ymin)*H;
  ctx.clearRect(0,0,W,H);
  // grid
  ctx.strokeStyle='#eef1f5'; ctx.lineWidth=1;
  for(let gx=Math.ceil(xmin);gx<=xmax;gx++){ctx.beginPath();ctx.moveTo(X(gx),0);ctx.lineTo(X(gx),H);ctx.stroke();}
  for(let gy=Math.ceil(ymin);gy<=ymax;gy++){ctx.beginPath();ctx.moveTo(0,Y(gy));ctx.lineTo(W,Y(gy));ctx.stroke();}
  // axes
  ctx.strokeStyle='#94a3b8'; ctx.lineWidth=1.4;
  if(ymin<0&&ymax>0){ctx.beginPath();ctx.moveTo(0,Y(0));ctx.lineTo(W,Y(0));ctx.stroke();}
  if(xmin<0&&xmax>0){ctx.beginPath();ctx.moveTo(X(0),0);ctx.lineTo(X(0),H);ctx.stroke();}
  // dashed reference lines
  (cfg.hlines||[]).forEach(l=>{ctx.save();ctx.strokeStyle=l.color||'#9ca3af';if(l.dash)ctx.setLineDash([5,4]);ctx.beginPath();ctx.moveTo(0,Y(l.y));ctx.lineTo(W,Y(l.y));ctx.stroke();ctx.restore();});
  // functions
  const plotFn=(f,color)=>{
    ctx.strokeStyle=color||'#185FA5';ctx.lineWidth=2;ctx.beginPath();let started=false;
    for(let px=0;px<=W;px++){const x=xmin+px/W*(xmax-xmin);let y;try{y=Function('x','return '+f)(x);}catch(e){y=NaN;}
      if(!isFinite(y)){started=false;continue;} const py=Y(y);
      if(py<-1000||py>H+1000){started=false;continue;}
      if(!started){ctx.moveTo(X(x),py);started=true;}else{ctx.lineTo(X(x),py);}}
    ctx.stroke();
  };
  (cfg.funcs||[]).forEach(fn=>plotFn(fn.f,fn.color));
  // piecewise segments
  (cfg.piecewise||[]).forEach(seg=>{
    ctx.strokeStyle=cfg.color||'#C1440E';ctx.lineWidth=2;ctx.beginPath();let started=false;
    for(let px=0;px<=W;px++){const x=xmin+px/W*(xmax-xmin);if(x<seg.xmin||x>seg.xmax){started=false;continue;}
      let y=Function('x','return '+seg.f)(x);const py=Y(y);
      if(!started){ctx.moveTo(X(x),py);started=true;}else{ctx.lineTo(X(x),py);}}
    ctx.stroke();
  });
  // straight lines through two points
  (cfg.lines||[]).forEach(l=>{
    ctx.strokeStyle=l.color||'#185FA5';ctx.lineWidth=2;
    const m=(l.p2[1]-l.p1[1])/(l.p2[0]-l.p1[0]);const b=l.p1[1]-m*l.p1[0];
    ctx.beginPath();ctx.moveTo(X(xmin),Y(m*xmin+b));ctx.lineTo(X(xmax),Y(m*xmax+b));ctx.stroke();
  });
  // circles
  (cfg.circles||[]).forEach(c=>{
    ctx.strokeStyle=c.color||'#185FA5';ctx.lineWidth=2;ctx.beginPath();
    const rx=c.r/(xmax-xmin)*W, ry=c.r/(ymax-ymin)*H;
    ctx.ellipse(X(c.cx),Y(c.cy),rx,ry,0,0,2*Math.PI);ctx.stroke();
  });
  // points
  (cfg.points||[]).forEach(p=>{
    ctx.fillStyle='#1f2937';ctx.beginPath();ctx.arc(X(p[0]),Y(p[1]),3.5,0,2*Math.PI);ctx.fill();
    ctx.font='11px sans-serif';ctx.fillText('('+p[0]+','+p[1]+')',X(p[0])+6,Y(p[1])-6);
  });
}
document.addEventListener("DOMContentLoaded",()=>{
  document.querySelectorAll('canvas[data-plot]').forEach(drawPlot);
  renderMathInElement(document.body,{delimiters:[{left:"$$",right:"$$",display:true},{left:"\\[",right:"\\]",display:true},{left:"\\(",right:"\\)",display:false},{left:"$",right:"$",display:false}],throwOnError:false});
});
