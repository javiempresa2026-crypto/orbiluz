"""Deja las voces en off a ritmo de TikTok: acorta las pausas largas (máx. 0,25 s) y acelera un poco.
Uso: python3 tiktok/preparar_voz.py entrada.wav salida.wav [tempo]"""
import sys, wave, subprocess
import numpy as np
import imageio_ffmpeg
from faster_whisper import WhisperModel

FF = imageio_ffmpeg.get_ffmpeg_exe()


def preparar(entrada, salida, tempo=1.08, max_pausa=0.25):
    tmp = salida + ".mono.wav"
    subprocess.run([FF, "-y", "-loglevel", "error", "-i", entrada, "-ac", "1", "-ar", "48000", tmp], check=True)
    w = wave.open(tmp); sr = w.getframerate(); x = np.frombuffer(w.readframes(w.getnframes()), "<i2").copy()
    segs, _ = WhisperModel("small", device="cpu", compute_type="int8").transcribe(tmp, language="es", word_timestamps=True)
    ws = [p for s in segs for p in s.words]
    trozos, ini = [], 0
    for a, b in zip(ws, ws[1:]):
        if b.start - a.end > max_pausa:  # se queda con la mitad de la pausa a cada lado
            m = max_pausa / 2
            trozos.append(x[ini:int((a.end + m) * sr)]); ini = int((b.start - m) * sr)
    trozos.append(x[ini:int((ws[-1].end + 0.3) * sr)])
    fundido = int(0.01 * sr)
    for t in trozos:  # pequeños fundidos para que no haya chasquidos en los cortes
        t[:fundido] = (t[:fundido] * np.linspace(0, 1, fundido)).astype(t.dtype)
        t[-fundido:] = (t[-fundido:] * np.linspace(1, 0, fundido)).astype(t.dtype)
    y = np.concatenate(trozos)
    with wave.open(tmp, "w") as o:
        o.setnchannels(1); o.setsampwidth(2); o.setframerate(sr); o.writeframes(y.tobytes())
    subprocess.run([FF, "-y", "-loglevel", "error", "-i", tmp, "-af", f"atempo={tempo},loudnorm=I=-16:TP=-1.5", "-ar", "48000", salida], check=True)
    import os; os.remove(tmp)


if __name__ == "__main__":
    preparar(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 1.08)
