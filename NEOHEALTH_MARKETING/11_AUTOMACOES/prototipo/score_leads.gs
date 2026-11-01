/**
 * Protótipo Google Apps Script — lead scoring. NÃO envia e-mail/WhatsApp, NÃO chama serviços externos.
 * Planilha: aba "Leads" (cabeçalho na linha 1: id,email,tipo_operadora,porte,cargo,erp,desafios,interesse,consentimento_contato,concorrente,estudante)
 * Aba "Regras" = conteúdo de lead_scoring.csv. Resultado: colunas score e classe ao final da aba Leads.
 * Instalação [REQUER APROVAÇÃO]: colar em Extensões > Apps Script da planilha. Execução manual pelo menu.
 */
function onOpen() { SpreadsheetApp.getUi().createMenu('NeoHealth').addItem('Calcular score', 'calcularScore').addToUi(); }
function norm_(s) { return String(s||'').normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase().trim().replace(/\s+/g,' '); }
function calcularScore() {
  var ss = SpreadsheetApp.getActive(), sh = ss.getSheetByName('Leads'), rg = ss.getSheetByName('Regras').getDataRange().getValues();
  var regras = {}, classes = [];
  for (var i=1;i<rg.length;i++){ var d=rg[i][0], v=rg[i][1], p=Number(rg[i][2]), t=rg[i][3];
    if (d==='classe') classes.push([v,p]); else { regras[d]=regras[d]||{}; regras[d][norm_(v)]=[p,t]; } }
  classes.sort(function(a,b){return b[1]-a[1];});
  var data = sh.getDataRange().getValues(), h = data[0], ix = {}; h.forEach(function(c,i){ix[c]=i;});
  var FREE=['gmail.com','hotmail.com','outlook.com','yahoo.com','yahoo.com.br','uol.com.br','bol.com.br','icloud.com','live.com'];
  function soma(dim, vals){ var tot=0, teto=null; vals.forEach(function(x){ var r=(regras[dim]||{})[norm_(x)]; if(r){tot+=r[0]; teto=Number(r[1]);} }); return teto!==null?Math.min(tot,teto):tot; }
  function sim(x){ return ['sim','s','1','true'].indexOf(norm_(x))>=0; }
  var out=[];
  for (var r=1;r<data.length;r++){ var l=data[r], total=0;
    ['tipo_operadora','porte','cargo','erp'].forEach(function(k){ total+=soma(k,[l[ix[k]]]); });
    ['desafios','interesse'].forEach(function(k){ total+=soma(k,String(l[ix[k]]||'').split(';')); });
    var dom=String(l[ix.email]).split('@').pop().toLowerCase();
    if (FREE.indexOf(dom)>=0) total-=10;
    var elim = sim(l[ix.concorrente])||sim(l[ix.estudante])||!sim(l[ix.consentimento_contato]);
    total=Math.max(0,Math.min(100,total)); var classe='Descarte';
    if(!elim) for (var c=0;c<classes.length;c++){ if(classes[c][0]!=='Descarte' && total>=classes[c][1]){classe=classes[c][0];break;} }
    out.push([total,classe]);
  }
  var col=h.length+1; sh.getRange(1,col,1,2).setValues([['score','classe']]);
  if(out.length) sh.getRange(2,col,out.length,2).setValues(out);
}
