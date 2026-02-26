#!/usr/bin/env python3
"""
Script simples para gerar versões otimizadas (webp + jpg) em várias larguras.
Gera saídas em optimized/<relative_path>/
Dependências: Pillow
Usage: python3 optimize-images.py
"""
import os
from PIL import Image

SIZES = [480, 800, 1200, 1600]
INPUT_DIR = 'images'
OUT_DIR = 'optimized'

if not os.path.isdir(INPUT_DIR):
    print('Diretório images/ não existe. Saindo.')
    exit(1)

for root, dirs, files in os.walk(INPUT_DIR):
    rel = os.path.relpath(root, INPUT_DIR)
    out_sub = os.path.join(OUT_DIR, rel) if rel != '.' else OUT_DIR
    os.makedirs(out_sub, exist_ok=True)
    for f in files:
        if not f.lower().endswith(('.png','.jpg','.jpeg')):
            continue
        in_path = os.path.join(root, f)
        name, ext = os.path.splitext(f)
        try:
            img = Image.open(in_path)
        except Exception as e:
            print('Não foi possível abrir', in_path, e)
            continue
        for w in SIZES:
            # calcular altura proporcional
            w = int(w)
            ratio = w / img.width
            h = int(img.height * ratio)
            resized = img.resize((w, h), Image.LANCZOS)
            out_jpg = os.path.join(out_sub, f"{name}-{w}.jpg")
            out_webp = os.path.join(out_sub, f"{name}-{w}.webp")
            try:
                resized.save(out_jpg, 'JPEG', quality=85, optimize=True)
                resized.save(out_webp, 'WEBP', quality=80, method=6)
                print('Gerado', out_jpg, out_webp)
            except Exception as e:
                print('Erro ao salvar', out_jpg, e)
print('Concluído')
