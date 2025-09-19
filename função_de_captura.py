import pyautogui
import time

print("📌 Em 5 segundos, posicione o mouse no CANTO SUPERIOR ESQUERDO da mensagem...")
time.sleep(5)
x1, y1 = pyautogui.position()
print(f"🔴 Topo esquerdo: {x1}, {y1}")

print("📌 Agora em 5 segundos posicione o mouse no CANTO INFERIOR DIREITO da mensagem...")
time.sleep(5)
x2, y2 = pyautogui.position()
print(f"🟢 Base direita: {x2}, {y2}")

largura = x2 - x1
altura = y2 - y1

imagem = pyautogui.screenshot(region=(x1, y1, largura, altura))
imagem.save("nenhum_usuario.png")

print("✅ Imagem salva como 'nenhum_usuario.png'")

print(f'x1= {x1}  y1= {y1}       x2= {x2}  y2= {y2}')
print(f'largura= {largura}')
print(f'altura= {altura}')
print("📸 Imagem modelo salva como 'nenhum_usuario.png'")