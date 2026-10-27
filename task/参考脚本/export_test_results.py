from pathlib import Path
import json,re,csv,statistics,html,hashlib
from collections import Counter
from bs4 import BeautifulSoup
from markdown_it import MarkdownIt
from latex2mathml.converter import convert

root=Path(__file__).parent
base=root/'成果/样本输出'
status=json.loads((root/'进度/sample-status.json').read_text(encoding='utf-8'))
summary=[]; all_formulas=[]; failures=[]; broken=[]; math_errors=[]
md_parser=MarkdownIt('commonmark',{'html':True}).enable('table')
def math_html(latex,display=False):
    try:return convert(latex,display='block' if display else 'inline')
    except Exception as e:
        math_errors.append({'latex':latex,'error':str(e)})
        return '<code>'+html.escape(latex)+'</code>'
def walk(obj):
    if isinstance(obj,dict):
        yield obj
        for v in obj.values():yield from walk(v)
    elif isinstance(obj,list):
        for v in obj:yield from walk(v)
for sid,s in sorted(status.items()):
    folder=base/sid
    if s['state']!='parsed':failures.append(sid);continue
    raw=json.loads((folder/'middle_json.json').read_text(encoding='utf-8'))
    formulas=[];table_count=0; refs=set()
    for node in walk(raw):
        typ=node.get('type','');content=node.get('content')
        if typ.startswith('equation') and isinstance(content,str):
            formulas.append({'type':typ,'latex':content})
        if isinstance(content,str) and '<eq>' in content:
            formulas.extend({'type':'table_equation','latex':m} for m in re.findall(r'<eq>(.*?)</eq>',content,re.S))
        if typ=='table_body' and isinstance(content,str):
            table_count+=1;td=folder/'tables';td.mkdir(exist_ok=True)
            (td/f'table_{table_count:02d}.html').write_text(content,encoding='utf-8')
            soup=BeautifulSoup(content,'html.parser');rows=[]
            for row in soup.select('tr'):
                rows.append([{'text':cell.get_text(' ',strip=True),'html':cell.decode_contents(),'rowspan':int(cell.get('rowspan',1)),'colspan':int(cell.get('colspan',1))} for cell in row.find_all(['th','td'],recursive=False)])
            (td/f'table_{table_count:02d}.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
            if all(c['rowspan']==c['colspan']==1 for row in rows for c in row):
                with (td/f'table_{table_count:02d}.csv').open('w',encoding='utf-8-sig',newline='') as f:csv.writer(f).writerows([[c['text'] for c in row] for row in rows])
        for key in ('image_path','image_source'):
            if isinstance(node.get(key),str):refs.add(node[key])
    for ref in refs:
        if not (folder/ref).is_file():broken.append({'sample':sid,'ref':ref})
    for i,f in enumerate(formulas,1):f.update(id=f'{sid}_formula_{i:03d}',sample=sid,source_page=s['source']['pdf_page'],review_status='unverified')
    all_formulas.extend(formulas)
    (folder/'formulas.jsonl').write_text(''.join(json.dumps(f,ensure_ascii=False)+'\n' for f in formulas),encoding='utf-8')
    md=(folder/'markdown.md').read_text(encoding='utf-8')
    slots=[]
    def slot(m,display=False):
        token=f'MATHSLOTZ{len(slots)}Z';slots.append(math_html(m.group(1).strip(),display));return token
    text=re.sub(r'\$\$(.*?)\$\$',lambda m:slot(m,True),md,flags=re.S)
    text=re.sub(r'(?<!\$)\$([^$\n]+)\$(?!\$)',slot,text)
    body=md_parser.render(text)
    for i,v in enumerate(slots):body=body.replace(f'MATHSLOTZ{i}Z',v)
    soup=BeautifulSoup(body,'html.parser')
    for eq in soup.find_all('eq'):eq.replace_with(BeautifulSoup(math_html(eq.get_text()),'html.parser'))
    for tag in soup(['script','iframe','object','embed']):tag.decompose()
    style='body{max-width:1000px;margin:35px auto;padding:0 24px;line-height:1.8;font-family:Microsoft YaHei,sans-serif}img{max-width:100%}table{border-collapse:collapse}td,th{border:1px solid #aaa;padding:5px 12px}math{font-size:1.12em}.note{padding:12px;background:#fff3d0}'
    page=f'<!doctype html><html lang="zh"><meta charset="utf-8"><title>{sid} 识别样本</title><style>{style}</style><h1>{sid}</h1><p class="note">机器识别样本，未逐字审核。公式可显示不代表正确。<a href="../../样本输入/{sid}.png">查看原页</a> · <a href="markdown.md">Markdown</a></p>{soup}</html>'
    (folder/'preview.html').write_text(page,encoding='utf-8')
    summary.append({'sample':sid,'seconds':s['seconds'],'formula_entries':len(formulas),'tables':table_count,'images':s['image_files'],'markdown_chars':s['markdown_chars']})
times=[s['seconds'] for s in summary]
report={'samples':summary,'successful_pages':len(summary),'failed_samples':failures,'total_seconds':sum(times),'median_seconds':statistics.median(times),'min_seconds':min(times),'max_seconds':max(times),'mean_seconds':statistics.mean(times),'formula_entries':len(all_formulas),'tables':sum(s['tables'] for s in summary),'assets':sum(s['images'] for s in summary),'broken_references':broken,'mathml_conversion_errors':math_errors,'note':'formula_entries includes inline and table formulas; all are unverified. No accuracy estimate.'}
(root/'成果/测试统计.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
links=''.join(f'<li><a href="样本输出/{s["sample"]}/preview.html">{s["sample"]}</a>：{s["seconds"]:.1f} 秒，公式{s["formula_entries"]}，表格{s["tables"]}，图像资源{s["images"]}</li>' for s in summary)
(root/'成果/测试结果索引.html').write_text(f'<!doctype html><html lang="zh"><meta charset="utf-8"><title>王道PDF模型测试</title><h1>16页本地模型测试</h1><p>输出尚未逐字审核。图像资源包括表格/公式兜底图，并非全部是教材插图。</p><ul>{links}</ul></html>',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='samples'},ensure_ascii=False,indent=2))
