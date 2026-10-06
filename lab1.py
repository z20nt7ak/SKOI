from PIL import Image
import time

start = time.perf_counter()
image = Image.open("image.jpeg").convert("L")
width, height = image.size
pixels = image.load()

G_x = [ [-1, 0, 1], [-2, 0, 2],[-1, 0, 1]]
G_y = [[-1, -2, -1],[0, 0, 0],[1, 2, 1]]

result = Image.new("L", (width, height))
result_pixels = result.load()

for y in range(1, height - 1):
    for x in range(1, width - 1):
        gradient_x = 0
        gradient_y = 0
        for kx in range(-1, 2):
            for ky in range(-1, 2):
                pixel = pixels[x + kx, y + ky]
                gradient_x += pixel * G_x[ky + 1][kx + 1]
                gradient_y += pixel * G_y[ky + 1][kx + 1]
        G = (gradient_x ** 2 + gradient_y ** 2) ** 0.5
        if G > 255:
            G = 255
        result_pixels[x, y] = int(G)

result.save("result.jpeg")
end = time.perf_counter()
print("Нативная версия:", end - start, "секунд")