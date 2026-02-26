#!/usr/bin/env python3
"""
Copia arquivos em optimized/ para nomes seguros (substitui espaços e parênteses por '-')
Retorna um mapeamento console-friendly para uso em mudanças de HTML.
"""
import os
import shutil

ROOT = 'optimized'

if not os.path.isdir(ROOT):
    print('optimized/ não existe. Rode optimize-images.py primeiro.')
    exit(1)

mapping = {}
for root, dirs, files in os.walk(ROOT):
    for f in files:
        src = os.path.join(root, f)
        safe = f.replace(' ', '-').replace('(', '').replace(')', '').replace(',', '').replace("'", '')
        dst = os.path.join(root, safe)
        if src != dst:
            shutil.copy2(src, dst)
        rel_src = os.path.relpath(src, ROOT)
        rel_dst = os.path.relpath(dst, ROOT)
        mapping[rel_src] = rel_dst

print('Mapping (original -> safe):')
for k,v in mapping.items():
    print(k, '->', v)
print('Concluído')
