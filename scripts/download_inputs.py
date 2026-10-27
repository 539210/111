"""Download private input release assets via authenticated gh; never print tokens."""
from pathlib import Path
import hashlib,json,subprocess,sys

ROOT=Path(__file__).resolve().parents[1]
REPO='539210/111'
TAG='input-v1'

def digest(path):
    with path.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()

def main():
    entries=json.loads((ROOT/'task/release-inputs.json').read_text(encoding='utf-8'))
    dest=ROOT/'inputs';dest.mkdir(exist_ok=True)
    for entry in entries:
        final=dest/entry['filename']
        if final.is_file() and final.stat().st_size==entry['bytes'] and digest(final)==entry['sha256']:
            print(f"Verified existing {entry['book_id']}");continue
        asset=dest/entry['asset_name']
        if asset.exists():
            if asset.stat().st_size!=entry['bytes'] or digest(asset)!=entry['sha256']:
                raise RuntimeError(f"Existing downloaded asset has unexpected bytes: {asset.name}. Inspect it before retrying.")
        else:
            subprocess.run(['gh','release','download',TAG,'--repo',REPO,'--pattern',entry['asset_name'],'--dir',str(dest)],check=True)
        if asset.stat().st_size!=entry['bytes'] or digest(asset)!=entry['sha256']:
            raise RuntimeError(f"Input verification failed: {entry['book_id']}; do not parse this file")
        if final.exists():
            raise RuntimeError(f"Unverified target already exists: {final.name}; preserve and inspect it before retrying")
        asset.replace(final)
        print(f"Downloaded and verified {entry['book_id']}")
    print('All release inputs verified. Full extraction has not been started.')

if __name__=='__main__':main()
