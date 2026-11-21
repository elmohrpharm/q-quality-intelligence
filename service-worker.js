const CACHE='qquality-2025-baltim-shell-v4';
const CORE=['./','./index.html','./sat.html','./achievement.html','./handbook.html','./style.css','./data.js','./workbook-rows.js','./app.js','./bilingual.js','./assets/qpharm-logo.png','./manifest.webmanifest','./icon-192.png','./icon-512.png'];
self.addEventListener('install',e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting())));
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(x=>x.startsWith('qquality-2025-baltim-shell-')&&x!==CACHE).map(x=>caches.delete(x)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',e=>{if(e.request.method!=='GET'||new URL(e.request.url).origin!==self.location.origin)return;e.respondWith(caches.match(e.request).then(v=>v||fetch(e.request).then(res=>{if(res.ok&&e.request.url.includes('/assets/')){let copy=res.clone();caches.open(CACHE).then(c=>c.put(e.request,copy)).catch(()=>{});}return res;})))});
