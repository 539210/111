from pathlib import Path
import argparse,json,time,traceback,hashlib,os,sys
from collections import Counter
from mineru.parser import MinerUParser
from mineru.parser.writer import FileBasedDataWriter

def main():
    root=Path(__file__).parent
    ap=argparse.ArgumentParser()
    ap.add_argument('--limit',type=int,default=16)
    ap.add_argument('--only',default='')
    args=ap.parse_args()
    records=json.loads((root/'成果/样本输入/样本清单.json').read_text(encoding='utf-8'))
    if args.only: records=[r for r in records if r['sample_id'] in args.only.split(',')]
    records=records[:args.limit]
    out=root/'成果/样本输出'
    out.mkdir(parents=True,exist_ok=True)
    status_path=root/'进度/sample-status.json'
    status=json.loads(status_path.read_text(encoding='utf-8')) if status_path.exists() else {}
    def checkpoint():
        tmp=status_path.with_suffix('.tmp')
        tmp.write_text(json.dumps(status,ensure_ascii=False,indent=2),encoding='utf-8');tmp.replace(status_path)
    parser=MinerUParser(tier='basic',parse_mode='ocr',image_analysis=True)
    for record in records:
        sid=record['sample_id'];target=out/sid
        if status.get(sid,{}).get('state')=='parsed' and (target/'middle_json.json').exists():
            print('SKIP',sid,flush=True);continue
        start=time.perf_counter()
        status[sid]={'state':'running','source':record,'started_at':time.strftime('%Y-%m-%d %H:%M:%S')};checkpoint()
        print('START',sid,flush=True)
        try:
            result=parser.parse(record['input'])
            result.save(FileBasedDataWriter(str(target)))
            structured=json.loads((target/'structured_content.json').read_text(encoding='utf-8'))
            counts=Counter(b['type'] for p in structured['pages'] for b in p['blocks'])
            md=(target/'markdown.md').read_text(encoding='utf-8')
            (target/'source.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
            status[sid].update(state='parsed',seconds=round(time.perf_counter()-start,3),pages=len(structured['pages']),blocks=dict(counts),markdown_chars=len(md),image_files=len(list((target/'images').glob('*'))) if (target/'images').exists() else 0)
            print('DONE',sid,json.dumps(status[sid],ensure_ascii=False),flush=True)
        except Exception as exc:
            status[sid].update(state='failed',seconds=round(time.perf_counter()-start,3),error=str(exc),traceback=traceback.format_exc())
            traceback.print_exc()
        checkpoint()
    print('FINISHED',json.dumps({k:v['state'] for k,v in status.items()}),flush=True)
    if any(status[r['sample_id']]['state']=='failed' for r in records):sys.exit(1)

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    main()
