/* NeoHealth BI · OPS — landing page. Sem dependências. Nenhum dado é enviado se NH_CONFIG.formEndpoint estiver vazio. */
(function(){
  'use strict';
  // ===== CONFIG (editar na homologação/produção) =====
  window.NH_CONFIG = window.NH_CONFIG || {
    formEndpoint: '',            // [A CONFIRMAR] endpoint do CRM/automação. VAZIO = nenhum envio (modo homologação).
    thanksPage: 'obrigado.html',
    schedulerUrl: ''             // [A CONFIRMAR] URL Calendly/Cal.com. Vazio = placeholder exibido.
  };
  var CFG = window.NH_CONFIG;
  window.dataLayer = window.dataLayer || [];
  function track(ev, p){ var o = {event: ev}; for (var k in (p||{})) o[k]=p[k]; window.dataLayer.push(o); }
  window.nhTrack = track;

  track('lp_view', {page_name:'landing_neohealth_bi', page_path: location.pathname});

  // ===== Menu mobile =====
  var btn = document.getElementById('menuBtn'), nav = document.getElementById('mainNav');
  if(btn && nav){
    btn.addEventListener('click', function(){ var o = nav.classList.toggle('open'); btn.setAttribute('aria-expanded', o); });
    nav.addEventListener('click', function(e){ if(e.target.tagName==='A'){ nav.classList.remove('open'); btn.setAttribute('aria-expanded','false'); }});
  }

  // ===== CTAs =====
  document.addEventListener('click', function(e){
    var a = e.target.closest('[data-cta]'); if(!a) return;
    track('cta_click', {cta_id: a.getAttribute('data-cta'), cta_text: (a.textContent||'').trim(), cta_target: a.getAttribute('href')||''});
  });

  // ===== Profundidade de rolagem =====
  var marks = [25,50,75,100], fired = {};
  window.addEventListener('scroll', function(){
    var h = document.documentElement, pct = Math.round((h.scrollTop+window.innerHeight)/h.scrollHeight*100);
    marks.forEach(function(m){ if(pct>=m && !fired[m]){ fired[m]=1; track('scroll_depth',{percent:m}); }});
  }, {passive:true});

  // ===== Seções vistas =====
  if('IntersectionObserver' in window){
    var seen = {}, io = new IntersectionObserver(function(es){ es.forEach(function(en){
      if(en.isIntersecting && !seen[en.target.id]){ seen[en.target.id]=1; track('section_view',{section_id:en.target.id}); }});}, {threshold:.35});
    document.querySelectorAll('main section[id]').forEach(function(s){ io.observe(s); });
  }

  // ===== FAQ =====
  document.querySelectorAll('details[data-faq]').forEach(function(d){
    d.addEventListener('toggle', function(){ if(d.open) track('faq_open',{question:d.querySelector('summary').textContent.trim()}); });
  });

  // ===== Captura de UTM / click IDs =====
  var KEYS = ['utm_source','utm_medium','utm_campaign','utm_term','utm_content','gclid','li_fat_id','fbclid'];
  var store = {};
  try { store = JSON.parse(sessionStorage.getItem('nh_attr')||'{}'); } catch(_){ store = {}; }
  var qs = new URLSearchParams(location.search);
  KEYS.forEach(function(k){ var v = qs.get(k); if(v){ store[k] = v.slice(0,200); }});
  try { sessionStorage.setItem('nh_attr', JSON.stringify(store)); } catch(_){}
  var form = document.getElementById('leadForm');
  function fillHidden(){
    if(!form) return;
    KEYS.concat(['landing_url','referrer']).forEach(function(k){
      var el = form.elements[k]; if(!el) return;
      el.value = k==='landing_url' ? location.href.split('#')[0] : k==='referrer' ? (document.referrer||'') : (store[k]||'');
    });
  }
  fillHidden();

  // ===== Agendamento =====
  var sched = document.getElementById('schedBox');
  if(sched){
    if(CFG.schedulerUrl){
      sched.innerHTML = '<iframe title="Agendamento de demonstração" src="'+encodeURI(CFG.schedulerUrl)+'" style="width:100%;height:700px;border:0" loading="lazy"></iframe>';
    }
    var seenS = false;
    if('IntersectionObserver' in window){ new IntersectionObserver(function(es,o){ if(es[0].isIntersecting && !seenS){ seenS=true; track('schedule_view'); o.disconnect(); }}).observe(sched); }
  }

  // ===== Formulário =====
  if(!form) return;
  var started = false;
  form.addEventListener('focusin', function(){ if(!started){ started=true; track('form_start'); }});
  var FREE = ['gmail.com','hotmail.com','outlook.com','yahoo.com','yahoo.com.br','live.com','icloud.com','bol.com.br','uol.com.br','terra.com.br','msn.com','proton.me','protonmail.com'];
  var rules = {
    nome:   function(v){ return v.trim().length>=3 || 'Informe seu nome completo.'; },
    email:  function(v){
      if(!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim())) return 'Informe um e-mail válido.';
      var d = v.trim().split('@')[1].toLowerCase();
      return FREE.indexOf(d)===-1 || 'Use seu e-mail corporativo.'; },
    cargo:  function(v){ return v.trim().length>=2 || 'Informe seu cargo.'; },
    empresa:function(v){ return v.trim().length>=2 || 'Informe o nome da operadora/empresa.'; },
    tipo_operadora:function(v){ return v!=='' || 'Selecione o tipo de organização.'; },
    erp:    function(v){ return v!=='' || 'Selecione o ERP utilizado.'; },
    desafio:function(v){ return v.trim().length>=10 || 'Descreva brevemente seu principal desafio (mín. 10 caracteres).'; },
    consentimento:function(_,el){ return el.checked || 'É necessário aceitar o tratamento de dados para enviar.'; }
  };
  function validateField(el){
    var r = rules[el.name]; if(!r) return true;
    var res = r(el.value, el), box = document.getElementById('err-'+el.name);
    if(res!==true){ el.setAttribute('aria-invalid','true'); if(box) box.textContent = res; return false; }
    el.removeAttribute('aria-invalid'); if(box) box.textContent=''; return true;
  }
  Object.keys(rules).forEach(function(n){
    var el = form.elements[n]; if(!el) return;
    el.addEventListener('blur', function(){ validateField(el); });
    el.addEventListener('input', function(){ if(el.getAttribute('aria-invalid')) validateField(el); });
    el.addEventListener('change', function(){ if(el.getAttribute('aria-invalid')) validateField(el); });
  });
  var status = document.getElementById('formStatus');
  form.addEventListener('submit', function(e){
    e.preventDefault();
    if(form.elements.website && form.elements.website.value){ return; } // honeypot: descarta silenciosamente
    var bad = [];
    Object.keys(rules).forEach(function(n){ var el=form.elements[n]; if(el && !validateField(el)) bad.push(n); });
    track('form_submit_attempt');
    if(bad.length){ track('form_validation_error',{fields:bad.join(',')}); form.elements[bad[0]].focus(); return; }
    var data = {}; new FormData(form).forEach(function(v,k){ if(k!=='website') data[k]=v; });
    // dataLayer: NÃO inclui dados pessoais (sem nome/e-mail).
    var done = function(mode){
      track('generate_lead',{form_id:'lead_demo', operadora_tipo:data.tipo_operadora, erp:data.erp, delivery:mode});
      location.href = CFG.thanksPage + (mode==='homologacao'?'?modo=homologacao':'');
    };
    if(!CFG.formEndpoint){ // modo homologação: nada é enviado
      if(status){ status.textContent='Modo homologação: formulário validado; nenhum dado foi enviado.'; status.className='status show'; }
      setTimeout(function(){ done('homologacao'); }, 600); return;
    }
    fetch(CFG.formEndpoint,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)})
      .then(function(r){ if(!r.ok) throw new Error(r.status); done('endpoint'); })
      .catch(function(){ if(status){ status.textContent='Não foi possível enviar agora. Tente novamente em instantes.'; status.className='status show'; } track('form_submit_error'); });
  });
})();
