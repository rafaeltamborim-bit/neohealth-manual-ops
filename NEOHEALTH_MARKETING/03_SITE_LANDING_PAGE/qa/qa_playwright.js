// Uso: PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node qa/qa_playwright.js
const {chromium}=require('/opt/node22/lib/node_modules/playwright');
const http=require('http'),fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'..');const types={'.html':'text/html','.css':'text/css','.js':'text/javascript','.jpg':'image/jpeg','.png':'image/png','.xml':'text/xml','.txt':'text/plain'};
const sent=[];
const srv=http.createServer((q,r)=>{let p=decodeURIComponent(q.url.split('?')[0]);if(p==='/')p='/index.html';if(q.method!=='GET'){sent.push(q.method+' '+q.url)}
 fs.readFile(path.join(root,p),(e,d)=>{if(e){r.writeHead(404);return r.end('nf')}r.writeHead(200,{'Content-Type':types[path.extname(p)]||'application/octet-stream'});r.end(d)})});
(async()=>{
 await new Promise(r=>srv.listen(0,r));const base='http://127.0.0.1:'+srv.address().port;
 const b=await chromium.launch();const res=[];const ok=(n,c,d='')=>{res.push({n,c:!!c,d});console.log((c?'PASS ':'FAIL ')+n+(d?' - '+d:''))};
 const external=[];
 for(const w of [375,768,1440]){
  const ctx=await b.newContext({viewport:{width:w,height:900}});const pg=await ctx.newPage();
  pg.on('request',r=>{if(!r.url().startsWith(base)&&!r.url().startsWith('data:'))external.push(r.url())});
  const errs=[];pg.on('pageerror',e=>errs.push(e.message));pg.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
  await pg.goto(base+'/index.html?utm_source=linkedin&utm_medium=paid&utm_campaign=teste&gclid=G123&li_fat_id=L456');
  await pg.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){window.scrollTo({top:y,behavior:'instant'});await new Promise(r=>setTimeout(r,60))}window.scrollTo({top:0,behavior:'instant'})});
  await pg.waitForTimeout(500);
  const o=await pg.evaluate(()=>({sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth,h1:document.querySelectorAll('h1').length,sections:document.querySelectorAll('main section').length,imgsNoAlt:[...document.images].filter(i=>!i.alt).length,broken:[...document.images].filter(i=>i.complete&&i.naturalWidth===0).length}));
  ok(`[${w}] sem overflow horizontal`,o.sw<=o.cw,`scrollWidth=${o.sw} clientWidth=${o.cw}`);
  ok(`[${w}] 15 secoes, 1 H1, imagens com alt, sem imagens quebradas`,o.sections===15&&o.h1===1&&o.imgsNoAlt===0&&o.broken===0,JSON.stringify(o));
  ok(`[${w}] sem erros de console`,errs.length===0,errs.join(' | '));
  await pg.screenshot({path:`qa/landing-${w}-dobra.png`});
  await pg.screenshot({path:`qa/landing-${w}-full.png`,fullPage:true});
  if(w===375){
   ok('menu mobile abre',await (async()=>{await pg.click('#menuBtn');return pg.locator('#mainNav.open').count().then(c=>c===1)})());
   await pg.click('#menuBtn');
  }
  if(w===1440){
   // campos ocultos
   const hid=await pg.evaluate(()=>({s:leadForm.utm_source.value,m:leadForm.utm_medium.value,g:leadForm.gclid.value,l:leadForm.li_fat_id.value,u:leadForm.landing_url.value}));
   ok('UTM/gclid/li_fat_id capturados nos campos ocultos',hid.s==='linkedin'&&hid.m==='paid'&&hid.g==='G123'&&hid.l==='L456'&&hid.u.includes('/index.html'),JSON.stringify(hid));
   const dl=await pg.evaluate(()=>window.dataLayer.map(e=>e.event));
   ok('dataLayer: lp_view e scroll_depth',dl.includes('lp_view')&&dl.includes('scroll_depth'),dl.join(','));
   // links internos
   const links=await pg.evaluate(()=>[...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href')));
   const bad=[];for(const h of [...new Set(links)]){
    if(h.startsWith('#')){ if(h!=='#'&&!(await pg.evaluate(s=>!!document.querySelector(s),h)))bad.push(h)}
    else if(!/^https?:/.test(h)){const r=await pg.request.get(base+'/'+h.split('#')[0]);if(r.status()!==200)bad.push(h)}}
   ok(`links internos (${new Set(links).size} unicos) resolvem`,bad.length===0,bad.join(','));
   // FAQ
   await pg.click('details[data-faq] summary');await pg.waitForTimeout(300);ok('FAQ abre e dispara faq_open',(await pg.evaluate(()=>window.dataLayer.some(e=>e.event==='faq_open'))));
   // form: vazio
   await pg.click('#leadForm button[type=submit]');
   const inv=await pg.locator('[aria-invalid="true"]').count();ok('form vazio: 8 campos invalidos',inv===8,'invalidos='+inv);
   // email pessoal
   await pg.fill('#nome','Maria Teste');await pg.fill('#email','maria@gmail.com');await pg.click('#nome');
   await pg.click('#cargo');ok('e-mail pessoal rejeitado',(await pg.textContent('#err-email')).includes('corporativo'));
   await pg.fill('#email','maria@operadora-teste.com.br');await pg.fill('#cargo','Gerente');await pg.fill('#empresa','Operadora Teste');
   await pg.selectOption('#tipo_operadora',{index:1});await pg.selectOption('#erp',{index:1});await pg.fill('#desafio','Acompanhar sinistralidade com mais antecedencia.');
   await pg.click('#leadForm button[type=submit]');
   ok('consentimento obrigatorio',(await pg.textContent('#err-consentimento')).length>0&&pg.url().includes('index.html'));
   // honeypot
   await pg.check('#consentimento');await pg.evaluate(()=>{document.getElementById('website').value='bot'});
   await pg.click('#leadForm button[type=submit]');await pg.waitForTimeout(1000);ok('honeypot bloqueia envio',pg.url().includes('index.html'));
   await pg.evaluate(()=>{document.getElementById('website').value=''});
   await pg.click('#leadForm button[type=submit]');await pg.waitForURL(/obrigado/,{timeout:5000}).catch(()=>{});
   ok('submit valido (sem endpoint) vai para obrigado em modo homologacao',/obrigado\.html\?modo=homologacao/.test(pg.url()),pg.url());
   await pg.screenshot({path:'qa/obrigado-1440.png'});
   await pg.goto(base+'/politica-de-privacidade.html');await pg.screenshot({path:'qa/politica-1440.png'});
   ok('politica de privacidade carrega',(await pg.textContent('h1')).includes('Privacidade'));
   const jl=await pg.goto(base+'/index.html').then(()=>pg.evaluate(()=>[...document.querySelectorAll('script[type="application/ld+json"]')].map(s=>JSON.parse(s.textContent)['@type'])));
   ok('JSON-LD Organization e FAQPage validos',jl.includes('Organization')&&jl.includes('FAQPage'),jl.join(','));
  }
  await ctx.close();
 }
 ok('nenhuma requisicao externa (nada enviado/carregado fora do host local)',external.length===0,external.join(','));
 ok('nenhum POST/PUT recebido pelo servidor local',sent.length===0,sent.join(','));
 fs.writeFileSync(path.join(root,'qa/resultado.json'),JSON.stringify(res,null,1));
 await b.close();srv.close();
})();
