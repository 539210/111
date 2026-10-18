const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const root = __dirname;
http.createServer((req,res)=>{
 const name=decodeURIComponent(req.url.split('?')[0]);
 const file=path.resolve(root,'.'+(name==='/'?'/index.html':name));
 if(!file.startsWith(root+path.sep)){res.writeHead(403);return res.end('Forbidden');}
 fs.readFile(file,(err,data)=>{if(err){res.writeHead(404);return res.end('Not found');}res.setHeader('Content-Type',({'html':'text/html; charset=utf-8','css':'text/css','js':'text/javascript'})[file.split('.').pop()]||'application/octet-stream');res.end(data);});
}).listen(process.env.PORT||3000,'0.0.0.0',()=>console.log('ConvoLab running on port '+(process.env.PORT||3000)));
