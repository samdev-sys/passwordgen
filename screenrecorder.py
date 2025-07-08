import cv2
import numpy as np
from PIL import ImageGrab
import time

def screenRecorder():
    print("Iniciando grabación...")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1366, 768))

    cv2.namedWindow("screen Recorder", cv2. WINDOW_NORMAL)

    try:
        while True:
            # Captura la pantalla (puedes ajustar bbox para capturar solo una parte)
            img = ImageGrab.grab(bbox=(0, 0, 1366, 768))
            frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

            # Escribe el frame al archivo
            out.write(frame)

            # Muestra el frame en una única ventana (la misma siempre)
            # cv2.imshow("Screen Recorder", frame)

            # Espera para no saturar CPU ni refrescar tan rápido (20ms ≈ 50 FPS máx)
            if cv2.waitKey(20) & 0xFF == 27:  # ESC para salir
                break

    except Exception as e:
        print(f"Error durante la grabación: {e}")

    finally:
        out.release()
        cv2.destroyAllWindows()
        print("Grabación finalizada.")

if __name__ == "__main__":
    screenRecorder()
