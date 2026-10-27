from pathlib import Path
import json,time,hashlib
import pypdfium2 as pdfium

root=Path(__file__).parent
out=root/'成果'/'样本输入'
out.mkdir(parents=True,exist_ok=True)
books=json.loads((root.parent/'PDF提取评估_20261027'/'inspection.json').read_text(encoding='utf-8'))
selections=[[9,20,21,92],[9,20,21,105],[9,30,31,87],[9,20,21,31]]
records=[]
for bi,(book,pages) in enumerate(zip(books,selections),1):
    src=Path(book['file'])
    h=hashlib.sha256()
    with src.open('rb') as f:
        for chunk in iter(lambda:f.read(4*1024*1024),b''):h.update(chunk)
    doc=pdfium.PdfDocument(str(src))
    for num in pages:
        page=doc[num-1]
        dst=out/f'b{bi}_p{num:03d}.png'
        page.render(scale=300/72).to_pil().save(dst)
        tp=page.get_textpage()
        text=tp.get_text_range()
        (out/f'b{bi}_p{num:03d}_old_ocr.txt').write_text(text,encoding='utf-8')
        records.append({'sample_id':dst.stem,'book':src.name,'source':str(src),'source_sha256':h.hexdigest(),'pdf_page':num,'input':str(dst),'render_dpi':300,'page_size_points':list(page.get_size()),'old_ocr_chars':len(text)})
        tp.close();page.close()
    doc.close()
(out/'样本清单.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Prepared {len(records)} samples')
